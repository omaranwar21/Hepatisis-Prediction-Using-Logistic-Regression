import streamlit as st
import pickle as pkle
import numpy as np
import os.path

# --------------------------------Page Configuration--------------------------------#
st.set_page_config(layout="wide", page_icon='💡', page_title="C Prediction")
content_left, space1, content_middle, space2, content_right = st.columns([1, 0.3, 1.5, 0.3, 1])

if 'next_clicked' not in st.session_state or 'User_Data' not in st.session_state or 'User_Name' not in st.session_state:
    st.session_state.next_clicked = 0
    st.session_state.User_Data = []
    st.session_state.User_Name = ''

with open("style.css")as f:
    st.markdown(f"<style>{f.read() }</style>", unsafe_allow_html=True)
pages = ['Start','Page2','Page3']

def thirdPage():
    with content_middle:
        st.header("")
        st.header("")
        st.header("")
        st.header("")
        st.header("")
        st.title('The Result')

        X_predict = np.array(st.session_state.User_Data)
        X_predict.reshape(1, -1)
        #st.write(X_predict.reshape(1, -1))
        loaded_model = pkle.load(open(
            r"..\Hepatisis_prediction_model",
            'rb'))
        x = loaded_model.predict(X_predict.reshape(1, -1))
        prediction = x[0]
        if x[0] == 0:
            prediction = 'Fortunately, You are in good health and do not suffer from any infections in the liver'
        else:
            prediction = 'Unfortunately, you suffer from Hepatisis, see a doctor as soon as possible'
        st.header("Welcome "+ st.session_state.User_Name)
        st.header(prediction)

    return 'Finish'

def firstPage():
    
    with content_left:
        st.title('Hepatisis Prediction')
        st.header("Data Information")
        st.text("The target attribute for classification is Category \n(blood donors vs. Hepatitis C (including its progress ('just' Hepatitis C,\n Fibrosis, and Cirrhosis).")
        st.markdown('+ **Hepatitis C** is a liver infection caused by the hepatitis C virus (HCV).')
        st.markdown('+ **Liver fibrosis** is the outcome of the wound healing response to tissue damage caused by chronic HCV infection.')
        st.markdown('+ **Cirrhosis:** The hepatitis C virus slowly damages the liver over many years, often progressing from inflammation to permanent, irreversible scarring.')
        st.markdown("### Model Precision 50%")
        st.markdown("### Model Accuracy 88.62%")
        st.markdown("### Model Sensitivity 85.7%")
    with content_middle:
        st.header("Model & Evaluation")
        st.markdown("The data is imbalanced, so the model is evaluated using the **confusion matrix** ")
        st.image('confusion_matrix.png')
        st.markdown("# Precision \n### Of the positives predicted, what percentage is truly positive \n### Precision does not evaluate the correctly predicted negative cases")
    with content_right:
        st.markdown("# Accuracy \n### Accuracy measures how often the model is correct.")
        st.markdown("# Sensitivity (Recall) \n### Of all the positive cases, what percentage are predicted positive \n### Sensitivity (sometimes called Recall) measures how good the model is at predicting positives. \n### This means it looks at true positives and false negatives (which are positives that have been incorrectly predicted as negative).\n### Sensitivity is good at understanding how well the model predicts something is positive")


def secondPage():
    with content_left:

        st.header("")
        st.header("")
        st.title('Hepatisis Prediction')
        st.write("")
        st.write("Please enter the following data:")
        st.session_state.User_Name = st.text_input("Name")
        User_Sex = st.selectbox('Gender', ('Male', 'Female'))
        User_Age = st.number_input("Age", step=1)

    with content_middle:
        st.header("")
        st.header("")
        st.write("")
        User_CREA = st.number_input("CREA level", step=0.1)
        User_ALB = st.number_input("ALB level", step=0.1)
        User_ALP = st.number_input("ALP level", step=0.1)
        User_ALT = st.number_input("ALT level", step=0.1)
        User_AST = st.number_input("AST level", step=0.1)

        submitted = st.button("Predict")

    with content_right:
        st.header("")
        st.header("")
        st.write("")
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
        title = 'Get Started'
        if choice == 'Start':
            firstPage()

        elif choice == 'Page2':
            title = secondPage()

        elif choice == 'Page3':
            title = thirdPage()

with content_left:
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
