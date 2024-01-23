import streamlit as st 

st.set_page_config(page_title='Aula DNC')

st.write('Hello')

st.header('Titulo da página')
st.markdown('Aqui um texto')

st.sidebar.header('texto da sidebar')

nome = st.text_input('Nome')
st.write(f'ola {nome} ')

cargo = ['Engenheiro','Programador','Data Scientist']
select_cargo = st.sidebar.selectbox('Qual seu cargo?',options=cargo)
st.sidebar.write(select_cargo)
