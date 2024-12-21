import streamlit as st
import requests
import json

# Define the Lambda endpoint URL
lambda_endpoint_url = "https://z2d9mnmysd.execute-api.eu-west-1.amazonaws.com/dev/binaryclassify"

# Streamlit app title
st.title("Text Review Prediction")

# Input text area for the user to enter reviews
user_input = st.text_area("Enter your review:")
final_input=user_input.split('\n')
# Define a function to make a POST API request to Lambda
def invoke_lambda(input_text):
    payload = {"sentences": input_text}
    response = requests.post(lambda_endpoint_url, json=payload)
    return response.json()

# Check if the user has entered text and submitted
if st.button("Predict"):
    if user_input:
        st.write("Input Review:", user_input)
        # Call the Lambda function to get predictions
        predictions = invoke_lambda(final_input)
        st.write("Predictions:", json.dumps(predictions, indent=4))
    else:
        st.warning("Please enter a review before predicting.")