# FastAPI CRUD Application

A sample FastAPI application with CRUD operations for managing tasks, using PostgreSQL for persistent storage and Redis for caching. The project is managed with `uv` for dependencies and can be run locally or in Docker containers.

## Prerequisites

- Python 3.11
- [uv](https://docs.astral.sh/uv/) (for dependency and environment management)
- Docker and Docker Compose (for containerized deployment)
- curl (for health checks, optional)

## Project Structure

```
fastapi_crud/
├── main.py              # FastAPI application
├── database/
   └── connection.py     # Database setup
├── models/
   └── task.py           # SQLAlchemy models task
├── services/
   └── redis_client.py   # Redis configuration
├── routers/
   └── tasks.py          # endpoints
├── Dockerfile           # Docker build configuration
├── docker-compose.yml   # Docker Compose for FastAPI, PostgreSQL, Redis
├── .dockerignore        # Files to exclude from Docker build
├── pyproject.toml       # Project configuration for uv
├── README.md            # This file
```

## Setup Instructions

### Local Development with uv

1. **Install uv**:
   Follow the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) to install `uv`.
   
   or

   Install the `uv` tool using the following command:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```


2. **Clone the Repository**:
   ```bash
   git clone https://github.com/GKMIT/python-dev-toolbox
   cd python-dev-toolbox/frameworks/fastapi_crud
   ```

3. **Install Dependencies**:
   ```bash
   uv sync
   ```
   This installs all dependencies listed in `pyproject.toml`, including dev dependencies like `pytest`.

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root:
   ```bash
   echo "DATABASE_URL=postgresql://user:password@localhost:5432/mydb" > .env
   echo "REDIS_URL=redis://localhost:6379/0" >> .env
   ```
   Update the values if your PostgreSQL or Redis setup differs.

5. **Run PostgreSQL and Redis Locally** (if not using Docker):
   Ensure PostgreSQL and Redis are running locally. For example:
   - PostgreSQL: Install and start with `sudo service postgresql start`.
   - Redis: Install and start with `redis-server`.

6. **Run the Application**:
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
   The `--reload` flag enables auto-reload for development.

7. **Access the API**:
   Open `http://localhost:8000/docs` in a browser to view the Swagger UI and test endpoints.

### Running with Docker

1. **Build and Start Containers**:
   ```bash
   docker compose up -d  
   ```
   This builds the FastAPI image and starts FastAPI, PostgreSQL, and Redis services.

2. **Access the API**:
   Open `http://localhost:8000/docs` to interact with the API.

3. **Stop Containers**:
   ```bash
   docker-compose down
   ```

### API Endpoints

- **POST /tasks/**: Create a new task (e.g., `{"title": "Task 1", "description": "Do something", "completed": false}`).
- **GET /tasks/**: List all tasks (cached in Redis for 60 seconds).
- **GET /tasks/{id}**: Retrieve a task by ID.
- **PUT /tasks/{id}**: Update a task by ID.
- **DELETE /tasks/{id}**: Delete a task by ID.
- **GET /health**: Check application health.

### Testing

Run tests with `pytest` (included in dev dependencies):
```bash
uv run pytest
```

Note: You'll need to create test files in a `tests/` directory for this to work. Not implemented yet.

### Notes

- The Redis caching in `GET /tasks/` uses simple serialization for demonstration. Use proper serialization (e.g., JSON) in production.
- Update PostgreSQL credentials in `docker-compose.yml` or `.env` for security.
- The `/health` endpoint is basic. Enhance it to check database and Redis connectivity if needed.

## Troubleshooting

- **Database Connection Issues**: Ensure PostgreSQL is running and the `DATABASE_URL` is correct.
- **Redis Connection Issues**: Verify Redis is running and the `REDIS_URL` is correct.
- **Docker Issues**: Check container logs with `docker-compose logs` if services fail to start.

For further customization or issues, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) or open an issue in the repository.