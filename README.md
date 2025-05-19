# FastAPI CRUD Starter

A modern, production-ready FastAPI starter template with CRUD operations, SQLAlchemy, and PostgreSQL. This template provides a solid foundation for building RESTful APIs with best practices and modern Python features.

## Features

- 🚀 FastAPI framework with async support
- 📦 SQLAlchemy ORM with PostgreSQL
- 🔄 Alembic for database migrations
- 🎯 Pydantic v2 for data validation
- 📝 OpenAPI (Swagger) documentation
- 🛠️ Poetry for dependency management
- 🐳 Docker support
- 🔍 Type hints and validation
- 🎨 Black and isort for code formatting

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.12 or higher
- PostgreSQL (version 12 or higher)
- Poetry (Python package manager)

### Installing Prerequisites

1. **Python 3.12+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **PostgreSQL**
   - Download from [postgresql.org](https://www.postgresql.org/download/)
   - Create a database: `createdb fastapi_crud`
   - Verify installation: `psql --version`

3. **Poetry**
   - Install using the official installer:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
   - Verify installation: `poetry --version`

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/fastapi-crud-starter.git
   cd fastapi-crud-starter
   ```

2. **Set up the virtual environment and install dependencies:**
   ```bash
   poetry install
   ```

3. **Configure environment variables:**
   ```bash
   cp .env_example .env
   ```
   Edit `.env` with your database settings:
   ```
   DB_URL=postgresql://postgres:postgres@localhost:5432/fastapi_crud
   ```
   Note: Replace `postgres` with your PostgreSQL username and password if different.

4. **Initialize the database:**
   ```bash
   # Create the database tables
   alembic upgrade head
   ```

5. **Start the development server:**
   ```bash
   make run-dev
   ```
   The API will be available at `http://localhost:8000`

## Exploring the API

Once the server is running, you can explore the API using:

- **Swagger UI**: Visit `http://localhost:8000/docs` for an interactive API documentation
- **ReDoc**: Visit `http://localhost:8000/redoc` for a more detailed API documentation

### Example API Usage

1. **Create a new task:**
   ```bash
   curl -X POST "http://localhost:8000/api/v1/tasks/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn FastAPI", "description": "Build a REST API with FastAPI"}'
   ```

2. **List all tasks:**
   ```bash
   curl "http://localhost:8000/api/v1/tasks/"
   ```

## Project Structure

```
fastapi-crud-starter/
├── alembic/              # Database migrations
├── app/
│   ├── api/             # API endpoints
│   │   └── v1/
│   │       └── endpoints/
│   ├── core/            # Core functionality
│   ├── crud/            # CRUD operations
│   ├── db/              # Database configuration
│   ├── models/          # SQLAlchemy models
│   └── schemas/         # Pydantic schemas
├── tests/               # Test files
├── .env                 # Environment variables
├── .env_example         # Example environment variables
├── pyproject.toml       # Project dependencies
├── Makefile            # Development commands
└── README.md           # Project documentation
```

## Development Workflow

### Common Tasks

1. **Running the development server:**
   ```bash
   make run-dev
   ```

2. **Formatting code:**
   ```bash
   make format
   ```

### Running Tests

You can run all tests using:
```bash
poetry run pytest
```

### Database Management

1. **Create a new migration:**
   ```bash
   alembic revision --autogenerate -m "description of changes"
   ```

2. **Apply migrations:**
   ```bash
   alembic upgrade head
   ```

3. **Rollback last migration:**
   ```bash
   alembic downgrade -1
   ```

## Docker Support

### Using Docker

1. **Build the image:**
   ```bash
   docker build -t fastapi-crud-starter .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 fastapi-crud-starter
   ```

### Docker Compose (Recommended)

1. **Start the services:**
   ```bash
   docker-compose up -d
   ```

2. **Stop the services:**
   ```bash
   docker-compose down
   ```