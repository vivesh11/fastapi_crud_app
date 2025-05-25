# FastAPI CRUD App

This is a basic FastAPI application implementing simple CRUD operations with CI/CD and code quality enforcement using GitHub Actions and Ruff.

## Features
- **CRUD operations** with in-memory database
- **FastAPI** for API implementation
- **Pytest** for unit testing
- **Ruff** for linting
- **GitHub Actions** for CI/CD pipeline with multiple environment triggers (`dev`, `qa`, `prod`)

## Project Structure
```
fastapi_crud_app/
├── app/
│   ├── main.py        # FastAPI routes
│   ├── crud.py        # Business logic
│   └── models.py      # Pydantic models
├── tests/
│   └── test_crud.py   # Unit tests
├── requirements.txt   # Python dependencies
├── pyproject.toml     # Linter/test config
├── README.md          # Project overview
└── .github/workflows/ci_cd.yml  # CI/CD pipeline
```

## Setup
1. **Clone the repo**
```bash
git clone <your-repo-url>
cd fastapi_crud_app
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
uvicorn app.main:app --reload
```

5. **Run tests**
```bash
pytest
```

6. **Lint code**
```bash
ruff check .
```

## CI/CD Pipeline
Triggered on:
- Push and PR to branches: `dev`, `qa`, `prod`

Steps:
- Checkout code
- Set up Python
- Install dependencies
- Run linter (Ruff)
- Run unit tests (Pytest)
- Simulated deploy step if checks pass

## License
MIT