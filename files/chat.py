import socket
import threading
import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#  UI & COLORS
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def print_banner():
    print(f"{Colors.HEADER}")
    print("╔════════════════════════════════════════╗")
    print("║                                        ║")
    print("║             ENCRYPTED CHAT             ║")
    print("║                                        ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")

# CRYPTOGRAPHY
class CryptoHandler:
    def __init__(self):
        # 1. Generate RSA Keys (2048 bits)
        self.key_pair = RSA.generate(2048)
        self.public_key = self.key_pair.publickey()
        self.session_key = None  # Will be established during handshake

    def get_public_bytes(self):
        """Export public key in PEM format."""
        return self.public_key.export_key(format='PEM')

    def encrypt_session_key(self, other_public_pem):
        """(Host) Generate AES key, encrypt with Client's Public RSA."""
        # Import Client's Public Key
        recipient_key = RSA.import_key(other_public_pem)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        
        # Generate random AES-256 Key (32 bytes)
        self.session_key = get_random_bytes(32)
        
        # Encrypt the session key
        enc_session_key = cipher_rsa.encrypt(self.session_key)
        return enc_session_key

    def decrypt_session_key(self, encrypted_key_bytes):
        """(Client) Decrypt the received AES key with my Private RSA."""
        cipher_rsa = PKCS1_OAEP.new(self.key_pair)
        self.session_key = cipher_rsa.decrypt(encrypted_key_bytes)

    def encrypt_message(self, plaintext):
        """Encrypt message using AES-CBC with PKCS7 padding."""
        if not self.session_key: raise ValueError("No Session Key")
        
        # Generate IV (Initialization Vector)
        iv = get_random_bytes(16)
        cipher_aes = AES.new(self.session_key, AES.MODE_CBC, iv)
        
        # Pad data to be multiple of 16 bytes
        padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
        ciphertext = cipher_aes.encrypt(padded_text)
        
        # Return IV + Ciphertext (IV is needed for decryption)
        return iv + ciphertext

#	"""Decrypt message."""
    def decrypt_message(self, payload):
        if not self.session_key: raise ValueError("No Session Key")
        
        # Extract IV (first 16 bytes) and Ciphertext
        iv = payload[:16]
        ciphertext = payload[16:]
        
        cipher_aes = AES.new(self.session_key, AES.MODE_CBC, iv)
        
        try:
            padded_plaintext = cipher_aes.decrypt(ciphertext)
            plaintext = unpad(padded_plaintext, AES.block_size)
            return plaintext.decode('utf-8')
        except (ValueError, KeyError):
            return "[Decryption Failed - Data Corrupted]"

#  NETWORKING & CHAT LOGIC
class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.crypto = CryptoHandler()

    def start(self):
        print_banner()
        mode = input("Select Mode: (1) Host Server  (2) Connect to Server: ").strip()
        
        if mode == '1':
            self.run_server()
        elif mode == '2':
            ip = input("Enter Server IP (e.g., 127.0.0.1): ").strip()
            self.run_client(ip)
        else:
            print("Invalid selection.")

    def perform_handshake(self, conn, is_server):
        print(f"{Colors.BLUE}[*] Starting Secure Handshake...{Colors.RESET}")
        
        # 1. Send My Public Key
        my_pub = self.crypto.get_public_bytes()
        conn.sendall(len(my_pub).to_bytes(4, 'big'))
        conn.sendall(my_pub)

        # 2. Receive Their Public Key
        other_size = int.from_bytes(conn.recv(4), 'big')
        other_pub = conn.recv(other_size)
        
        # 3. Establish Session Key
        if is_server:
            print(f"{Colors.BLUE}[*] Generating AES Session Key...{Colors.RESET}")
            enc_key = self.crypto.encrypt_session_key(other_pub)
            conn.sendall(len(enc_key).to_bytes(4, 'big'))
            conn.sendall(enc_key)
        else:
            print(f"{Colors.BLUE}[*] Waiting for Session Key...{Colors.RESET}")
            key_size = int.from_bytes(conn.recv(4), 'big')
            enc_key = conn.recv(key_size)
            self.crypto.decrypt_session_key(enc_key)

        print(f"{Colors.GREEN}[+] Secure Connection Established!{Colors.RESET}")
        print("-" * 40)

    def run_server(self):
        self.sock.bind(('0.0.0.0', 9999))
        self.sock.listen(1)
        print(f"{Colors.BLUE}[*] Listening on port 9999...{Colors.RESET}")
        
        conn, addr = self.sock.accept()
        print(f"{Colors.GREEN}[+] Connected to {addr[0]}{Colors.RESET}")
        
        self.perform_handshake(conn, is_server=True)
        self.chat_loop(conn)

    def run_client(self, ip):
        try:
            self.sock.connect((ip, 9999))
            self.perform_handshake(self.sock, is_server=False)
            self.chat_loop(self.sock)
        except ConnectionRefusedError:
            print(f"{Colors.RED}[!] Could not connect.{Colors.RESET}")

    def chat_loop(self, conn):
        listener = threading.Thread(target=self.receive_messages, args=(conn,), daemon=True)
        listener.start()

        try:
            while True:
                msg = input()
                if msg.lower() == 'exit': break
                
                encrypted_package = self.crypto.encrypt_message(msg)
                conn.sendall(len(encrypted_package).to_bytes(4, 'big') + encrypted_package)
                
                # Visual cleanup
                sys.stdout.write("\033[F") 
                print(f"{Colors.GREEN}You:{Colors.RESET} {msg}")
                
        except (BrokenPipeError, ConnectionResetError):
            print(f"{Colors.RED}[!] Connection closed.{Colors.RESET}")
        finally:
            conn.close()

    def receive_messages(self, conn):
        try:
            while True:
                raw_len = conn.recv(4)
                if not raw_len: break
                msg_len = int.from_bytes(raw_len, 'big')
                
                data = b""
                while len(data) < msg_len:
                    packet = conn.recv(msg_len - len(data))
                    if not packet: break
                    data += packet

                plaintext = self.crypto.decrypt_message(data)
                print(f"\r{Colors.BLUE}Partner:{Colors.RESET} {plaintext}\nYou: ", end="")
        except:
            print(f"\n{Colors.RED}[!] Connection Lost.{Colors.RESET}")
            os._exit(0)

if __name__ == "__main__":
    client = ChatClient()
    client.start()
