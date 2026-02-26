"""
Simple Job Scraper & IP Address Analyzer
=========================================
- Scrapes job postings from RemoteOK using BeautifulSoup
- Analyzes IP address and TCP/IP details of the target website
- Exports results to JSON
"""

import socket
import ssl
import time
import json
import ipaddress
from datetime import datetime

import requests
from bs4 import BeautifulSoup


# ──────────────────────────────────────────────
# PART 1: IP Address & Network Analysis
# ──────────────────────────────────────────────

def analyze_ip(hostname):
    """Resolve hostname to IP and analyze it."""
    print(f"\n{'='*50}")
    print(f"  IP & NETWORK ANALYSIS: {hostname}")
    print(f"{'='*50}")

    # Step 1: DNS Resolution (Domain → IP Address)
    print("\n[1] DNS Resolution...")
    start = time.time()
    ip_address = socket.gethostbyname(hostname)
    dns_time = (time.time() - start) * 1000
    print(f"    Hostname  : {hostname}")
    print(f"    IP Address: {ip_address}")
    print(f"    DNS Time  : {dns_time:.2f} ms")

    # Step 2: IP Address Classification
    print("\n[2] IP Address Classification...")
    ip_obj = ipaddress.ip_address(ip_address)
    first_octet = int(ip_address.split(".")[0])

    if first_octet <= 127:
        ip_class = "A"
    elif first_octet <= 191:
        ip_class = "B"
    elif first_octet <= 223:
        ip_class = "C"
    elif first_octet <= 239:
        ip_class = "D (Multicast)"
    else:
        ip_class = "E (Reserved)"

    print(f"    IP Version : IPv{ip_obj.version}")
    print(f"    Class      : {ip_class}")
    print(f"    Private?   : {ip_obj.is_private}")
    print(f"    Global?    : {ip_obj.is_global}")
    print(f"    Loopback?  : {ip_obj.is_loopback}")

    # Step 3: TCP Connection Test
    print("\n[3] TCP Connection (Port 443 - HTTPS)...")
    start = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((hostname, 443))
    tcp_time = (time.time() - start) * 1000
    print(f"    TCP Handshake: {tcp_time:.2f} ms")

    # Step 4: SSL/TLS Info
    print("\n[4] SSL/TLS Certificate...")
    context = ssl.create_default_context()
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(f"    TLS Version: {ssock.version()}")
        cert = ssock.getpeercert()
        if cert:
            issuer = dict(x[0] for x in cert.get("issuer", []))
            print(f"    Issuer     : {issuer.get('organizationName', 'N/A')}")
            print(f"    Expires    : {cert.get('notAfter', 'N/A')}")

    # TCP/IP Summary
    print("\n[5] TCP/IP Protocol Summary:")
    print("    Layer 4 (Application) : HTTP/HTTPS request")
    print("    Layer 3 (Transport)   : TCP 3-way handshake (SYN→SYN-ACK→ACK)")
    print("    Layer 2 (Internet)    : IP packet routing to", ip_address)
    print("    Layer 1 (Link)        : Physical network (Ethernet/Wi-Fi)")

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "dns_time_ms": round(dns_time, 2),
        "ip_class": ip_class,
        "is_private": ip_obj.is_private,
        "tcp_handshake_ms": round(tcp_time, 2),
    }


# ──────────────────────────────────────────────
# PART 2: Job Scraping with BeautifulSoup
# ──────────────────────────────────────────────

def scrape_jobs(max_jobs=20):
    """Scrape job postings from RemoteOK."""
    print(f"\n{'='*50}")
    print("  SCRAPING JOB POSTINGS (RemoteOK)")
    print(f"{'='*50}")

    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/122.0.0.0"}

    print(f"\n  Fetching: {url}")
    start = time.time()
    response = requests.get(url, headers=headers, timeout=30)
    elapsed = (time.time() - start) * 1000

    print(f"  Status  : {response.status_code}")
    print(f"  Time    : {elapsed:.0f} ms")
    print(f"  Size    : {len(response.content) / 1024:.1f} KB")

    # Parse JSON (first item is metadata, skip it)
    data = response.json()
    job_list = data[1: max_jobs + 1]

    print(f"  Jobs    : {len(job_list)} extracted\n")

    # Parse each job using BeautifulSoup (for HTML descriptions)
    jobs = []
    print(f"  {'#':<4} {'Title':<35} {'Company':<20} {'Location':<15}")
    print(f"  {'-'*4} {'-'*35} {'-'*20} {'-'*15}")

    for i, entry in enumerate(job_list, 1):
        # Use BeautifulSoup to clean HTML from description
        raw_desc = entry.get("description", "")
        clean_desc = BeautifulSoup(raw_desc, "lxml").get_text(strip=True)[:150]

        title = entry.get("position", "N/A")
        company = entry.get("company", "N/A")
        location = entry.get("location", "") or "Remote"
        tags = entry.get("tags", []) or []
        date = entry.get("date", "")

        # Salary
        sal_min = entry.get("salary_min")
        sal_max = entry.get("salary_max")
        salary = f"${sal_min:,}–${sal_max:,}" if sal_min and sal_max else "Not listed"

        job = {
            "title": title,
            "company": company,
            "location": location,
            "salary": salary,
            "tags": tags,
            "description": clean_desc,
            "url": f"https://remoteok.com{entry.get('url', '')}",
            "date_posted": date,
        }
        jobs.append(job)

        print(f"  {i:<4} {title[:35]:<35} {company[:20]:<20} {location[:15]:<15}")

    return jobs


# ──────────────────────────────────────────────
# PART 3: Save Results
# ──────────────────────────────────────────────

def save_results(jobs, network_info):
    """Save everything to a JSON file."""
    output = {
        "scraped_at": datetime.now().isoformat(),
        "network_analysis": network_info,
        "total_jobs": len(jobs),
        "jobs": jobs,
    }

    filename = "scraped_jobs.json"
    with open(filename, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  ✓ Saved {len(jobs)} jobs to {filename}")


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

if __name__ == "__main__":
    # Analyze IP address of the target website
    network_info = analyze_ip("remoteok.com")

    # Scrape job postings
    jobs = scrape_jobs(max_jobs=20)

    # Save to file
    save_results(jobs, network_info)

    print(f"\n{'='*50}")
    print("  DONE!")
    print(f"{'='*50}\n")
