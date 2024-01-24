import streamlit as st 



st.set_page_config(
    page_title='Deploy do modelo de insurance',
    page_icon='D:\Desktop\Scripts\Deploy_Streamlit\img\stethoscope.png'
)
st.title('Insurance Prediction')

st.sidebar.header('Project Description')
st.write('\n\n')

st.image('img/health_insurance_img.jpg')

st.success('Please go to the other page to make predictions')