# Task 1: Introduction to Version Control and Git Basics

## Task Overview

This task focused on understanding version control fundamentals and exploring Git through hands-on practice. Key activities included Git installation, repository management, branching, conflict resolution, and remote repository integration with AI-assisted cheatsheet creation.

---

## Theory of Version Control

Version control tracks and manages file changes over time, enabling collaboration, history tracking, and error recovery.

**Version Control Types:**
- **Local VCS**: Single computer tracking
- **Centralized VCS**: Central server (SVN) - single point of failure
- **Distributed VCS**: Complete local copies (Git) - best for collaboration

**Git Benefits:** Complete local history, powerful branching, offline work, and industry-standard adoption.

---

## Git Installation and Configuration

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Hands-on Git Commands

### Basic Workflow
```bash
# Initialize repository
git init
echo "# Project" > README.md
git add .
git commit -m "Initial commit"

# Check status and history
git status
git log --oneline
```

### Branching and Merging
```bash
# Create feature branch
git checkout -b feature-navbar
echo "<nav>Menu</nav>" > navbar.html
git add navbar.html
git commit -m "Add navbar"

# Merge to main
git checkout main
git merge feature-navbar
```

### Merge Conflicts
```bash
# Create conflict, resolve manually, then:
git add resolved-file.txt
git commit -m "Resolve conflict"
```

### Git Revert (Undo Mistakes)
```bash
echo "Bug" > bug.js
git add bug.js
git commit -m "Buggy feature"
git revert HEAD  # Safely undo
```

### Cherry-Pick (Selective Commits)
```bash
git checkout -b experimental
# Multiple commits...
git checkout main
git cherry-pick <commit-hash>  # Apply specific commit only
```

---

## Remote Repository Interaction

```bash
# Connect to GitHub/GitLab
git remote add origin https://github.com/username/repo.git
git push -u origin main

# Clone and pull
git clone https://github.com/username/repo.git
git pull origin main
```

---

## Git Commands Cheatsheet (AI-Assisted)

A comprehensive cheatsheet covering 100+ Git commands was created using AI assistance, organized by categories with practical examples.

**📋 Access Cheatsheet:**  
[Git Commands Cheatsheet](https://github.com/28d33/Cheatsheets/blob/main/git.md)

---

## Learning Outcome

**Skills Achieved:**
- Mastered Git installation and configuration
- Proficient in basic workflow (add, commit, push, pull)
- Successfully managed branches and resolved conflicts
- Applied `git revert` for safe rollbacks
- Used `git cherry-pick` for selective integration
- Integrated local and remote repositories


---

# Secure Local Login System 🛡️

A **defensive-by-design** authentication system built with Node.js, Express, and Docker. This project implements a full **Role-Based Access Control (RBAC)** system with "Defense-in-Depth" security principles, running entirely locally using DynamoDB Local and self-signed TLS.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Security](https://img.shields.io/badge/Security-High-green)
![Docker](https://img.shields.io/badge/Containerized-Docker-blue)

## 🚀 Key Features

* **Role-Based Access Control (RBAC):** Distinct flows for `User` (Dashboard) and `Admin` (User Management).
* **Transport Security:** Enforced **HTTPS/TLS 1.3** using self-signed certificates.
* **Session Security:** **HttpOnly, Secure, SameSite** Cookies preventing XSS token theft.
* **Brute Force Protection:** Rate limiting blocking IPs after 5 failed attempts.
* **Database Security:** DynamoDB Local with **NoSQL Injection** protection logic.
* **Password Hashing:** Industry-standard **bcrypt** with per-user salting.
* **CSRF Protection:** Synchronized Token Pattern via `csurf`.
* **Secure Headers:** Helmet.js implementation (CSP, HSTS, No-Sniff).

## 🛠️ Tech Stack

* **Backend:** Node.js, Express
* **Database:** Amazon DynamoDB Local
* **Infrastructure:** Docker, Docker Compose
* **Frontend:** Vanilla HTML/CSS/JS (No frameworks, strict CSP)
* **Security Libs:** `helmet`, `csurf`, `bcrypt`, `express-rate-limit`, `jsonwebtoken`

## 📂 Project Structure

```bash
secure-login-system/
├── backend/
│   ├── certs/          # Self-signed TLS keys (Not in repo)
│   ├── src/
│   │   └── server.js   # Core API & Security Middleware
│   ├── Dockerfile
│   └── package.json
├── frontend/           # Static UI assets
│   ├── index.html      # Login Page
│   ├── admin.html      # RBAC Admin Panel
│   ├── dashboard.html  # Standard User View
│   └── style.css       # Glassmorphism UI
├── docker-compose.yml  # Orchestration
└── .gitignore
```

## ⚡ Quick Start

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
* A terminal (Bash, PowerShell, or Zsh).

### 1. Clone the Repository

```bash
git clone https://github.com/28d33/ultimate-login.git
cd ultimate-login
```

### 2. Generate SSL Certificates

Since this project enforces HTTPS, you must generate a local key pair.

```bash
mkdir -p backend/certs
cd backend/certs

# Generate a self-signed cert valid for localhost
openssl req -x509 -new -nodes \
  -keyout server.key \
  -out server.cert \
  -sha256 -days 365 \
  -subj "/C=US/ST=State/L=City/O=LocalSecurity/OU=Dev/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

cd ../..
```

### 3. Build & Run

```bash
docker-compose up --build
```

*Wait until you see `Secure Server running on https://localhost:3001` in the terminal.*

### 4. Access the App

Open your browser to:
**[https://localhost:3001](https://localhost:3001)**

> **Note:** Your browser will warn you "Your connection is not private". This is normal because we signed the certificate ourselves. Click **Advanced -> Proceed to localhost**.

## 🧪 How to Test

### 1. Register an Admin

* Go to `Register`.
* Create a user named **`admin`** (This triggers the auto-admin role logic in the backend).
* Login. You will be redirected to the **Admin Panel** where you can manage other users.

### 2. Test Rate Limiting

* Try to login with wrong credentials **5+ times**.
* Result: `429 Too Many Requests`.

### 3. Test Security Headers

* Inspect the page (F12) -> Network Tab.
* You will see `Content-Security-Policy`, `X-Frame-Options: DENY`, and strictly scoped Cookies.

## 🛡️ Security Architecture

| Vector | Defense Mechanism |
| :--- | :--- |
| **MITM Attacks** | End-to-End HTTPS (TLS) enforced via Helmet. |
| **XSS (Scripting)** | Strict `Content-Security-Policy` & `HttpOnly` Cookies. |
| **SQL/NoSQL Injection** | Input Validation & ORM-like parameter binding. |
| **CSRF** | Double-submit cookie pattern with `csurf` tokens. |
| **Brute Force** | IP & Username-based exponential backoff/lockout. |

## ⚖️ Disclaimer

This project is for **educational purposes only**. The `JWT_SECRET` is hardcoded in the docker-compose file for demonstration. In a production environment, use environment variables and a real Certificate Authority.

---

# TASK 3: Create an Application on EC2 Instance


---

## Overview of Amazon EC2

Amazon EC2 (Elastic Compute Cloud) provides scalable virtual servers in the cloud. It allows users to run applications with full control over the operating system, networking, and storage. EC2 supports a wide range of use cases, including web applications, APIs, and backend services.

---

## Steps Performed

### 1. Launching an EC2 Instance

- Logged in to the AWS Management Console  
- Navigated to **EC2 → Instances**  
- Launched a new instance with the following configuration:
  - **Instance Type:** t2.micro  
  - **AMI:** Amazon Linux  
  - **Key Pair:** Configured for secure SSH access  
  - **Network:** Default VPC  

The instance was successfully launched and reached the **Running** state.

---

### 2. Connecting to the EC2 Instance

- Connected to the EC2 instance using SSH  
- Verified terminal access to the instance  

This allowed full control of the server through the command line.

---

### 3. Installing Required Software

- Updated system packages  
- Installed Python and required dependencies  
- Installed Flask to create a dynamic web application  

This prepared the EC2 instance to host a web-based application.

---

### 4. Creating a Dynamic Application

A simple dynamic web application was created using Python and Flask.  
The application responds to HTTP requests, confirming that it is running on an EC2 instance.

Key characteristics:
- Runs on port **80**
- Binds to `0.0.0.0` for public accessibility
- Handles dynamic HTTP requests

---

### 5. Running the Application in the Background

The application was started in the background using the `nohup` command:

```bash
nohup python3 app.py > app.log 2>&1 &
```

This ensured the application continued running even after closing the terminal session.

---

### 6. Configuring Security (Firewall)

- Identified the Security Group attached to the EC2 instance  
- Opened **port 80** for inbound HTTP traffic using AWS CLI  
- Allowed access from `0.0.0.0/0`  

This enabled external access to the application via the public IP.

---

### 7. Verifying the Application

- Verified locally using:
```bash
curl http://localhost
```

- Verified externally using:
```bash
curl http://<EC2-Public-IP>
```

The application responded successfully in both cases.

---

## Result

The dynamic application was successfully deployed and executed on an Amazon EC2 instance. The instance was configured securely, and the application was accessible over the internet.

---

## Conclusion

This task demonstrated how Amazon EC2 can be used to build and run virtually any dynamic application. By launching and configuring an EC2 instance, managing security settings, and deploying an application, a complete cloud-based deployment was achieved.

---

# TASK 4: AWS CloudFront – Serve Content from Multiple S3 Buckets

---

## Overview of Amazon CloudFront

Amazon CloudFront is a global content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to users worldwide with low latency and high transfer speeds. CloudFront works by caching content at edge locations close to users, reducing load on the origin server.

---

## Overview of Amazon S3

Amazon Simple Storage Service (Amazon S3) is a scalable object storage service designed for high availability, durability, and security. It is commonly used to store static assets such as images, videos, HTML files, and application data.

---

## Architecture Overview

- Multiple Amazon S3 buckets act as content origins
- Amazon CloudFront distribution is created
- CloudFront edge locations cache and serve content globally
- End users access content via the CloudFront distribution URL

This architecture improves performance, scalability, and reliability.

---

## Steps Performed

### 1. Creating Amazon S3 Buckets

- Created multiple S3 buckets to store web content
- Uploaded sample static and dynamic content files
- Configured appropriate bucket permissions and policies

---

### 2. Configuring S3 for CloudFront Access

- Disabled public access where applicable
- Used CloudFront Origin Access Control (OAC) or Origin Access Identity (OAI)
- Ensured secure access between CloudFront and S3

---

### 3. Creating a CloudFront Distribution

- Navigated to **CloudFront → Create Distribution**
- Selected Amazon S3 buckets as origins
- Configured default cache behavior
- Enabled HTTP and HTTPS access
- Selected global edge locations

---

### 4. Enabling Dynamic Content Delivery

- Configured cache behaviors for dynamic content
- Forwarded query strings and headers where required
- Set appropriate TTL (Time To Live) values

This ensured dynamic content is served correctly while maintaining performance.

---

### 5. Testing the CloudFront Distribution

- Accessed content using the CloudFront distribution domain name
- Verified content delivery from different S3 buckets
- Observed reduced latency and faster response times

---

## Result

The CloudFront distribution was successfully configured to serve content from multiple Amazon S3 buckets. Content was delivered securely and efficiently to users through global edge locations.

---


## Conclusion

This task demonstrated how Amazon CloudFront can be used in conjunction with Amazon S3 to deliver content efficiently across the globe. By setting up a dynamic content distribution, CloudFront enhanced performance, security, and scalability while serving content from multiple S3 buckets.

---


# TASK: Penetration Testing Report with Kali

---

##  Introduction

Kali Linux is a Debian-based Linux distribution designed for penetration testing, ethical hacking, and digital forensics. 
This report documents the complete process of setting up a penetration testing lab using Oracle VirtualBox, installing Kali Linux, 
and performing a **Web Application Penetration Test** against a deliberately vulnerable web application.

---

##  Objective

The objectives  were:

- To understand virtualization using Oracle VirtualBox  
- To install and configure Kali Linux  
- To gain hands-on experience with web application penetration testing  
- To identify security vulnerabilities in a web application  
- To document findings with proof of concept and remediation strategies  

---

##  Scope of Assessment

### Application Details

| Parameter | Value |
|---------|------|
| Application Name | Home of Acunetix Art Web Application |
| URL | http://testphp.vulnweb.com |
| Starting Vector | External |
| Target Criticality | Critical |
| Assessment Nature | Cautious & Calculated |
| Assessment Conspicuity | Clear |
| Proof of Concept | Attached Wherever Applicable |

---

##  Virtualization Overview

Virtualization enables multiple operating systems to run on a single physical host. Oracle VirtualBox was used to safely deploy Kali Linux without impacting the host operating system.

Benefits include:
- Isolated testing environment  
- Snapshot and rollback capability  
- Safe exploitation testing  

---

##  Oracle VirtualBox Installation

###  Downloading VirtualBox

1. Visit https://www.virtualbox.org  
2. Download VirtualBox for your host OS  
3. Download the VirtualBox Extension Pack  

###  Installing VirtualBox

1. Run the installer  
2. Accept license agreement  
3. Allow network drivers  
4. Complete installation  

---

##  Kali Linux Installation

###  Download Kali Linux ISO

- URL: https://www.kali.org  
- Version: Installer (64-bit)

###  Create Kali VM

- Type: Linux  
- Version: Debian (64-bit)  
- RAM: 4–8 GB  
- CPU: 2–4 cores  
- Storage: 20–40 GB  

###  Install Kali Linux

- Select **Graphical Install**
- Configure language, region, keyboard
- Create user credentials
- Complete installation and reboot

---

##  Web Penetration Testing Methodology

The assessment followed a **Black Box Web Application Security Testing** approach:

1. Reconnaissance  
2. Input Validation Testing  
3. Injection Testing  
4. Authentication Testing  
5. Client-Side Testing  
6. Risk Analysis  
7. Reporting  

---

#  Web Application Penetration Testing Report

## Summary

A total of **6 vulnerabilities** were identified during the assessment.

| Severity | Count |
|-------|------|
| High | 3 |
| Medium | 1 |
| Low | 2 |

---

## Vulnerability : SQL Injection

 **CWE ID:** CWE-89  
**Risk Rating:** High  
**Tools Used:** Browser, SQLmap  

### Description
SQL Injection was identified in a GET parameter allowing attackers to extract database information.

### Vulnerable URL
```
http://testphp.vulnweb.com/artists.php?artist=1
```

### Impact
Attackers can retrieve sensitive user information including credentials and personal data.

### Recommendation
- Use prepared statements
- Input validation
- Least privilege
- Deploy WAF

📸 **Proof of Concept**
```
[Insert SQL Injection screenshots here]
```

---

## Vulnerability : Reflected Cross-Site Scripting (XSS)

 **CWE ID:** CWE-79  
**Risk Rating:** Medium  

### Description
JavaScript input was reflected and executed in the browser.

### Impact
Session hijacking, credential theft

### Recommendation
- Input filtering
- Output encoding
- Content Security Policy

📸 **Proof of Concept**
```
[Insert Reflected XSS screenshots here]
```

---

## Vulnerability : Stored XSS

 **CWE ID:** CWE-79 
**Risk Rating:** High  

### Description
Malicious JavaScript input was stored in the application profile section.

### Impact
Persistent client-side attacks affecting all users.

📸 **Proof of Concept**
```
[Insert Stored XSS screenshots here]
```

---

## Vulnerability : Broken Authentication

 **CWE ID:** CWE-287  
**Risk Rating:** High  

### Description
Authentication bypass using SQL logic in login fields.

📸 **Proof of Concept**
```
[Insert Authentication Bypass screenshots here]
```

---

## Vulnerability : HTML Injection

 **CWE ID:** CWE-80  
**Risk Rating:** Low  

📸 **Proof of Concept**
```
[Insert HTML Injection screenshots here]
```

---

## Vulnerability : Clickjacking

 **CWE ID:** CWE-1021 
**Risk Rating:** Low  

📸 **Proof of Concept**
```
[Insert Clickjacking screenshots here]
```

---

##  Risk Classification

| Level | Description |
|----|------------|
| Low | Minimal risk |
| Medium | Exploitable with effort |
| High | Easily exploitable |
| Critical | Severe impact |

---

##  Conclusion

This assessment demonstrated the complete lifecycle of setting up a penetration testing environment using Kali Linux and Oracle VirtualBox, followed by a detailed web application security assessment. Multiple high-risk vulnerabilities were identified, highlighting the importance of secure coding practices and regular security testing.

---



# OSI Model and Cloud Computing

## 1. Introduction

The Open Systems Interconnection (OSI) model is a conceptual framework used to understand how data is transmitted across a network. It divides the communication process into seven distinct layers, each responsible for a specific networking function. The OSI model is widely used in networking and cloud computing to design, implement, and troubleshoot network architectures.

In this task, a simple visual representation of the OSI model was created using a cloud-based diagramming tool such as Draw.io. This report explains the OSI architecture, associated protocols, switching, routing, handshakes, and IP addressing, and describes how each OSI layer relates to cloud computing.

---

## 2. Visual Representation of the OSI Model

The OSI model consists of seven layers arranged from top to bottom. The diagram created in Draw.io represents these layers in a stacked format:

```
Layer 7 – Application
Layer 6 – Presentation
Layer 5 – Session
Layer 4 – Transport
Layer 3 – Network
Layer 2 – Data Link
Layer 1 – Physical
```

This layered structure helps in understanding how data flows from user applications down to the physical network infrastructure used in cloud environments.

---

## 3. OSI Architecture and Layer-wise Explanation

### 3.1 Application Layer (Layer 7)

The Application layer provides network services directly to end users and applications. It enables user interaction with network-based services.

**Common Protocols:**  
HTTP, HTTPS, FTP, SMTP, DNS

**Relation to Cloud Computing:**  
Cloud services such as web applications, email platforms, and cloud storage systems operate at this layer. When users access cloud resources through a browser or application, communication begins at the Application layer.

---

### 3.2 Presentation Layer (Layer 6)

The Presentation layer is responsible for data formatting, encryption, decryption, and compression to ensure compatibility between systems.

**Technologies Used:**  
SSL/TLS, data encoding standards

**Relation to Cloud Computing:**  
Cloud platforms rely on this layer to secure data using encryption, especially during HTTPS communication, ensuring confidentiality and data integrity.

---

### 3.3 Session Layer (Layer 5)

The Session layer manages sessions between communicating devices. It establishes, maintains, and terminates communication sessions.

**Functions:**  
Session establishment, authentication, session termination

**Relation to Cloud Computing:**  
User login sessions in cloud dashboards and cloud-based applications are handled at this layer, allowing persistent communication during user interaction.

---

### 3.4 Transport Layer (Layer 4)

The Transport layer ensures reliable or fast delivery of data between systems. It controls error handling, flow control, and data segmentation.

**Protocols:**  
TCP (reliable), UDP (fast but unreliable)

**Handshakes:**  
TCP uses a three-way handshake (SYN, SYN-ACK, ACK) to establish reliable connections.

**Relation to Cloud Computing:**  
Cloud services use TCP for reliable data transfer such as file uploads and database access, while UDP is commonly used for streaming and real-time applications.

---

### 3.5 Network Layer (Layer 3)

The Network layer is responsible for routing data packets and logical addressing.

**Protocols:**  
IP (IPv4, IPv6), ICMP

**Routing and IP Addressing:**  
Routers determine the best path for data transmission using IP addresses.

**Relation to Cloud Computing:**  
Cloud providers use virtual networks, subnets, and routing tables to manage traffic between virtual machines and external networks.

---

### 3.6 Data Link Layer (Layer 2)

The Data Link layer provides node-to-node data transfer and handles physical addressing.

**Devices:**  
Switches, Network Interface Cards (NICs)

**Protocols:**  
Ethernet, ARP

**Switching:**  
Switches forward data frames using MAC addresses.

**Relation to Cloud Computing:**  
Cloud data centers use virtual switches to enable efficient communication between virtual machines within the same network.

---

### 3.7 Physical Layer (Layer 1)

The Physical layer transmits raw bits over physical media such as cables or wireless signals.

**Components:**  
Cables, fiber optics, network hardware

**Relation to Cloud Computing:**  
Cloud infrastructure depends on physical data centers, servers, and high-speed fiber-optic connections.

---

## 4. Switching, Routing, Handshakes, and IP Addressing

- **Switching** operates at the Data Link layer (Layer 2) using MAC addresses.
- **Routing** operates at the Network layer (Layer 3) using IP addresses.
- **IP Addressing** enables logical identification of devices in cloud networks.
- **Handshakes**, such as the TCP three-way handshake, occur at the Transport layer (Layer 4).

These mechanisms ensure reliable and efficient communication in cloud computing environments.

---

## 5. Importance of the OSI Model in Cloud Computing

The OSI model helps cloud engineers and network administrators to:
- Design scalable and secure cloud networks
- Troubleshoot connectivity and performance issues
- Implement layered security mechanisms
- Understand data flow across cloud services

---

## 6. Conclusion

The OSI model provides a structured approach to understanding network communication. In cloud computing, each OSI layer plays an important role in delivering secure, reliable, and scalable services. By studying the OSI architecture along with protocols, switching, routing, handshakes, and IP addressing, a deeper understanding of modern cloud-based networking systems is achieved.

---

# Types of Cloud Computing

## Introduction
Cloud computing refers to the delivery of computing services such as servers, storage, databases, networking, software, analytics, artificial intelligence, and intelligence over the internet (the cloud). It enables users to access IT resources on demand without the need for direct active management of physical infrastructure. Cloud computing supports modern technologies such as big data, Internet of Things (IoT), artificial intelligence (AI), machine learning (ML), and DevOps.

Organizations adopt cloud computing to achieve faster innovation, flexible resources, and economies of scale. It is widely used in education, healthcare, banking, e-commerce, entertainment, and government sectors.

---

## 1. Cloud Computing Deployment Models
Deployment models define **where** the cloud infrastructure is located and **who** has access to it.

### 1.1 Public Cloud
The public cloud is owned and operated by third-party cloud service providers who deliver computing resources such as servers, storage, and applications over the internet. These resources are shared among multiple customers using a multi-tenant model.

**Key Characteristics:**
- Owned and managed by cloud service providers
- Accessible via the public internet
- Highly scalable and elastic
- Multi-tenant architecture

**Advantages:**
- Low upfront investment
- Pay-as-you-go pricing model
- High availability and reliability
- Ideal for startups and small businesses

**Disadvantages:**
- Limited customization
- Potential security and compliance concerns
- Internet dependency

**Use Cases:**
- Web hosting
- Application development and testing
- Data analytics

**Examples:** Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP)

---

### 1.2 Private Cloud
A private cloud is a cloud infrastructure dedicated exclusively to a single organization. It may be hosted on the organization’s premises or managed by a third-party provider. It offers greater control and security compared to public cloud models.

**Key Characteristics:**
- Single-tenant environment
- Dedicated hardware resources
- High level of customization

**Advantages:**
- Strong data security and privacy
- Better compliance with regulations
- Greater control over performance

**Disadvantages:**
- Higher capital and operational costs
- Requires skilled IT staff
- Limited scalability compared to public cloud

**Use Cases:**
- Financial institutions
- Healthcare systems
- Government organizations

**Examples:** VMware Private Cloud, OpenStack, IBM Cloud Private

---

### 1.3 Hybrid Cloud
The hybrid cloud combines public and private clouds, allowing data and applications to be shared between them.

**Key Characteristics:**
- Mix of public and private environments
- Data portability between clouds

**Advantages:**
- Flexibility and scalability
- Cost optimization
- Improved disaster recovery

**Disadvantages:**
- Complex management
- Integration challenges

**Examples:** AWS Outposts, Azure Hybrid Cloud

---

### 1.4 Community Cloud
A community cloud is shared by multiple organizations with common goals, policies, or compliance requirements.

**Key Characteristics:**
- Shared infrastructure among similar organizations
- Managed internally or by a third party

**Advantages:**
- Cost shared among members
- Better compliance
- Collaboration-friendly

**Disadvantages:**
- Limited scalability
- Governance complexity

**Examples:** Government or healthcare community clouds

---

## 2. Cloud Computing Service Models
Service models define **what level of service** is provided to the user.

### 2.1 Infrastructure as a Service (IaaS)
Infrastructure as a Service provides virtualized computing resources over the internet. It allows organizations to rent IT infrastructure instead of purchasing physical hardware.

**User Manages:** Operating systems, middleware, runtime, applications, and data

**Provider Manages:** Physical servers, storage, networking, and virtualization

**Advantages:**
- High flexibility and scalability
- Cost-effective for variable workloads
- Suitable for disaster recovery and backup

**Disadvantages:**
- Requires technical expertise
- Security responsibility lies with the user

**Use Cases:**
- Website hosting
- Big data analysis
- Test and development environments

**Examples:** AWS EC2, Google Compute Engine, Azure Virtual Machines

---

### 2.2 Platform as a Service (PaaS)
PaaS provides a platform that allows developers to build, test, and deploy applications without managing infrastructure.

**User Manages:** Applications and data

**Provider Manages:** OS, runtime, middleware, infrastructure

**Advantages:**
- Faster development
- Reduced complexity

**Examples:** Google App Engine, Azure App Services, Heroku

---

### 2.3 Software as a Service (SaaS)
SaaS delivers fully functional software applications over the internet on a subscription basis.

**User Manages:** Only application usage

**Provider Manages:** Everything else

**Advantages:**
- Easy to use
- No installation required
- Automatic updates

**Examples:** Gmail, Microsoft 365, Salesforce

---

## 3. Additional Cloud Service Models

### 3.1 Function as a Service (FaaS)
FaaS allows users to execute code in response to events without managing servers.

**Advantages:**
- Serverless architecture
- Pay per execution

**Examples:** AWS Lambda, Azure Functions

---

### 3.2 Storage as a Service (STaaS)
Provides cloud-based storage solutions for data backup and access.

**Examples:** Google Drive, Amazon S3, Dropbox

---

## 4. Comparison Between Cloud Models

| Model | Ownership | Scalability | Cost | Security |
|------|----------|-------------|------|----------|
| Public Cloud | Provider | Very High | Low | Moderate |
| Private Cloud | Organization | Limited | High | High |
| Hybrid Cloud | Shared | High | Medium | High |
| Community Cloud | Shared Community | Medium | Medium | Medium |

---

## 5. Benefits of Cloud Computing
- Reduced IT costs
- On-demand self-service
- Global accessibility
- Automatic software updates
- Business continuity and disaster recovery

---

## 6. Challenges of Cloud Computing
- Data security and privacy risks
- Downtime and internet dependency
- Vendor lock-in
- Compliance issues

---

## Conclusion
Cloud computing provides a flexible and efficient approach to managing IT resources. With various deployment and service models available, organizations can choose solutions tailored to their operational needs, security requirements, and budget. As technology evolves, cloud computing continues to play a critical role in digital transformation and innovation.



# Task: Secure End-to-End Encrypted Chat Application


**Technology Stack:** Python 3, PyCryptodome, Socket API  

---

## 1. Executive Summary

This project implements a secure, terminal-based Peer-to-Peer (P2P) chat application. It addresses the need for private communication by ensuring that no message travels over the network in plaintext. The application utilizes a **Hybrid Encryption** scheme, combining the convenience of asymmetric encryption (RSA) for the initial handshake with the speed of symmetric encryption (AES) for real-time messaging.

---

## 2. System Architecture

The application follows a client-server architecture where two nodes (Host and Client) establish a direct TCP connection. The security protocol mimics standard TLS/SSL handshakes but is implemented manually for educational transparency.

### 2.1 The Encryption Protocol (Hybrid Approach)

1. **Identity Generation:**  
   On startup, both users generate a temporary 2048-bit RSA key pair.

2. **Handshake:**  
   - Users exchange **RSA Public Keys**  
   - The Host generates a cryptographically secure random **AES-256 Session Key**  
   - The Host encrypts this session key using the Client's public RSA key and sends it

3. **Secure Session:**  
   Both parties now possess the identical AES Session Key. All subsequent chat messages are encrypted using **AES-256-CBC** mode with PKCS7 padding.

---

### 2.2 Workflow Diagram

> **[INSERT IMAGE HERE: System Flowchart / Mermaid Diagram]**  
> *Figure 1: Application Logic Flow*

---

## 3. Technical Implementation

### 3.1 Dependencies

- **Language:** Python 3.13+  
- **Library:** pycryptodome (v3.23.0)  
- **Network:** socket, threading  

---

### 3.2 Key Modules

#### CryptoHandler Class

- `encrypt_session_key()` – RSA OAEP  
- `encrypt_message()` – AES with random IV  
- `decrypt_message()` – AES decryption  

#### ChatClient Class

- Multithreading for async receive  
- `SO_REUSEADDR` to prevent port reuse errors  

---

## 4. Usage & Execution

### 4.1 Prerequisites

```bash
pip install pycryptodome
```

---

### 4.2 Running the Application

#### Step 1: Start the Host

> **[INSERT IMAGE HERE: Host Terminal]**  
> *Figure 2: Host Server Startup*

#### Step 2: Connect the Client

> **[INSERT IMAGE HERE: Client Handshake]**  
> *Figure 3: Successful Handshake*

#### Step 3: Secure Chat

> **[INSERT IMAGE HERE: Encrypted Chat]**  
> *Figure 4: Encrypted Chat Session*

---

## 5. Challenges & Solutions

### 5.1 Zombie Port Issue

```python
self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

---

### 5.2 Message Fragmentation

A fixed-size length header is used to handle TCP packet fragmentation.

---


## 7. Conclusion

This project demonstrates secure communication using hybrid encryption.

---


