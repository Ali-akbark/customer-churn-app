import streamlit as st
import requests

st.set_page_config(page_title="SaaS Churn Prediction", layout="wide")

st.title("📊 SaaS Customer Churn Prediction App")

st.write("Enter customer details below to predict churn probability.")

# FastAPI endpoint
API_URL = "http://fastapi:8000/predict"


# ----------------------------
# INPUT FORM
# ----------------------------
with st.form("churn_form"):
    st.subheader("Customer Information")

    industry = st.selectbox("Industry", ["FinTech", "HealthTech", "EdTech", "DevTools", "Cybersecurity"])
    country = st.selectbox("Country", ["US", "IN", "UK", "CA", "FR", "DE"])
    referral_source = st.selectbox("Referral Source", ["organic", "partner", "ads", "event", "other"])
    plan_tier = st.selectbox("Current Plan Tier", ["Basic", "Pro", "Enterprise"])
    
    seats = st.number_input("Seats", min_value=1, max_value=500)
    is_trial = st.selectbox("Is Trial?", [0, 1])
    churn_flag_final = st.selectbox("Historical Churn Flag", [0, 1])  # optional
    churn = st.selectbox("Churn Label", [0, 1])  # optional
    
    total_subscriptions = st.number_input("Total Subscriptions", min_value=1, max_value=50)
    latest_plan_tier = st.selectbox("Latest Plan Tier", ["Basic", "Pro", "Enterprise"])
    max_seats = st.number_input("Max Seats Observed", min_value=1, max_value=500)
    
    current_mrr = st.number_input("Current MRR ($)", min_value=0)
    current_arr = st.number_input("Current ARR ($)", min_value=0)

    total_upgrades = st.number_input("Total Upgrades", min_value=0)
    total_downgrades = st.number_input("Total Downgrades", min_value=0)
    auto_renew_count = st.number_input("Auto Renew Count", min_value=0)

    total_usage_count = st.number_input("Total Usage Count", min_value=0)
    total_usage_seconds = st.number_input("Total Usage Seconds", min_value=0)
    unique_features_used = st.number_input("Unique Features Used", min_value=0)
    total_errors = st.number_input("Total Errors", min_value=0)

    total_tickets = st.number_input("Total Support Tickets", min_value=0)
    avg_resolution_hours = st.number_input("Avg Resolution Hours", min_value=0.0)
    avg_first_response_minutes = st.number_input("Avg First Response Minutes", min_value=0.0)
    avg_satisfaction_score = st.number_input("Avg Satisfaction Score", min_value=0.0)
    total_escalations = st.number_input("Total Escalations", min_value=0)

    submitted = st.form_submit_button("Predict Churn")

# ----------------------------
# SEND TO API
# ----------------------------
if submitted:
    data = {
        "industry": industry,
        "country": country,
        "referral_source": referral_source,
        "plan_tier": plan_tier,
        "seats": seats,
        "is_trial": is_trial,
        "churn_flag_final": churn_flag_final,
        "churn": churn,
        "total_subscriptions": total_subscriptions,
        "latest_plan_tier": latest_plan_tier,
        "max_seats": max_seats,
        "current_mrr": current_mrr,
        "current_arr": current_arr,
        "total_upgrades": total_upgrades,
        "total_downgrades": total_downgrades,
        "auto_renew_count": auto_renew_count,
        "total_usage_count": total_usage_count,
        "total_usage_seconds": total_usage_seconds,
        "unique_features_used": unique_features_used,
        "total_errors": total_errors,
        "total_tickets": total_tickets,
        "avg_resolution_hours": avg_resolution_hours,
        "avg_first_response_minutes": avg_first_response_minutes,
        "avg_satisfaction_score": avg_satisfaction_score,
        "total_escalations": total_escalations
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()
        pred = result["churn_prediction"]
        proba = result["churn_probability"]

        st.success(f"**Churn Probability:** {proba:.2f}")
        st.info(f"**Churn Prediction (0=No, 1=Yes):** {pred}")
    else:
        st.error("Error calling API!")
