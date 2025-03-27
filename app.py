import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from src.logger import log_info, log_error

# Load model
model_path = Path("../models/sales_prediction.pkl")
model = joblib.load(model_path)

st.title("🛒 BigMart Sales Prediction")
log_info("Streamlit App Started")


item_weight = st.number_input("Item Weight", min_value=1.0, max_value=50.0, value=5.0)
item_visibility = st.number_input("Item Visibility", min_value=0.0, max_value=0.3, value=0.05)
item_mrp = st.number_input("Item MRP", min_value=10.0, max_value=300.0, value=50.0)

input_data = pd.DataFrame([[item_weight, item_visibility, item_mrp]], columns=["Item_Weight", "Item_Visibility", "Item_MRP"])

if st.button("Predict Sales"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"✅ Predicted Sales: ₹{prediction:.2f}")
        log_info(f"Prediction Success: {prediction}")
    except Exception as e:
        st.error("❌ Prediction failed")
        log_error(f"Prediction Error: {e}")
