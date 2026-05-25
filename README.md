# 💸 Expense Tracker API

A personal expense tracking REST API built with **FastAPI** and **MongoDB**, with automated workflows powered by **n8n**.

---

## 🛠️ Tech Stack

- **FastAPI** — REST API framework
- **MongoDB** — NoSQL database
- **Motor** — Async MongoDB driver
- **Beanie** — MongoDB ODM built on Pydantic
- **n8n** — Workflow automation (self-hosted via Docker)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- MongoDB running locally
- Docker (for n8n)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create your environment file
cp .env.example .env
```

### Environment Variables

Create a `.env` file in the root of the project:

```
MONGO_URI=mongodb://localhost:27017
DB_NAME=expense_tracker
```

### Run the API

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

Interactive docs (Swagger UI) at `http://localhost:8000/docs`

---

## 📌 API Endpoints

### Expenses

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/expenses` | Create a new expense |
| `GET` | `/expenses` | Get all expenses |
| `GET` | `/expenses/{id}` | Get a single expense by ID |
| `DELETE` | `/expenses/{id}` | Delete an expense |

### Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/expenses/summary` | Get total spent grouped by category |

---

## 📝 Request & Response Examples

### Create Expense — `POST /expenses`

**Request body:**
```json
{
  "amount": 3000,
  "category": "Food",
  "description": "Chinese food",
  "date": "2026-05-25T00:00:00"
}
```

**Response:**
```json
{
  "id": "683b1f4e2a1c4d0012e3a5f7",
  "amount": 3000,
  "category": "Food",
  "description": "Chinese food",
  "date": "2026-05-25T00:00:00"
}
```

### Get Summary — `GET /expenses/summary`

**Response:**
```json
{
  "Food": 5500,
  "Transport": 1200,
  "Entertainment": 800
}
```

---

## ⚙️ n8n Automation

n8n runs locally via Docker and connects to the API to automate two workflows.

### Run n8n with Docker

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Open n8n at `http://localhost:5678`

> **Note:** Inside Docker, use `http://host.docker.internal:8000` to reach the FastAPI app running on your machine.

---

### Workflow 1 — Weekly Spending Digest 📊

Runs every **Sunday at 8:00 PM** and sends a spending summary for the week.

**Flow:**
```
Schedule Trigger (Sunday 8PM)
  → HTTP Request GET /expenses/summary
  → Format message with category totals
  → Send Email (or Telegram notification)
```

**What you receive:**
```
📊 Weekly Expense Summary

Food:          $5,500
Transport:     $1,200
Entertainment: $800
─────────────────────
Total:         $7,500
```

---

### Workflow 2 — Budget Alert 🚨

Runs **every day at 9:00 AM** and sends a notification if any category exceeds a defined budget threshold.

**Flow:**
```
Schedule Trigger (Daily 9AM)
  → HTTP Request GET /expenses/summary
  → IF node: category total > threshold
  → Send Alert Notification
```

**Thresholds (configurable in the IF node):**

| Category | Limit |
|---|---|
| Food | $5,000 |
| Transport | $2,000 |
| Entertainment | $1,500 |

---

## 📁 Project Structure

```
expense-tracker/
├── main.py           # FastAPI app and routes
├── models.py         # Pydantic models (Expense, ExpenseResponse)
├── database.py       # MongoDB connection
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📦 Dependencies

```
fastapi
uvicorn
motor
beanie
pydantic
python-dotenv
```

Install all with:
```bash
pip install -r requirements.txt
```