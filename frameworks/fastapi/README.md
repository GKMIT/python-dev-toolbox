# FastAPI Boilerplate

This is a production-ready FastAPI boilerplate with a structured project setup that follows best practices. It provides a solid foundation for building robust APIs quickly.

## Features

- **Modern Python**: Built with Python 3.11+ utilizing modern Python features
- **Fast API Framework**: Utilizes FastAPI for high performance and standards-based API development
- **Project Structure**: Organized project structure for scalability 
- **Configuration Management**: Environment-based configuration with Pydantic settings
- **Docker Ready**: Includes Dockerfile for containerization
- **Dependency Management**: Using `uv` for fast, reliable Python package management
- **CORS Middleware**: Pre-configured Cross-Origin Resource Sharing (CORS)

## Project Structure

```
├── app/                    # Application package
│   ├── main.py             # Application entry point
│   ├── core/               # Core modules
│   │   └── config.py       # Configuration management
│   ├── database/           # Database connections and models
│   │   └── connection.py   # Database connection management
│   ├── models/             # SQLAlchemy models
│   │   └── base.py         # Base model class
│   ├── repository/         # Data access layer
│   ├── routers/            # API routes/endpoints
│   ├── schemas/            # Pydantic models/schemas
│   ├── services/           # Business logic
│   └── utils/              # Utility functions
├── Dockerfile              # Docker configuration
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # Project documentation
└── uv.lock                 # Lock file for dependencies
```

## Setup and Installation

### Prerequisites

- Python 3.11 or higher
- `uv` package manager (optional, but recommended)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-boilerplate
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Using pip
   pip install -e .
   
   # Or using uv
   uv sync
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API documentation**
   - Swagger UI: http://localhost:8000/api/v1/docs
   - ReDoc: http://localhost:8000/api/v1/redoc

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t fastapi-boilerplate .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:80 fastapi-boilerplate
   ```

## Configuration

Configuration is managed by the `Settings` class in `app/core/config.py`. You can set environment variables or use a `.env` file in the project root to customize settings.

Key configurations:
- `API_V1_STR`: API version prefix
- `PROJECT_NAME`: Name of the project
- `BACKEND_CORS_ORIGINS`: List of allowed CORS origins
- `ENVIRONMENT`: Runtime environment (`local`, `staging`, `production`)

## Adding New Endpoints

1. Create a new router file in the `app/routers/` directory
2. Define your endpoints using FastAPI's router
3. Import and include your router in `app/main.py`

Example router (`app/routers/example.py`):
```python
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/examples", tags=["examples"])

@router.get("/")
async def get_examples():
    return {"message": "Get all examples"}

@router.get("/{example_id}")
async def get_example(example_id: int):
    return {"message": f"Get example with ID {example_id}"}
```