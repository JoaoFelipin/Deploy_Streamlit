import pickle as pk 
import streamlit as st 
import pandas as pd 


st.set_page_config(page_title='Deploy do modelo de insurance')

#parametros
idade = st.number_input(label='Age',value=18,min_value=18,max_value=120)
bmi = st.number_input(label='BMI',value=30.0)
children = st.slider(label='Children',min_value=0)
smoker = st.selectbox(label='Smoker',options=['No','Yes'])

