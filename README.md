# Enterprise Notification System

A scalable backend-based notification platform built using Python and modern backend technologies. This project is designed for enterprise-level communication where notifications can be sent asynchronously through APIs, message queues, and worker services.

---

## Features

* User Notification Management
* REST API using FastAPI
* Asynchronous Task Processing with Celery
* Message Queue Integration using RabbitMQ
* PostgreSQL Database Support
* Docker & Docker Compose Setup
* Scalable Microservice Architecture
* API Documentation with Swagger UI
* Environment Variable Configuration
* Background Worker Processing

---

## Tech Stack

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python         | Backend Development        |
| FastAPI        | REST API Framework         |
| PostgreSQL     | Database                   |
| RabbitMQ       | Message Broker             |
| Celery         | Background Task Queue      |
| Docker         | Containerization           |
| Docker Compose | Multi-container Management |
| SQLAlchemy     | ORM                        |
| Pydantic       | Data Validation            |

---

# Project Structure

```bash
enterprise_notification_system/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   └── main.py
│
├── docker/
├── requirements.txt
├── docker-compose.yml
├── .env
└── README.md
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/enterprise_notification_system.git

cd enterprise_notification_system
```

---

## 2. Create Virtual Environment

### Windows (PowerShell)

```powershell
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory.

Example:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/notification_db
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672//
SECRET_KEY=your_secret_key
```

---

# Run Using Docker

## Start All Services

```powershell
docker compose up --build
```

---

## Stop Containers

```powershell
docker compose down
```

---

# API Documentation

After running the project:

Swagger UI:

```bash
http://localhost:8000/docs
```

ReDoc:

```bash
http://localhost:8000/redoc
```

---

# Sample API Endpoint

## Send Notification

```http
POST /notifications/send
```

### Request Body

```json
{
  "user_id": 1,
  "title": "System Alert",
  "message": "Your report has been generated successfully"
}
```

### Response

```json
{
  "status": "success",
  "message": "Notification queued successfully"
}
```

---

# Celery Worker

Run Celery worker manually:

```bash
celery -A app.workers.celery_worker worker --loglevel=info
```

---

# Database Migration

If using Alembic:

```bash
alembic upgrade head
```

---

# Future Improvements

* Email Notification Support
* SMS Notification Integration
* Push Notification Service
* Notification Analytics Dashboard
* User Authentication & Authorization
* Kafka Integration
* Kubernetes Deployment

---

# Common Docker Commands

## Check Running Containers

```powershell
docker ps
```

## View Logs

```powershell
docker compose logs -f
```

## Rebuild Containers

```powershell
docker compose up --build --force-recreate
```

---

# Troubleshooting

## Docker Desktop Not Starting

* Restart Docker Desktop
* Enable Virtualization in BIOS
* Update WSL2
* Restart System

---

# Author

**Jaydip Badgujar**

