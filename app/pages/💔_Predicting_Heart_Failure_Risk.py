import streamlit as st
from pathlib import Path
import pandas as pd
import pickle

st.title('💔 Predicting Heart Failure Risk')

with open(str(Path(__file__).parents[1]) + '/models/heart_failure_classifier.pkl', 'rb') as file:
  model = pickle.load(file)
    
@st.cache
def predict(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time):
  return model.predict(pd.DataFrame([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]]))

bool_options = {0: 'No', 1: 'Yes'}
sex_options = {0: 'Male', 1: 'Female'}

age = st.number_input('Age:', min_value=1)
anaemia = st.radio('Anaemia:', horizontal=True, options=list(bool_options.keys()), format_func=lambda x: bool_options[x])
creatinine_phosphokinase = st.number_input('Creatinine Phosphokinase:', min_value=0)
diabetes = st.radio('Diabetes:', horizontal=True, options=list(bool_options.keys()), format_func=lambda x: bool_options[x])
ejection_fraction = st.number_input('Ejection Fraction:', min_value=0)
high_blood_pressure = st.radio('High Blood Pressure:', horizontal=True, options=list(bool_options.keys()), format_func=lambda x: bool_options[x])
platelets = st.number_input('Platelets:', min_value=0)
serum_creatinine = st.number_input('Serum Creatinine:', min_value=0.0)
serum_sodium = st.number_input('Serum Sodium:', min_value=0)
sex = st.radio('Sex:', horizontal=True, options=list(sex_options.keys()), format_func=lambda x: sex_options[x])
smoking = st.radio('Smoking:', horizontal=True, options=list(bool_options.keys()), format_func=lambda x: bool_options[x])
time = st.number_input('Follow-Up Period (Days):', min_value=1)

if st.button('Predict'):
  prediction = predict(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time)
  
  if prediction[0]:
    st.error('You are at high risk of heart failure.')
  else:
    st.success('You are at low risk of heart failure.')