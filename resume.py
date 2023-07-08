import streamlit as st
from PIL import Image, ImageOps, ImageDraw
from pro_cer.Project_details import project_selection
from pro_cer.Cert_details import cert_sel
import urllib.request

st.set_page_config(layout='wide')
mypic = "images/Untitled.jpg"

st.cache_data()
def resume():
    url = "https://docs.google.com/document/d/1XaEmEM2QvrLmQshrmBoPitc7vNCYZLmpPAR-ofbbAX0/export?format=pdf"

    res = urllib.request.urlopen(url)
    pdf_data = res.read()
    st.download_button(label="Nataraj_Palanivel_Resume", data=pdf_data, file_name="Nataraj_Palanivel_Resume.pdf", mime="application/pdf")

def add_circle_frame(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))

    # Create circular mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    # Apply circular mask to the image
    circular_image = ImageOps.fit(resized_image, mask.size, centering=(0.5, 0.5))
    circular_image.putalpha(mask)

    return circular_image
#st.write(f"### Resume first version")

col1, col3 = st.columns([2.5, 7])

with col1:

    circular_image = add_circle_frame(mypic, 450, 390)
    st.image(circular_image)
    #st.write("<h4 style='text-align: center; color: orange;'>NATARAJ PALANIVEL</h4>", unsafe_allow_html=True)

with col3:
    st.markdown("""<div style='text-align: center;'>
<h2 style=' color: #2d89f2;'>NATARAJ PALANIVEL</h2></div>""", unsafe_allow_html=True)
    #st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("""<div style='text-align: center;'>
<p style='font-size: 18px; text-align: justify; text-justify: inter-word;'>
I am An Aspiring Data Engineer With Strong Problem-Solving Aptitude For Designing <strong>Efficient Data Pipelines, 
Optimize Query Performance and Create Robust Data Models</strong>.Driven by a passion for delivering high-quality data solutions, 
while learning new <strong>emerging trends and technologies</strong> in the field of data engineering.
I am enthusiastic about leveraging my skills to contribute to the success of <strong>data-driven 
initiatives</strong> and make a meaningful <strong>impact.</strong>
.
</p></div>""", unsafe_allow_html=True)

#########################################
    docl,colg1, colg2,colg3 = st.columns([2,3.5,3,3])

    # GitHub link
    github_link = "#### [GitHub](https://github.com/pnraj)"
    colg1.markdown(github_link)

    # LinkedIn link
    linkedin_link = "#### [LinkedIn](https://www.linkedin.com/in/nataraj-palanivel-057085144/)"
    colg2.markdown(linkedin_link)

    colg3.markdown("""<div style='text-align: center;'>
<h4 style=' color: #2d89f2;'>pnrajk@gmail.com</h4></div>""", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)
lcol,rcol = st.columns([2.5,7])

with lcol:
    st.markdown('<br>', unsafe_allow_html=True)
    st.write("#### :blue[TECHNICAL-SKILLS]")
    ycol1, ycol2 = st.columns(2)
    with ycol1:
    
        st.write("<p style='font-size: 18px;'>Python</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>Mysql</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>MongoDB</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>Docker</p>", unsafe_allow_html=True)
    with ycol2:        
        st.write("<p style='font-size: 18px;'>Apache Spark</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>Airflow</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>AWS</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>DataBricks</p>", unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    ##########################
    st.write("#### :blue[WORK EXPREIENCE]")
    Ecol1, Ecol2 = st.columns([6,3])
    with Ecol1:
        st.write("<p style='font-size: 18px;'>Civil Engineer(Freelancer)</p>", unsafe_allow_html=True)
    with Ecol2:
        st.write("<p style='font-size: 18px;'>2017-2022</p>", unsafe_allow_html=True)                

    st.markdown('<hr>', unsafe_allow_html=True)

    ##########################
    st.write("#### :blue[EDUCATIONS]")
    acol1,acol, acol2 = st.columns([4.5,1.4,2.5])
    with acol1:
        #st.markdown('<br>', unsafe_allow_html=True) 
        st.write("<p style='font-size: 18px;'>BE-Civil Engineering</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>HSC - State Board </p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>SSLC - Matriculation</p>", unsafe_allow_html=True)
    with acol:
        st.write("<p style='font-size: 18px;'>70%</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>76.4%</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>86.2%</p>", unsafe_allow_html=True)
    with acol2:
        st.write("<p style='font-size: 18px;'>2013-2017</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>2011-2013</p>", unsafe_allow_html=True)
        st.write("<p style='font-size: 18px;'>2010-2011</p>", unsafe_allow_html=True)
    

with rcol:

    sncol1, sncol2 = st.columns([3,9])
    with sncol1:
        st.markdown('<br>', unsafe_allow_html=True) 
        st.write("#### :blue[PROJECTS TITLE:-]")
    
    with sncol2:
        prlist = ['API TO RDS USING LAMBDA WITH SLACK ERROR MONITORING', 'SPARK-ENABLED EXTRACTION AND LOADING INTO AWS RDS',
                  'PhonePe Pulse Data Analysis 2018-2022','Twitter Scraping','YouTube Data Harvesting and Warehousing'
                  ]
        sel = prlist.index("API TO RDS USING LAMBDA WITH SLACK ERROR MONITORING")
        selected_pr = st.selectbox("", prlist, index=sel)
    
    #st.markdown('<hr>', unsafe_allow_html=True)
    project_selection(selected_pr)
    st.markdown('<br>', unsafe_allow_html=True) 
    dum1,resc,resc1 = st.columns([3,5,4])
    resc.write(f"###### :blue[Click The Button to Download My Resume:]")
    with resc1:
        resume()
st.markdown('<hr>', unsafe_allow_html=True)     

st.markdown("""<div style='text-align: center;'>
<h4 style=' color: #2d89f2;'>CERTIFICATION</h4></div>""", unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)  
#st.write("#### :blue[CERTIFICATION:-]")
cert_sel()

