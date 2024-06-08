

import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('model.pkl')

# Title of the app
st.title('Customer Churn Prediction')

# Sidebar for user input
st.sidebar.header('User Input')

# Input fields for user to enter data
# Modify these based on your dataset
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
SeniorCitizen = st.sidebar.selectbox('Senior Citizen', ['Yes', 'No'])
Partner = st.sidebar.selectbox('Partner', ['Yes', 'No'])
Dependents = st.sidebar.selectbox('Dependents', ['Yes', 'No'])
# Add more input fields as needed

# Create a dataframe for prediction
data = {'gender': [gender], 'SeniorCitizen': [SeniorCitizen], 'Partner': [Partner], 'Dependents': [Dependents]}
df = pd.DataFrame(data)

# Make predictions
prediction = model.predict(df)

# Display the prediction
st.write('Prediction:', prediction[0])
