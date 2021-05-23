import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import os
import base64

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
