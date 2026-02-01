# Patient Encounter Management System

A production-ready backend API for managing patients, doctors, and medical appointments, built with **FastAPI**, **SQLAlchemy** and **pytest**, with full **CI + coverage enforcement** using **GitHub Actions**.

---

## Features

- Patient management (create, list)
- Doctor management (create, list)
- Appointment scheduling with:
  - Foreign key validation
  - Overlap detection
  - Timezone-safe datetime handling
- RESTful API using FastAPI
- SQLAlchemy ORM (2.0 style)
- Pytest test suite with coverage
- GitHub Actions CI pipeline
- Clean `src/` project layout

---

## Tech Stack

- **Backend**: FastAPI  
- **ORM**: SQLAlchemy  
- **Database**: MySQL (production), SQLite (testing)  
- **Testing**: Pytest, pytest-cov  
- **CI/CD**: GitHub Actions  
- **Language**: Python 3.10+

---

## Project Structure

```bash
patient-encounter-system/
├── src/
│ └── patient_encounter_system/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── services.py
│
├── tests/
│ ├── conftest.py
│ ├── test_patients.py
│ ├── test_doctors.py
│ └── test_appointments.py
│
├── .github/workflows
├── pyproject.toml
└── README.md
```

**Set up Instructions**

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd patient-encounter-system
    ```
      
2. Install poetry:

 ```bash
  pip install poetry
```

3. Install dependencies:

```bash
  poetry install 
  poetry shell
 ```

4. Run the Fastapi server

  ```bash
uvicorn patient_encounter_system.main:app --reload
```
The server will run at http://127.0.0.1:8000/docs
