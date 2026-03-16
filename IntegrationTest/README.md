Below is a **project** that shows how to **set up an integration testing environment and write test cases that validate interaction between system components**.

We will build a **simple microservice system**:

* **Frontend/API Service** → Python Flask
* **Database** → PostgreSQL
* **Integration Tests** → Python + Pytest
* **Environment** → Docker + Docker Compose

This shows how **components interact together**, which is the main goal of **integration testing**.

---

# 1. Project Architecture

```
User Request
     │
     ▼
Flask API (app service)
     │
     ▼
PostgreSQL Database
     │
     ▼
Integration Tests (pytest)
     │
     ▼
Validate API ↔ Database interaction
```

Integration tests verify:

* API can connect to DB
* Data can be stored
* Data can be retrieved
* Services communicate correctly

---

# 2. Project Folder Structure

```
integration-testing-project
│
├── app
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│
├── tests
│   └── test_integration.py
│
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

# 3. Step 1 — Create Flask Sample Application

## `app/app.py`

```python
from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Integration Testing Demo"

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s,%s) RETURNING id",
        (data["name"], data["email"])
    )

    user_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"id": user_id, "name": data["name"], "email": data["email"]})

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT name,email FROM users")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

# 4. Step 2 — Database Connection

## `app/db.py`

```python
import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST","db"),
        database="testdb",
        user="postgres",
        password="postgres"
    )
    return conn
```

---

# 5. Step 3 — Python Dependencies

## `app/requirements.txt`

```
flask
psycopg2-binary
pytest
requests
```

---

# 6. Step 4 — Dockerfile

This builds the application container.

```
FROM python:3.10

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]
```

---

# 7. Step 5 — Docker Compose (Integration Environment)

## `docker-compose.yml`

```
version: '3'

services:

  db:
    image: postgres:14
    environment:
      POSTGRES_DB: testdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"

  app:
    build: .
    depends_on:
      - db
    ports:
      - "5000:5000"
```

This creates the **integration testing environment**.

Components running together:

* Flask app
* PostgreSQL database

---

# 8. Step 6 — Create Integration Tests

Integration tests check **interaction between API and database**.

## `tests/test_integration.py`

```python
import requests

BASE_URL = "http://localhost:5000"

def test_create_user():

    payload = {
        "name": "John",
        "email": "john@test.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "John"
    assert data["email"] == "john@test.com"


def test_get_users():

    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    users = response.json()

    assert isinstance(users, list)
```

---

# 9. Step 7 — Start Environment

Run the environment:

```bash
docker-compose up --build
```

App will run at:

```
http://localhost:5000
```

---

# 10. Step 8 — Run Integration Tests

Open another terminal.

Install dependencies:

```bash
pip install pytest requests
```

Run tests:

```bash
pytest tests/
```

Output example:

```
================== test session starts ==================
collected 2 items

tests/test_integration.py ..                [100%]

================== 2 passed ==================
```

---

# 11. What This Integration Test Validates

| Test          | Validation           |
| ------------- | -------------------- |
| create_user   | API ↔ Database write |
| get_users     | API ↔ Database read  |
| status_code   | Service health       |
| response data | Data integrity       |

---

# 12. Why Integration Testing is Important

It validates **communication between components**, not just single units.

| Test Type        | Example                |
| ---------------- | ---------------------- |
| Unit Test        | Function works         |
| Integration Test | API + DB work together |
| System Test      | Whole application      |
| E2E Test         | User workflow          |

---


You can run tests automatically using:

* **GitHub Actions**
* **Jenkins**
* **GitLab CI**

---



