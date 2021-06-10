from altair.vegalite.v4.schema.core import Align
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import os
import base64


import streamlit.components.v1 as components

st.set_page_config(layout="wide")


rad=st.sidebar.radio("Menu",["Home","Education and Experience","Projects","Technologies and Tools","Certifications and Courses"])
if rad == "Home":
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return
    set_png_as_page_bg('Static/homef.gif')

    LOGO_IMAGE = "Static/0C3B8359-4504-45D3-91DD-0BE600C0B26F_4_5005_c.jpeg"


    st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #ffffff!important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True)


    st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">  CHIRANTHANA R R</p>
    </div>
    """,
    unsafe_allow_html=True)


    

    #a,b,c=st.beta_columns(3)
    #c.title('Chiranthana R R')

    #p,q,r=st.beta_columns(3)
    #q.image('Static/0C3B8359-4504-45D3-91DD-0BE600C0B26F_4_5005_c.jpeg' ,width=380)
    
   #x,y,z=st.beta_columns(3)
    #y.markdown("""
    ## DATA ENTHUSIAST """,True)
    st.write("\n")

    html_temp = """
    <div style="background:#ffffff;padding:1px">
    <h2 style="color:black;text-align:center;"> I am a computer science engineering student at SRMIST , passionate and enthusiastic about exploring the field data science and machine learning deeper. </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    #st.write("## I am a computer science engineering student at SRMIST , passionate and enthusiastic about exploring the field data science and machine learning deeper.")


    #x2,y2,z2=st.beta_columns(3)
    #components.html("""<iframe src="https://giphy.com/embed/9JrkkDoJuU0FbdbUZU" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/90s-drawing-welcome-9JrkkDoJuU0FbdbUZU">via GIPHY</a></p>""", width=480,height=480)
    #y2.image('Static/giphy1.gif')

    x1,y1,z1=st.beta_columns(3)
    html_temp = """
    <p>
    <div style="background:#ffffff;padding:1px">
    <h3 style="color:black;text-align:center;"> CONNECT ME : </h3>
    </div>
    </p>
    """
    y1.markdown(html_temp, unsafe_allow_html = True)
    
    
    m,n,o=st.beta_columns(3)
    #m.header('[LINKEDIN](https://www.linkedin.com/in/chiranthana-r-r-232385200/)')
    #m.image('174857.png')
    #n.header('[GITHUB](https://github.com/chiru30/)')
    #n.image('25231.png')
    #o.header('[MEDIUM](https://chiranthana30rr.medium.com)')
    #o.image('unnamed.png')
