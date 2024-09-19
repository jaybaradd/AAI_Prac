import streamlit as st
st.title('Hello world')
st.subheader('this is a subheader')

name = st.text_input('Enter your name')

st.write('Hello ', name)

maths = st.slider('enter your marks',0,100)
st.write(name, ' scored ', maths, ' marks in math')

exam = st.radio('choose an exam ',['GRE','GMAT','none hehe'])
st.write('You chose ',exam)

subjects = st.multiselect(
    'Choose your subjects ', ['math','phy','chem','stats']
)

st.write('You chose ', subjects )

import pandas as pd
uploaded_file = st.file_uploader('choose a file ', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

