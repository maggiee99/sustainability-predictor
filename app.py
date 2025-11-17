import streamlit as st
import pickle
import numpy as np

#Load model
with open('lrmodel_sustainable.pkl', 'rb') as file:
    model = pickle.load(file)

#Title for the web app
st.title("Sustainable Product Demand Predictor")

#User inputs for prediction
carbon_emmisions = st.number_input("Carbon Emissions (in tons)", min_value=0.0, format='%f')
energy_output = st.number_input("Energy Output : ", min_value=0.0, format='%f')
renewability_index = st.number_input("Renewability Index : ", min_value=0.0, format='%f')
cost_efficiency = st.number_input("Cost_efficiency : ", min_value=0.0, format='%f')

#Predict button
if st.button("Predict Demand"):
    #Prepare input data for prediction
    input_data = np.array([[carbon_emmisions, energy_output, renewability_index, cost_efficiency]])
    
    #Make prediction
    prediction = model.predict(input_data)
    
    #Display the result
    if prediction[0] == 1:
        st.success(f"Product is sustainable with a demand prediction of {prediction[0]}")
    else:
        st.info(f"Product is not sustainable with a demand prediction of {prediction[0]}")