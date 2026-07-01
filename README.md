# AI Backend Production Deployment

## Overview

This project demonstrates how to deploy a production-ready backend application using Docker and AWS EC2.

The application consists of:

* FastAPI
* PostgreSQL
* Redis
* NGINX Reverse Proxy
* Docker Compose
* GitHub Actions CI/CD

The project is designed to simulate a real-world production deployment with containerization, automated deployment, health monitoring, logging, restart policies, and basic server security.

---

# Architecture

```
                Internet
                                    │
                                                 HTTP / HTTPS
                                                                     │
                                                                                     NGINX
                                                                                                         │
                                                                                                                     Reverse Proxy
                                                                                                                                         │
                                                                                                                                                         FastAPI
                                                                                                                                                                        /       \
                                                                                                                                                                              PostgreSQL      Redis
                                                                                                                                                                                                  │
                                                                                                                                                                                                               Docker Compose
                                                                                                                                                                                                                                   │
                                                                                                                                                                                                                                                    AWS EC2

                                                                                                                                                                                                                                                    GitHub
                                                                                                                                                                                                                                                        │
                                                                                                                                                                                                                                                        Git Push
                                                                                                                                                                                                                                                            │
                                                                                                                                                                                                                                                            GitHub Actions
                                                                                                                                                                                                                                                                │
                                                                                                                                                                                                                                                                SSH
                                                                                                                                                                                                                                                                    │
                                                                                                                                                                                                                                                                    AWS EC2
                                                                                                                                                                                                                                                                    ```

                                                                                                                                                                                                                                                                    ---

# Tech Stack

* FastAPI
* PostgreSQL
* Redis
* Docker
* Docker Compose
* NGINX
* GitHub Actions
* AWS EC2
* Ubuntu

---

# Features

* Dockerized FastAPI application
* PostgreSQL database
* Redis cache
* NGINX reverse proxy
* Docker Compose orchestration
* Environment variable configuration
* Health check endpoint
* Automatic container restart policy
* Log rotation using Docker logging
* Database backup script
* GitHub Actions CI/CD deployment
* UFW Firewall
* Fail2Ban protection

---

# Project Structure

```
.
├── app/
│   ├── main.py
│   ├── database.py
│   ├── redis_client.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
├── scripts/
│   └── backup.sh
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Running Locally

Clone the repository:

```bash
git clone <repository-url>
cd ai-backend-deployment
```

Create the environment file:

```bash
cp .env.example .env
```

Start the application:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker compose ps
```

Application:

```
http://localhost
```

Swagger UI:

```
http://localhost/docs
```

Health Endpoint:

```
http://localhost/health
```

---

# Deployment

The application is deployed on an AWS EC2 Ubuntu instance.

Deployment process:

1. Push code to the `main` branch.
2. GitHub Actions workflow starts automatically.
3. GitHub Actions connects to the EC2 instance via SSH.
4. Latest code is pulled from GitHub.
5. Docker Compose rebuilds and restarts the application.
6. Updated application becomes available.

---

# Environment Variables

Example:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=appdb

POSTGRES_HOST=postgres
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379
```

---

# Health Check

Endpoint:

```
GET /health
```

The endpoint verifies:

* PostgreSQL connectivity
* Redis connectivity

---

# Logging Strategy

Docker JSON logging driver is used with log rotation.

Configuration:

* Maximum log size: 10 MB
* Maximum log files: 3

Logs can be viewed using:

```bash
docker compose logs -f
```

---

# Restart Strategy

Containers use Docker restart policies to recover automatically after failures or server reboot.

---

# Backup Strategy

A backup script creates PostgreSQL database dumps.

The script can be executed manually or scheduled using cron jobs for automated daily backups.

---

# Security Measures

* Environment variables for secrets
* NGINX reverse proxy
* UFW Firewall
* Fail2Ban for SSH protection
* Docker bridge networking
* Isolated application containers

---

# SSL

HTTPS is planned using Let's Encrypt (Certbot).

At the time of this deployment, a production domain name is not available. Therefore, an SSL certificate could not be generated.

Once a domain is mapped to the AWS EC2 public IP, SSL can be enabled using:

```bash
sudo certbot --nginx -d your-domain.com
```

This will configure HTTPS and automatic certificate renewal.

---

# CI/CD

GitHub Actions automatically deploys every push to the `main` branch.

Workflow steps:

* Checkout repository
* Connect to AWS EC2 over SSH
* Pull latest code
* Build Docker images
* Restart containers

---

# Future Improvements

* HTTPS with Let's Encrypt
* Cloudflare integration
* Prometheus monitoring
* Grafana dashboards
* Zero-downtime deployments
* Docker image registry
* Kubernetes deployment

---

# Author

Prateek Mall

