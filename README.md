# HR-Pro ETL System 🚀

## 📝 Project Description
This project involves the design and implementation of a robust **ETL (Extract, Transform, Load)** system for the human resources leader **"HR Pro"**. The goal is to manage large volumes of real-time data (Kafka events) regarding employees, payroll, and recruitment, ensuring data persistence and quality.

## 🏗️ System Architecture
The system follows a professional data flow divided into three layers:
1.  **Ingestion:** Real-time event consumption from **Apache Kafka**.
2.  **NoSQL Storage (Bronze):** Raw message persistence in **MongoDB**.
3.  **Processing & Loading (Gold):** Data cleaning and normalization using **Pandas**, with final loading into **MySQL**.



## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Dependency Manager:** [uv](https://github.com/astral-sh/uv)
* **Messaging:** Apache Kafka
* **Databases:** MongoDB (NoSQL) & MySQL (Relational)
* **Infrastructure:** Docker & Docker Compose
* **Code Quality:** Ruff (Linter & Formatter)

## 📂 Project Structure
```text
├── .github/workflows/  # CI/CD Automation (Ruff checks)
├── infra/              # Docker configuration (Kafka, DBs)
├── src/                # Source code
│   ├── consumer/       # Kafka consumer logic
│   ├── processing/     # Data transformation with Pandas
│   └── database/       # Database connectors
├── tests/              # Unit tests

## 🚀 Quick Start for the Team

    Spin up infrastructure: ```bash
    cd infra && docker-compose up -d


    Create Kafka topic (only required once):
    Bash

    docker exec -it infra-kafka-1 kafka-topics --create --topic hr_pro_data --bootstrap-server localhost:9092

    Run the consumer:
    Bash

    python -m src.consumer.kafka_consumer