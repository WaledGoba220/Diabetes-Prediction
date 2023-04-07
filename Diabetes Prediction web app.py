# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 01:26:16 2023

@author: lenovo
"""

import numpy as np
import pickle
import streamlit as st



loaded_model = pickle.load(open(r"C:\Users\lenovo\Desktop\Projects\Diabetes Binary Classification\model.pkl",'rb'))

## creating a function for prediction

def diabets_prediction(input_data):
 #   input_data = (5,166,72,19,175,25.8,0.587,51)
 
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data,dtype=float)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
     return 'The person is Normal, Negative Diabetes '
    else:
       return 'The Person is Positive Diabetes '
    
    

    

def main():
    st.title("Diabetes Prediction System")
    
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    
    ## getting the input data from user
    
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Level")
    DiabetesPedigreeFunction = st.text_input(" Diabetes Pedigree Function Value")
    Age = st.text_input("Age of The Person")
    
    
    ## code for prediction
    
    diagnosis = ''
    
    ## creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabets_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(diagnosis)
    
if __name__ == '__main__':
        main()




