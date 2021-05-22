import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

rad=st.sidebar.radio("Menu",["Home","Education and Experience","Projects","Technologies and Tools"])
if rad == "Home":
    a,b,c=st.beta_columns(3)
    b.title('Chiranthana R R')
    
    p,q,r=st.beta_columns(3)
    q.image("/Users/chiranthanarr/portfolio/0C3B8359-4504-45D3-91DD-0BE600C0B26F_4_5005_c.jpeg")
    st.markdown("""
    ### I am a computer science engineering student at SRMIST , passionate and enthusiastic about exploring the field data science and web scraping deeper.""",True)
    
    st.header("Connect me")
    m,n,o=st.beta_columns(3)
    m.header('[LINKEDIN](https://www.linkedin.com/in/chiranthana-r-r-232385200/)')
    m.image('174857.png')
    n.header('[GITHUB](https://github.com/chiru30/)')
    n.image('25231.png')
    o.header('[MEDIUM](https://chiranthana30rr.medium.com)')
    o.image('unnamed.png')
