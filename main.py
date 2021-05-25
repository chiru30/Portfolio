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
    
    LOGO_IMAGE = "0C3B8359-4504-45D3-91DD-0BE600C0B26F_4_5005_c.jpeg"


    st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #faebd7 !important;
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
    #a.image('0C3B8359-4504-45D3-91DD-0BE600C0B26F_4_5005_c.jpeg' ,width=380)
    
   #x,y,z=st.beta_columns(3)
    #y.markdown("""
    ## DATA ENTHUSIAST """,True)

    st.write("## I am a computer science engineering student at SRMIST , passionate and enthusiastic about exploring the field data science and machine learning deeper.")


    x2,y2,z2=st.beta_columns(3)
    #components.html("""<iframe src="https://giphy.com/embed/9JrkkDoJuU0FbdbUZU" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/90s-drawing-welcome-9JrkkDoJuU0FbdbUZU">via GIPHY</a></p>""", width=480,height=480)
    y2.image('giphy1.gif')
   
    

    
    x1,y1,z1=st.beta_columns(3)
    y1.markdown(""" ## Connect me """)
    st.write("\n")
    
    m,n,o=st.beta_columns(3)
    #m.header('[LINKEDIN](https://www.linkedin.com/in/chiranthana-r-r-232385200/)')
    #m.image('174857.png')
    #n.header('[GITHUB](https://github.com/chiru30/)')
    #n.image('25231.png')
    #o.header('[MEDIUM](https://chiranthana30rr.medium.com)')
    #o.image('unnamed.png')
    

    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
            return base64.b64encode(data).decode()
    @st.cache(allow_output_mutation=True)
    def get_img_with_href (local_img_path, target_url):
        img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
        bin_str = get_base64_of_bin_file(local_img_path)
        html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
        return html_code
    
    medium_html = get_img_with_href('medium.png', 'https://chiranthana30rr.medium.com')
    o.markdown(medium_html, unsafe_allow_html=True)

    linkedin_html = get_img_with_href('linkedin_logo.png', 'https://www.linkedin.com/in/chiranthana-r-r-232385200/')
    m.markdown(linkedin_html, unsafe_allow_html=True)

    github_html = get_img_with_href('github.png', 'https://github.com/chiru30/')
    n.markdown(github_html, unsafe_allow_html=True)
