from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Curriculum Vitae", page_icon=":scroll:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# load assets

lottie_coding = load_lottieurl("https://lottie.host/d800beee-9a8b-4a3b-90ca-03a73bbdcd12/kQBRubtMio.json")
lottie_javafx=load_lottieurl("https://lottie.host/3882b58c-56b9-4652-8304-0b6e32c08ead/UWdZorvfaP.json")
lottie_mysql=load_lottieurl("https://lottie.host/b327ccb5-a8fc-4ac1-8feb-728a1d64a7bd/WBepAzgF66.json")
lottie_cpp=load_lottieurl("https://lottie.host/0d15656b-3b60-4c69-921b-6402329e6cbb/WjQgGXoucP.json")
lottie_mobileapp=load_lottieurl("https://lottie.host/41e2b36e-845c-4f5d-97f6-0aeaed49d540/AICQ1iIQkz.json")
lottie_javalogo=load_lottieurl("https://lottie.host/4bb4b0fd-ec4b-4ce9-b06f-ef3fa59bb8dc/eTYIzw5a7r.json")
lottie_moto=load_lottieurl("https://lottie.host/b70f9512-b452-456f-a79f-30007d8deaae/GzHqdkO5IT.json")

# header section

with st.container():
    st.subheader("	:small_blue_diamond: Hi, I am Benjamin :small_blue_diamond:")
    st.title("Education")
  #  st.write("I am currently studying at the AGH University of Science and Technology, Faculty of Metals Engineering and Industrial Informatics, where I am majoring in Technical Informatics.")
  #  st.write("I am currently pursuing my degree at the AGH University of Science and Technology, Faculty of Metals Engineering and Industrial Informatics, specializing in Technical Informatics.")
    st.write("I am currently in my third year of studies at the AGH University of Science and Technology, Faculty of Metals Engineering and Industrial Informatics, specializing in Computer Science in Engineering.")


# what i do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
#I am currently pursuing a degree in Technical Computer Science.
#Alongside my studies, I am undertaking Java courses on javastart.pl and codegym.cc.

"""
Pursuing a degree in Computer Science in Engineering, I am enrolled in Java courses on javastart.pl and codegym.cc. 
Throughout my academic journey, I have developed several projects as part of the 'Window and Mobile Applications' course.

Beyond computer science, I have a keen interest in music.
I play guitar and piano, and enjoy composing my own music and arrangements.

I am actively seeking an internship opportunity within the IT industry.
"""
        )
    st.write("[Github profile >](https://github.com/benishhh)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# skills
with st.container():
    st.write("---")
    st.header("Skills")
    col1, col2, col3 = st.columns(3)

with col1:
    st_lottie(lottie_javalogo, height=100, key="codingjavalogo")

with col2:
    st_lottie(lottie_mysql, height=110, key="codingmysql")

with col3:
    st_lottie(lottie_cpp, height=100, key="codingcpp")


# projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    # Pierwszy projekt
    with st.expander("Classifieds Platform Inspired by Otomoto"):
        image_column, text_column = st.columns(2)

        with image_column:
            st_lottie(lottie_moto, height=400, key="codingmoto")

        with text_column:
            st.write(
                """
               "MOTOOTO" is a dynamic web application allowing users to add and browse classified ads, drawing inspiration from the popular platform Otomoto.
                Built using React and Typescript, the application leverages the Mantine library for efficient management of ads.
                Motooto offers users a clear and responsive interface for browsing and adding ads, ensuring a comfortable user experience.
               > React 

               > Typescript 
               
               >Mantine
                """
            )
            st.markdown("[Github repository...](https://github.com/benishhh/FrontendWebApp)")

        # Drugi projekt
    with st.expander("Teacher & Group Manager"):
        image_column, text_column = st.columns(2)

        with image_column:
            st_lottie(lottie_javafx, height=400, key="codingfx")

        with text_column:
            st.write(
                """
                Teacher & Group Manager is a user-friendly JavaFX application designed for schools and organizations to efficiently handle teacher and group management tasks. With MySQL Workbench and Hibernate integration, it simplifies administrative processes, making it easy to add, remove, and organize teachers and groups.
               > JavaFX 

               > MySQL Workbench 

               > Hibernate 
                """
            )
            st.markdown("[Github repository...](https://github.com/benishhh/JavaFXandHibernate1)")

    # Trzeci projekt
    with st.expander("BMI Calculator"):
        image_column, text_column = st.columns(2)

        with image_column:
            st_lottie(lottie_mobileapp, height=400, key="codingmobile")

        with text_column:
            st.write(
                """
                    The BMI Calculator is a simple mobile application designed to calculate Body Mass Index (BMI) effortlessly. 
                    Developed using Kotlin with Jetpack Compose, this app offers users a convenient way to assess their BMI and access relevant information.
               > Kotlin

               > Jetpack Compose

                 """
            )
            st.markdown("[Github repository...](https://github.com/benishhh/bmiApplication)")
