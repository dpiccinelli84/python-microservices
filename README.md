# Python Microservices Example

This project demonstrates a simple microservices architecture using Python and Flask.

## Architecture

- **user-service**: Manages users.
- **catalog-service**: Manages products.
- **order-service**: Manages orders and communicates with the user-service.

## How to Run

Each service is independent. You need to run each one in a separate terminal.

### Terminal 1: User Service

```bash
cd user-service
pip install -r requirements.txt
python app.py
# Service will run on http://127.0.0.1:5001
```

### Terminal 2: Catalog Service

```bash
cd catalog-service
pip install -r requirements.txt
python app.py
# Service will run on http://127.0.0.1:5002
```

### Terminal 3: Order Service

```bash
cd order-service
pip install -r requirements.txt
python app.py
# Service will run on http://127.0.0.1:5003
```

## How to Test

The `user-service` includes a basic test suite.

To run the tests:

```bash
# Navigate to the user-service directory
cd user-service

# Install dependencies (including pytest)
pip install -r requirements.txt

# Run pytest
pytest
```

## GitHub Actions Workflow

A CI workflow is defined in `.github/workflows/ci.yml`. It automatically runs the tests for the `user-service` on every push to the `main` branch.
