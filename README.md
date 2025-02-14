# 🛒 Walmart Demand Forecasting using XGBoost

This project builds a machine learning model to forecast weekly sales for Walmart stores using XGBoost and serves predictions through a Flask API.

---

## 📌 Project Overview
- **Domain:** Retail & Supply Chain  
- **Model:** XGBoost Regressor  
- **API:** Flask (Served locally)  
- **Tool:** Postman for Testing  
- **Deployment:** Local Flask API  

---

## 🗂 Data Description
The dataset contains weekly sales for different Walmart stores and includes the following features:
- `Store`: Store ID  
- `Date`: Week start date  
- `Weekly_Sales`: Sales for the store during the week  
- `Holiday_Flag`: Indicates if the week includes a major holiday  
- `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`: Economic factors  

---

## 🚀 Model Training and Features
- **Model:** XGBoost Regressor  
- **Features Used:**
  - Lag Features (`Lag_1`, `Lag_2`, `Lag_3`, `Lag_4`)  
  - Moving Averages (`MA_4`, `MA_12`)  
  - Store, Holiday Flag, and Economic Indicators  

---

## 🛠️ API Setup and Usage
### **1️⃣ Install Dependencies**
```bash
pip install flask pandas numpy xgboost
