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
    y2.image('Static/giphy1.gif')
   
    

    
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
    
    medium_html = get_img_with_href('Static/medium.png', 'https://chiranthana30rr.medium.com')
    o.markdown(medium_html, unsafe_allow_html=True)

    linkedin_html = get_img_with_href('Static/linkedin_logo.png', 'https://www.linkedin.com/in/chiranthana-r-r-232385200/')
    m.markdown(linkedin_html, unsafe_allow_html=True)

    github_html = get_img_with_href('Static/github.png', 'https://github.com/chiru30/')
    n.markdown(github_html, unsafe_allow_html=True)

if rad == "Certifications and Courses" :
    st.header("COURSES")
    x2,y2=st.beta_columns(2)
    x2.header('[Data Science Professional Certificate](https://coursera.org/share/d94fecaa44cfd428602697b950af7b3a)')
    x2.image('Static/F7729A18-BC52-4EAA-88C5-4DB18468CC23.jpeg')

    y2.header('[Introduction to Data Science ](https://coursera.org/share/5375de8fd80e80ce446302f5547e900d)')
    y2.image('Static/6FC2BC47-C5DC-4879-BE51-EFA0B33D0E4C_1_105_c.jpeg')
    

    x2,y2=st.beta_columns(2)
    x2.header('[Introduction to Web Development](https://coursera.org/share/a0a8bf8c302439c3e1d655743617fd6d)')
    x2.image('Static/B8000BCC-D69C-40BF-AFF5-359631803A1A_1_105_c.jpeg')

    y2.header('[Machine Learning with Python](https://coursera.org/share/0e02b5a2cd78f594a6d373cda4ccb5e9)')
    y2.image('Static/1270125A-0969-477E-8E65-2FDF58D1AA10_1_105_c.jpeg')
    
    x2,y2=st.beta_columns(2)
    x2.header('[Data Analysis with python](https://coursera.org/share/956059eb0718c2863e3019a990985c0f)')
    x2.image('Static/67A08962-DE84-42E1-AD61-30E6FE1780E4_1_105_c.jpeg')

    y2.header('[Data Visulaization with python](https://coursera.org/share/a1bc327ad2b0dfd124368914c2aa48c5)')
    y2.image('Static/89E39C1B-A3A7-4B88-9862-02A09FFBFA16_1_105_c.jpeg')

    x2,y2=st.beta_columns(2)
    x2.header('[Databases and SQL](https://coursera.org/share/ce71284a2277da1556bcb6f52296cd6c)')
    x2.image('Static/9F58C5A9-E0E7-47ED-89F8-3A86F68699BC_1_105_c.jpeg')

    y2.header('[Python to Access Web Data](https://coursera.org/share/2130619a45880678c3d312c2d0d8c2b7)')
    y2.image('Static/CE96F3E4-ECBE-48EF-A2FE-27A7496BD30C_1_105_c.jpeg')

    x2,y2=st.beta_columns(2)
    x2.header('[Python Data Structures](https://coursera.org/share/606c0d43726500dd67f80061b92e55f0)')
    x2.image('Static/1D2A4266-CCC2-4323-9E20-5C8E0D23F581_1_105_c.jpeg')

    y2.header('[Getting Started with Python](https://coursera.org/share/787266dc51221f671e2261a91da592f4)')
    y2.image('Static/E05F607B-B8D9-47CC-9596-20EDE15F81B2_1_105_c.jpeg')
    
    st.header("Other")
