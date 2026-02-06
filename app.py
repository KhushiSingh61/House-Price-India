import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict price")

# ---------------- INPUT FIELDS ----------------
living_area = st.number_input("Living Area (sqft)", min_value=100)
lot_area = st.number_input("Lot Area (sqft)", min_value=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1)
floors = st.number_input("Number of Floors", min_value=1)

# ---------------- DATA PREPARATION ----------------
expected_cols = model.feature_names_in_

# Create dataframe with all expected columns
input_data = pd.DataFrame(columns=expected_cols)
input_data.loc[0] = 0

# Fill values using EXACT column names
input_data["number of bedrooms"] = bedrooms
input_data["number of bathrooms"] = bathrooms
input_data["living area"] = living_area
input_data["lot area"] = lot_area
input_data["number of floors"] = floors

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")