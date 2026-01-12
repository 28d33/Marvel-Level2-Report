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

**Challenges Overcome:**
- Understood merge conflict markers through practice
- Learned staging area concept via selective commits
- Distinguished revert (safe for shared) vs reset (local only)

**Proficiency Summary:**

| Skill | Level |
|-------|-------|
| Basic Commands | Advanced |
| Branching/Merging | Advanced |
| Remote Operations | Intermediate |
| Error Recovery | Intermediate |

---

**Task Status:** ✅ Completed  
**Next:** Task 2 - Advanced Git Operations

*Report demonstrates practical Git proficiency and AI-assisted learning.*

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



