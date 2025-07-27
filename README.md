
# 🚀 KPA Backend Assignment – Wheel Specification API

This project implements two backend APIs for submission and retrieval of railway **wheel specification forms** using **FastAPI**, **PostgreSQL**, and **Docker**.

It is developed as part of the **KPA Backend Assignment**, and is designed to work with the provided Flutter frontend and Postman collection.

---

## 🛠️ Tech Stack

- **FastAPI** – Python web framework
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for interacting with PostgreSQL
- **Docker + Docker Compose** – Containerized app and DB
- **Pydantic** – Data validation and serialization
- **Uvicorn** – FastAPI server
- **Postman** – API testing

---

## 📦 APIs Implemented

### ✅ 1. `POST /api/forms/wheel-specifications`

Submit a new wheel specification form.

**Sample Request Body**:
```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelProfile": "29.4 Flange Thickness",
    "intermediateWWP": "20 TO 28",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "wheelDiscWidth": "127 (+4/-0)"
  }
}
```

**Success Response**:
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
```

---

### ✅ 2. `GET /api/forms/wheel-specifications`

Retrieve one or more wheel specification forms using query filters.

**Request Example**:
```
GET /api/forms/wheel-specifications?formNumber=WHEEL-2025-001&submittedBy=user_id_123&submittedDate=2025-07-03
```

**Success Response**:
```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "condemningDia": "825 (800-900)",
        "wheelGauge": "1600 (+2,-1)",
        "variationSameAxle": "0.5",
        "variationSameBogie": "5",
        "variationSameCoach": "13",
        "wheelProfile": "29.4 Flange Thickness",
        "intermediateWWP": "20 TO 28",
        "bearingSeatDiameter": "130.043 TO 130.068",
        "rollerBearingOuterDia": "280 (+0.0/-0.035)",
        "rollerBearingBoreDia": "130 (+0.0/-0.025)",
        "rollerBearingWidth": "93 (+0/-0.250)",
        "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
        "wheelDiscWidth": "127 (+4/-0)"
      }
    }
  ]
}
```

---

## 🧪 Postman Collection

You can test both APIs using Postman.

- File: `wheel_spec_collection.json`
- Includes:
  - Sample POST request with body
  - Sample GET request with query parameters

---

## 🐳 Running the Project with Docker

### 📁 Prerequisites

- Docker and Docker Compose installed
- Ports 8000 (FastAPI) and 5432 (PostgreSQL) should be free

---

### ▶️ Steps to Run Locally

1. **Clone this repository**
```bash
git clone https://github.com/blacxtar/kpa-assignment.git
cd kpa-assignment
```

2. **Create `.env` file**
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=kpa_assignment
DB_HOST=db
DB_PORT=5432
```

3. **Run the app using Docker**
```bash
docker-compose up --build
```

4. Open your browser to:
```
http://localhost:8000/docs
```

This opens the FastAPI Swagger docs to test endpoints interactively.

---

## 📂 Project Structure

```
kpa-assignment/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       └── wheel_spec.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚠️ Assumptions & Notes

- No user authentication is implemented (as per assignment scope)
- `fields` is stored as a JSON column to accommodate dynamic values
- Dates must follow `YYYY-MM-DD` format
- The project is containerized for easier deployment

---

## 👤 Author

**Name**: Salman Ahmad  
**Email**: salmanmohammad399@gmail.com  
**GitHub**: [github.com/blacxtar](https://github.com/blacxtar)
