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
    set_png_as_page_bg('Static/achh.gif')

    st.header("CERTIFICATIONS")
    x2,y2,z2=st.beta_columns(3)
    x2.subheader('Data Analytics intern at KPMG')
    x2.image('Static/kpmg.png')

    y2.subheader('Data Analytics and Business Analytics intern at TSF')
    y2.image('Static/tsf.png')

    z2.subheader('Data Science and Machine Learning intern at Technocolabs')
    z2.image('Static/630C21E0-9B5C-4C03-9C06-CBC4F261E6A6_1_105_c.jpeg')

    x2,y2=st.beta_columns(2)
    x2.subheader('[Recruited at Aakash Research Labs](https://www.instagram.com/p/CLtsedijimo/?utm_medium=copy_link)')
    x2.image('Static/BC2DA83C-C474-4758-9864-52B32B9DF564.jpeg')

    y2.subheader('[Recruited at CodeChef SRM](https://www.linkedin.com/posts/ccscsrm_inspiration-activity-6763374002221187072-EYY7)')
    y2.image('Static/codechef.jpg')

    if st.button("HACKATHONS"):
        x2,y2,z2=st.beta_columns(3)
        x2.subheader('[Hacktrix-TOP 10](https://devfolio.co/submissions/aquaanalyst-327b)')
        x2.image('Static/hacktrix.png')

        y2.subheader('[E-HACK]')
        y2.image('Static/e-hack.png')

        z2.subheader('Frosthack')
        z2.image('Static/frosthack.png')


    if st.button("COURSES"):
        x2,y2,z2=st.beta_columns(3)
        x2.subheader('[Data Science Professional Certificate](https://coursera.org/share/d94fecaa44cfd428602697b950af7b3a)')
        x2.image('Static/F7729A18-BC52-4EAA-88C5-4DB18468CC23.jpeg')

        y2.subheader('[Introduction to Data Science ](https://coursera.org/share/5375de8fd80e80ce446302f5547e900d)')
        y2.image('Static/6FC2BC47-C5DC-4879-BE51-EFA0B33D0E4C_1_105_c.jpeg')
    
        z2.subheader('[Introduction to Web Development](https://coursera.org/share/a0a8bf8c302439c3e1d655743617fd6d)')
        z2.image('Static/B8000BCC-D69C-40BF-AFF5-359631803A1A_1_105_c.jpeg')

        x2,y2,z2=st.beta_columns(3)
        x2.subheader('[Machine Learning with Python](https://coursera.org/share/0e02b5a2cd78f594a6d373cda4ccb5e9)')
        x2.image('Static/1270125A-0969-477E-8E65-2FDF58D1AA10_1_105_c.jpeg')
    
        y2.subheader('[Data Analysis with python](https://coursera.org/share/956059eb0718c2863e3019a990985c0f)')
        y2.image('Static/67A08962-DE84-42E1-AD61-30E6FE1780E4_1_105_c.jpeg')

        z2.subheader('[Data Visulaization with python](https://coursera.org/share/a1bc327ad2b0dfd124368914c2aa48c5)')
        z2.image('Static/89E39C1B-A3A7-4B88-9862-02A09FFBFA16_1_105_c.jpeg')

        x2,y2,z2=st.beta_columns(3)
        x2.subheader('[Databases and SQL](https://coursera.org/share/ce71284a2277da1556bcb6f52296cd6c)')
        x2.image('Static/9F58C5A9-E0E7-47ED-89F8-3A86F68699BC_1_105_c.jpeg')

        y2.subheader('[Python to Access Web Data](https://coursera.org/share/2130619a45880678c3d312c2d0d8c2b7)')
        y2.image('Static/CE96F3E4-ECBE-48EF-A2FE-27A7496BD30C_1_105_c.jpeg')

        z2.subheader('[Python Data Structures](https://coursera.org/share/606c0d43726500dd67f80061b92e55f0)')
        z2.image('Static/1D2A4266-CCC2-4323-9E20-5C8E0D23F581_1_105_c.jpeg')

        x2,y2,z2=st.beta_columns(3)
        x2.subheader('[Getting Started with Python](https://coursera.org/share/787266dc51221f671e2261a91da592f4)')
        x2.image('Static/E05F607B-B8D9-47CC-9596-20EDE15F81B2_1_105_c.jpeg')
    
    
if rad== 'Technologies and Tools':
    
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
    set_png_as_page_bg('Static/tool.gif')
    
    html_temp="""
    <p>
    <div style="background:#ffffff;padding:10px">
    <h2 style="color:black;text-align:center;"> SKILLS : </h2>
    </div>
    </p>
    <h3 style="text-align:center;color:lightblue;">1. Data Science</h3>
    <h3 style="text-align:center;color:lightblue;">2. Data Analysis</h3>
    <h3 style="text-align:center;color:lightblue;">3. Machine Learning</h3>
    <h3 style="text-align:center;color:lightblue;">4. Deep Learning</h3>
    <h3 style="text-align:center;color:lightblue;">5. Web Development</h3>
    <h3 style="text-align:center;color:lightblue;">6. Business Analytics</h3>
    
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)

    html_temp="""
    <p>
    <div style="background:#ffffff;padding:10px">
    <h2 style="color:black;text-align:center;"> Languages and Tools: </h2>
    </div>
    </p>
    
    <p align="left"> <a href="https://www.cprogramming.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> 
    <a href="https://www.w3schools.com/cpp/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> 
    <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> 
    <a href="https://heroku.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> 
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
    <a href="https://www.mysql.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> 
    <a href="https://opencv.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a> 
    <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
    <a href="https://scikit-learn.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> 
    <a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> 
    <a href="https://www.tensorflow.org" target="_blank"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40
    </a> <a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a>
    </a> <a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> </p>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

   
    
