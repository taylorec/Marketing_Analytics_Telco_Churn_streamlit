import streamlit as st
import joblib
import pandas as pd

st.title("Customer Churn Prediction")
st.write("This model predicts if a customer will churn.")

loaded_GBC = joblib.load('GBC.joblib')

Avg_Calls = st.number_input('Average number of calls made', min_value=0)
Complaint_Code = st.selectbox('Complaint type', ['Billing Problem', 'Call Quality', 'Moving', 'Check Account', 'Inaccurate Sales Information', 'Pricing'])
Account_Age = st.number_input('Age of account', min_value=10)
Avg_Days_Delinquent = st.number_input('Average number of days the customer is late on payment', min_value=0)
Percent_Increase_MOM = st.number_input('Month-over-month percentage billing increase', min_value=-1.0)
Avg_Calls_Weekdays = st.number_input('Average number of calls made on weekdays', min_value=0)
Current_Bill_Amt = st.number_input("Customer's current bill amount", min_value=0)


if Complaint_Code == 'Billing Problem':
    Complaint_Code = 0
elif Complaint_Code == 'Call Quality':
    Complaint_Code = 1
elif Complaint_Code == 'Check Account':
    Complaint_Code = 2
elif Complaint_Code == 'Inaccurate Sales Information':
    Complaint_Code = 3
elif Complaint_Code == 'Moving':
    Complaint_Code = 4
elif Complaint_Code == 'Pricing':
    Complaint_Code = 5
    
data = pd.DataFrame([[Avg_Days_Delinquent,Percent_Increase_MOM, 
                                  Avg_Calls_Weekdays,Current_Bill_Amt,
                                  Avg_Calls,Complaint_Code,Account_Age]])
    
prediction = loaded_GBC.predict(data)
if prediction == 0:
    prediction = 'No, this model predicts the customer will not churn.'
else: 
    prediction = 'Yes, this model predicts the customer will churn'
st.write('Is this customer predicted to churn? {}'.format(prediction))