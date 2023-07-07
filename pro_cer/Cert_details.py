import streamlit as st
import pandas as pd

redirect_url = ['https://www.guvi.in/verify-certificate?id=1o8539e2i6x8ufs615',
                'https://www.guvi.in/verify-certificate?id=H67F96NVI41118A6o3',
                'https://www.guvi.in/verify-certificate?id=4g5W658168p677Iln8',
                'https://www.kaggle.com/learn/certification/nataraj96/intro-to-programming',
                'https://www.hackerrank.com/certificates/b38eaa644dd2'
                ]

def cert_sel():
    dfa1,cerc, cerc2, afa2 = st.columns([2,6,3,1])
    with cerc:
        st.write("1. Guvi-Python (Basic to Advanced) Certificate")
        st.markdown('<br>', unsafe_allow_html=True) 
        st.write("2. Guvi-Introduction to Data Engineering and Bigdata")
        #st.markdown('<br>', unsafe_allow_html=True)
        st.write("")  
        st.write("3. Guvi-Data Analytics Using Pandas")
        st.markdown('<br>', unsafe_allow_html=True) 
        st.write("4. Kaggle-Intro to Programming.Certificate")
        #st.markdown('<br>', unsafe_allow_html=True) 
        st.write("") 
        st.write("5. Hackerrank-SQL (Intermediate) Certificate")
    with cerc2:
        st.write(f"##### [Verification link]({redirect_url[0]})")
        st.markdown('<br>', unsafe_allow_html=True)
        st.write("")  
        st.write(f"##### [Verification link]({redirect_url[1]})")
        st.markdown('<br>', unsafe_allow_html=True)
        st.write(f"##### [Verification link]({redirect_url[2]})")
        #st.markdown('<br>', unsafe_allow_html=True)
        st.write("")  
        st.write(f"##### [Verification link]({redirect_url[3]})")
        #st.markdown('<br>', unsafe_allow_html=True)
        st.write("") 
        st.write(f"##### [Verification link]({redirect_url[4]})")

