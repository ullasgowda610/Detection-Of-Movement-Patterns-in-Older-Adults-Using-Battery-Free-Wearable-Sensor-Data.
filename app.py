
import streamlit as st
import numpy as np
import pandas as pd
import joblib

with open("final_model.joblib","rb") as file:
    model=joblib.load(file)

def prediction(inp_list):

    pred=model.predict([inp_list])[0]
    if pred==0:
        return "Sitting on bed"
    elif pred==1:
        return "Sitting on chair"
    elif pred==2:
        return "Lying on Bed"
    else:
        return "Ambulating"

        
def main():
    st.title("Activity Prediction from Sensor Data")
    st.subheader("This Application will predict the ongoing activity of the basis of sensor data provided. Fill the respective fields it will be predicted.")
    st.image("Image.jpg")

    rfid=st.selectbox("Enter the RFID configuration settings",["Config 1 (4 Sensors)","Config 2 (3 Sensors)"])
    rfid_e= (lambda x: 3 if x=="Config 2 (3 Sensors)" else 4)(rfid)

    ant_id=st.selectbox("Select the Antenna ID ",[1,2,3,4])
    rssi=st.number_input("Enter the Recieved signal strength indicator (RSSI) ",format="%.6f")
    accv=st.number_input("Enter the Vertical Acceleration from the Sensor",format="%.6f")
    accf=st.number_input("Enter the frontal Acceleration from the Sensor",format="%.6f")
    accl=st.number_input("Enter the lateral Acceleration from the Sensor",format="%.6f")

    input_data=[accf,accv,accl,ant_id,rssi,rfid_e]

    if st.button("Predict"):
        response=prediction(input_data)
        st.success(response)


if __name__=="__main__":
    main()
