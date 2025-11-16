🔥 Perfect — let’s upgrade your GitHub repo into a **portfolio-ready, production-grade project** with:

# ✅ 1. A Professional README

# ✅ 4. GitHub Actions CI/CD

# ✅ 5. Free Streamlit Cloud Deployment

---

# ✅ **STEP 1 — Your Professional README (Copy-Paste into README.md)**

Below is a **fully polished, premium-level README** perfect for interviews, LinkedIn, and portfolio.

---

## 🚀 **Customer Churn Prediction App (FastAPI + Streamlit + Docker + Azure VM)**

An end-to-end **production-ready** SaaS churn prediction system built using:

* **FastAPI** (Backend ML API)
* **XGBoost Model** (Predict churn probability)
* **Streamlit UI** (Frontend Web App)
* **Docker + Docker Compose**
* **Azure Virtual Machine** (Live Deployment)

This project predicts whether a customer is likely to churn based on subscription activity, product usage, and support interactions.

---

## 📌 **Features**

### 🔥 Machine Learning & Data

* Cleaned & processed 5 datasets (Accounts, Events, Usage, Subscriptions, Tickets)
* Feature engineering for churn labels
* XGBoost classifier tuned for highest accuracy
* Stored artefacts:

  * `churn_xgb_model.pkl`
  * `churn_feature_columns.pkl`
  * `churn_categorical_columns.pkl`

### ⚡ FastAPI Backend

* `/predict` API endpoint
* Real-time ML inference
* Dockerized microservice

### 🎨 Streamlit Frontend

* User-friendly app
* Sends input → FastAPI → shows churn probability
* Dockerized frontend service

### 🐳 Docker + Compose

Two fully isolated containers:

```
backend  → FastAPI (port 8000)
frontend → Streamlit (port 8501)
```

### ☁ Azure Deployment

Runs seamlessly on a Linux VM with Docker Compose.

---

## 🏗 **Project Architecture**

```
Customer_Churn/
│── models/
│── main.py                 # FastAPI backend
│── streamlit_app.py        # Streamlit UI
│── Dockerfile              # Backend Dockerfile
│── Dockerfile.streamlit    # Frontend Dockerfile
│── docker-compose.yml      # Runs both services
│── requirements.txt
│── *.csv                   # Data files
│── *.pkl                   # Model files
```

---

## 🚀 **How to Run Locally**

### 1️⃣ Clone repo

```sh
git clone https://github.com/Ali-akbark/customer-churn-app.git
cd customer-churn-app
```

### 2️⃣ Build & Run

```sh
docker compose up --build
```

Backend → [http://localhost:8000](http://localhost:8000)
Streamlit → [http://localhost:8501](http://localhost:8501)

---

## 🌐 **Live Azure Deployment**

Backend API
👉 [http://YOUR-AZURE-IP:8000/predict](http://YOUR-AZURE-IP:8000/predict)

Streamlit UI
👉 [http://YOUR-AZURE-IP:8501](http://YOUR-AZURE-IP:8501)

---

## 🧪 **Sample API Request**

```json
POST /predict

{
  "tenure": 12,
  "plan": "premium",
  "total_tickets": 3,
  "last_active_days": 5
}
```

---

## 🛠 Tech Stack

| Component       | Technology        |
| --------------- | ----------------- |
| ML Model        | XGBoost           |
| Backend         | FastAPI           |
| Frontend        | Streamlit         |
| Deployment      | Docker & Azure VM |
| Version Control | Git + GitHub      |
| CI/CD           | GitHub Actions    |

---

## 📝 Author

**Aliakbar Kanorewala**
End-to-End Data Scientist | Azure | Machine Learning | Deployment

---

