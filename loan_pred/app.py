import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open('trained_lap_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Title and description
st.title('Loan Approval Prediction')
st.write('Enter the following details to check if your loan will be approved.')

# Input fields
no_of_dependents = st.number_input('Number of Dependents', min_value=0, value=0)
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['No', 'Yes'])
income_annum = st.number_input('Annual Income', min_value=0, value=0)
loan_amount = st.number_input('Loan Amount', min_value=0, value=0)
loan_term = st.number_input('Loan Term (in months)', min_value=0, value=0)
cibil_score = st.number_input('CIBIL Score', min_value=0, value=0)
residential_assets_value = st.number_input('Residential Assets Value', min_value=0, value=0)
commercial_assets_value = st.number_input('Commercial Assets Value', min_value=0, value=0)
luxury_assets_value = st.number_input('Luxury Assets Value', min_value=0, value=0)
bank_asset_value = st.number_input('Bank Asset Value', min_value=0, value=0)

# Convert categorical variables to numerical values
education_encoded = 1 if education == 'Graduate' else 0
self_employed_encoded = 1 if self_employed == 'Yes' else 0

# Create a dictionary from user inputs
user_data = [
no_of_dependents,
education_encoded,
self_employed_encoded,
income_annum,
loan_amount,
loan_term,
cibil_score,
residential_assets_value,
commercial_assets_value,
luxury_assets_value,
bank_asset_value
]

# Convert user data into a DataFrame
user_df = np.array([user_data])

# Predict button
if st.button('Predict Loan Approval'):
    # Make predictions using the trained model
    prediction = model.predict(user_df)
    
    # Display the prediction
    if prediction == 1:
        st.write('Congratulations! Your loan is approved.')
    else:
        st.write('Sorry, your loan is not approved.')

# Note to the user

