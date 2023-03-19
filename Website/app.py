import streamlit as st
import pickle as pkle
import numpy as np
import os.path

# --------------------------------Page Configuration--------------------------------#
st.set_page_config(layout="wide", page_icon='💡', page_title="C Prediction")
content_left, space1, content_middle, space2, content_right = st.columns([1, 0.3, 1.5, 0.3, 1])

if 'next_clicked' not in st.session_state or 'User_Data' not in st.session_state:
    st.session_state.next_clicked = 0
    st.session_state.User_Data = []

with open("style.css")as f:
    st.markdown(f"<style>{f.read() }</style>", unsafe_allow_html=True)
pages = ['Start','Page2','Page3']
# if os.path.isfile('next.p'):
#     next_clicked = pkle.load(open('next.p', 'rb'))
#     if next_clicked == len(pages):
#         next_clicked = 0
# else:
#     next_clicked = 0

def thirdPage():
    with content_middle:
        st.title('The Result')

        X_predict = np.array(st.session_state.User_Data)
        X_predict.reshape(1, -1)
        #st.write(X_predict.reshape(1, -1))
        loaded_model = pkle.load(open(
            r"C:\Partitiion\3rd Year\2nd Term\CDSS\Github Projects\Hepatisis-Prediction-Using-Logistic-Regression\Hepatisis_prediction_model",
            'rb'))
        x = loaded_model.predict(X_predict.reshape(1, -1))
        prediction = x[0]
        if x[0] == 0 or x[0] == 2 or x[0] == 3:
            prediction = 'Normal'
        elif x[0] == 1:
            prediction = 'Hepatitis'
        st.header(prediction)
    return 'Finish'

def firstPage():
    with content_middle:
        st.title('Welcome to our website')

def secondPage():
    with content_left:
        st.write("Please enter the following data:")
        User_Name = st.text_input("Name")
        User_Sex = st.selectbox('Gender', ('Male', 'Female'))
        User_Age = st.number_input("Age", step=1)
        User_CREA = st.number_input("CREA level", step=0.1)

    with content_middle:
        st.title('*Hepatits-C Prediction*')
        st.write("")
        st.write("")
        User_ALB = st.number_input("ALB level", step=0.1)
        User_ALP = st.number_input("ALP level", step=0.1)
        User_ALT = st.number_input("ALT level", step=0.1)
        User_AST = st.number_input("AST level", step=0.1)

        submitted = st.button("Predict")

    with content_right:
        st.write("")
        st.subheader("")
        User_BIL = st.number_input("BIL level", step=0.1)
        User_CHE = st.number_input("CHE level", step=0.1)
        User_CHOL = st.number_input("CHOL level", step=0.1)
        User_GGT = st.number_input("GGT level", step=0.1)
        User_PROT = st.number_input("PROT level", step=0.1)

    if User_Sex == 'Male':
        User_Sex = 1
    elif User_Sex == 'Female':
        User_Sex = 2
    st.session_state.User_Data = [User_Age,User_Sex,User_ALB,User_ALP,User_ALT,User_AST,User_BIL,User_CHE,User_CHOL,User_CREA,User_GGT,User_PROT]

    if submitted:
        st.session_state.next_clicked = st.session_state.next_clicked + 1
        st.experimental_rerun()

    return ''

with content_left:
    if next:
        if st.session_state.next_clicked == len(pages):
            st.session_state.next_clicked = 0
        choice = st.radio("",('Start','Page2', 'Page3'), index=st.session_state.next_clicked , horizontal=True , disabled=True)
        #pkle.dump(pages.index(choice), open('next.p', 'wb'))
        title = 'Get Started'
        if choice == 'Start':
            firstPage()

        elif choice == 'Page2':
            title = secondPage()

        elif choice == 'Page3':
            title = thirdPage()

with content_middle:
    if title == '':
        pass
    else:
        next = st.button(title)
        st.session_state.next_clicked = st.session_state.next_clicked + 1

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
