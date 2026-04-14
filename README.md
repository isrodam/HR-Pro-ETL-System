# HR-Pro ETL System 🚀

## 📝 Descripción del Proyecto
Este proyecto consiste en el diseño e implementación de un sistema **ETL (Extract, Transform, Load)** robusto para la empresa líder en recursos humanos **"HR Pro"**. El objetivo es gestionar grandes volúmenes de datos generados en tiempo real (eventos de Kafka) sobre empleados, nóminas y selección, asegurando su persistencia y calidad.

## 🏗️ Arquitectura del Sistema
El sistema sigue un flujo de datos profesional dividido en tres capas:
1.  **Ingesta:** Consumo de eventos en tiempo real desde **Apache Kafka**.
2.  **Almacenamiento NoSQL (Bronze):** Persistencia de mensajes en bruto en **MongoDB**.
3.  **Procesamiento y Carga (Gold):** Limpieza y normalización de datos con **Pandas** y carga final en **MySQL**.



## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.12+
* **Gestor de Dependencias:** [uv](https://github.com/astral-sh/uv)
* **Mensajería:** Apache Kafka
* **Bases de Datos:** MongoDB (NoSQL) y MySQL (Relacional)
* **Infraestructura:** Docker & Docker Compose
* **Calidad de Código:** Ruff (Linter & Formatter)

## 📂 Estructura del Proyecto
```text
├── .github/workflows/  # Automatización CI/CD (Ruff checks)
├── infra/              # Configuración de Docker (Kafka, DBs)
├── src/                # Código fuente
│   ├── consumer/       # Lector de Kafka
│   ├── processing/     # Transformación con Pandas
│   └── database/       # Conectores de base de datos
├── tests/              # Pruebas unitarias
├── pyproject.toml      # Configuración de uv
└── README.md