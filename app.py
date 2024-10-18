import streamlit as st
import pickle
import pandas as pd

# Load your trained model
with open('fraud_detection_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_fraud(step, amount, oldbalanceDest, isFlaggedFraud, type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER, balanceChangedest, balanceChange):
    input_data = pd.DataFrame({
        'step': [step],
        'amount': [amount],
        'oldbalanceDest': [oldbalanceDest],
        'isFlaggedFraud': [isFlaggedFraud],
        'type_CASH_OUT': [type_CASH_OUT],
        'type_DEBIT': [type_DEBIT],
        'type_PAYMENT': [type_PAYMENT],
        'type_TRANSFER': [type_TRANSFER],
        'balanceChangedest': [balanceChangedest],
        'balanceChange': [balanceChange]
    })
    
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("Anamoly Detection Using PYOD")

step = st.number_input("Step", min_value=0)
amount = st.number_input("Amount", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)
isFlaggedFraud = st.selectbox("Is Flagged Fraud", (0, 1))
type_CASH_OUT = st.number_input("Type CASH OUT", min_value=0)
type_DEBIT = st.number_input("Type DEBIT", min_value=0)
type_PAYMENT = st.number_input("Type PAYMENT", min_value=0)
type_TRANSFER = st.number_input("Type TRANSFER", min_value=0)
balanceChangedest = st.number_input("Balance Change Destination", min_value=0.0)
balanceChange = st.number_input("Balance Change", min_value=0.0)

if st.button("Predict"):
    prediction = predict_fraud(step, amount, oldbalanceDest, isFlaggedFraud, type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER, balanceChangedest, balanceChange)
    if prediction == 1:
        st.success("Transaction is Fraudulent")
    else:
        st.success("Transaction doesn't seem to be Fraudulent.")
