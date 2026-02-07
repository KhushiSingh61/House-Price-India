🏠 Predicting House Prices Using Property and Location Features
📌 Problem Overview

Accurate house price prediction is crucial for real estate companies, investors, and buyers to make informed decisions. Real-world property data is often incomplete, inconsistent, and affected by multiple factors such as location, size, amenities, and surrounding infrastructure. This project aims to build an end-to-end machine learning solution that predicts house prices using regression techniques while handling real-world data challenges.

The project covers the complete machine learning lifecycle, from data collection and preprocessing to model deployment using Streamlit.

📊 Dataset

Source: Kaggle Website

Format: CSV file

Size: 14,000+ rows

Features: 20+ property and location-related attributes

Target Variable: House Price

Sample Features

Number of bedrooms and bathrooms

Living area and lot area

Number of floors

House condition and grade

Built year and renovation year

Latitude and longitude

Distance from airport

Number of schools nearby

🛠️ Machine Learning Workflow

The following mandatory ML stages were implemented:

Problem understanding & target definition

Data collection and inspection

Data cleaning (missing values, duplicates)

Exploratory Data Analysis (EDA) with insights

Feature engineering and preprocessing

Train–test split

Training multiple regression models

Model evaluation and comparison

Model saving using pickle

Local deployment using Streamlit

🤖 Models Used

The following regression models were trained and evaluated:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

✅ Final Model Selection

The Gradient Boosting Regressor was selected as the final model based on:

Lowest RMSE

Better generalization on test data

Strong performance on non-linear relationships

The trained model was saved as:

house_price_model.pkl

🚀 Streamlit Deployment

A local web application was built using Streamlit to allow users to input house details and get real-time price predictions.

How to Run the Streamlit App Locally

Clone the repository:

git clone <repository-url>
cd <repository-folder>


Install required libraries:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


📁 Repository Structure
├── House Price India.csv
├── House_Price_Prediction.ipynb
├── house_price_model.pkl
├── app.py
├── README.md

📈 Conclusion

This project demonstrates a complete real-world machine learning pipeline, from raw data handling to model deployment. It highlights the importance of feature consistency, preprocessing, and model evaluation while showcasing how machine learning models can be deployed for practical use using Streamlit.

✅ End-to-End Machine Learning | Regression | Streamlit Deployment
