# API Versioning Service

Flask REST API demonstrating `/api/v1` and `/api/v2` contracts without breaking existing clients.

## Features
- Versioned REST endpoints
- Backward-compatible v1 response
- Enhanced v2 response
- Shared data layer
- Error handling
- Health endpoint
- Pytest tests

## Run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Endpoints:
- `GET /health`
- `GET /api/v1/products`
- `GET /api/v2/products`

Tests:

```bash
pytest
```
