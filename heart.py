# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:55:39 2022

@author: Afroz
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('heart.sav', 'rb'))



# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person has no heart Disease'
    else:
      return 'The person has heart Disease'
  
  
def main():
    
    #st.markdown(f'<h1 style="color:Brown;font-size:24px;">{"Heart Disease Prediction"}</h1>', unsafe_allow_html=True)
    # getting the input data from the user
    
    
    title = '<p style="font-family:Lucida Calligraphy; color:Red; font-size: 50px;">Heart Disease Prediction</p>'
    st.markdown(title, unsafe_allow_html=True)

   
    # Age
    #st.text_input('Age')          
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Age of the patient [years]</p>'
    st.markdown(title, unsafe_allow_html=True)
    Age = st.slider('Age', 0, 100, 30)                             
    st.write("Age ", Age, 'years old')
    
    # Sex
    # Sex = st.text_input('Sex')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Sex of the patient : Female = 0 , Male = 1 </p>'
    st.markdown(title, unsafe_allow_html=True)
    Sex = st.selectbox("Sex: ",['0','1'])                         
    st.write("You Selected: ", Sex)
    
    #ChestPainType
    #ChestPainType = st.text_input('ChestPainType')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">ChestPainType : Asymptomatic = 0 , Non-Anginal Pain = 1, Atypical Angina = 2 , Typical Angina = 3 </p>'
    st.markdown(title, unsafe_allow_html=True)
    ChestPainType = st.selectbox("ChestPainType: ",['0','1','2','3'])
    st.write("You Selected: ", ChestPainType)
    
    
    # RestingBP
    # RestingBP = st.text_input('RestingBP')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Resting blood pressure [mm Hg] </p>'
    st.markdown(title, unsafe_allow_html=True)
    RestingBP = st.slider('RestingBP', 0, 200, 30)
    st.write("RestingBP ", RestingBP)
    
    
    
    # Cholesterol
    # Cholesterol = st.text_input('Cholesterol')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Serum Cholesterol [mm/dl]</p>'
    st.markdown(title, unsafe_allow_html=True)
    Cholesterol = st.slider('Cholesterol', 0, 700, 50)
    st.write("Your Cholesterol is ", Cholesterol)
    
    
    # FastingBS
    # FastingBS = st.text_input('FastingBS')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]</p>'
    st.markdown(title, unsafe_allow_html=True)
    FastingBS = st.selectbox("FastingBS: ",['1','0'])
    st.write("You Selected: ",FastingBS)
    
    
    # RestingECG
    # RestingECG = st.text_input('RestingECG')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Resting electrocardiogram : Normal = 0 , LVH = 1 , ST = 2 </p>'
    st.markdown(title, unsafe_allow_html=True)
    RestingECG = st.selectbox("RestingECG : ",['0','1','2'])
    st.write("You Selected: ",RestingECG)
    
    
    # MaxHR
    # MaxHR = st.text_input('MaxHR')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Maximum heart rate achieved [Numeric value between 60 and 202]</p>'
    st.markdown(title, unsafe_allow_html=True)
    MaxHR = st.slider('MaxHR', 0, 250, 50)
    st.write("Your MaxHR is ", MaxHR)
    
    # ExerciseAngina
    # ExerciseAngina = st.text_input('ExerciseAngina')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Exercise-induced angina: No = 0 , Yes = 1 </p>'
    st.markdown(title, unsafe_allow_html=True)                        
    ExerciseAngina = st.selectbox("ExerciseAngina: ",['0','1'])
    st.write("You Selected: ",ExerciseAngina)
    
    
    # Oldpeak
    # Oldpeak = st.text_input('Oldpeak')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">ST [Numeric value measured in depression] : -3 to 7 </p>'
    st.markdown(title, unsafe_allow_html=True)
    Oldpeak = st.slider('Oldpeak', -3, 7, 1)
    st.write("Your Oldpeak is ", Oldpeak)
    
    
    
    # ST_Slope
    #ST_Slope = st.text_input('ST_Slope')
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">The slope of the peak exercise ST segment: Flat = 0 , Upsloping = 1 , Downsloping= 2 </p>'
    st.markdown(title, unsafe_allow_html=True)                     
    ST_Slope = st.selectbox("ST_Slope: ",['0','1','2'])
    st.write("You Selected: ",ST_Slope)
    
    
    
    
    # code for Prediction
    diagnosis = ''
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Age, Sex, ChestPainType,  RestingBP, Cholesterol, FastingBS, RestingECG,MaxHR, ExerciseAngina, Oldpeak,ST_Slope])
           
    st.success(diagnosis)
     
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  