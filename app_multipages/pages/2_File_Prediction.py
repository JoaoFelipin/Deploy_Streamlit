import pickle
import streamlit as st 
import pandas as pd


st.set_page_config(page_title='Deploy do modelo de insurance')
st.title('Insurance Prediction')
st.sidebar.header('Upload File')

data = st.file_uploader('Upload your file')



with open('models/model.pkl','rb') as model_file:
    model = pickle.load(model_file)


if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction=insurance_prediction)

    st.markdown('Insurance Cost Prediction')
    st.write(df_output)