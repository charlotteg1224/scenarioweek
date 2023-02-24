

import base64
import streamlit as st
from PIL import Image

#background image for Homepage
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('no.jpeg') 




def main():
    # Create a banner at the top with links to other pages
    with st.container():
        st.markdown(
            """
            <div style='background-color: white; padding: 1px;'>
            <h1 style='font-family:Optima;color: #8B4513; text-align: center;'>Jorge & Jeff</h1>
            <p style='font-family: Optima;color: #8B4513; text-align: center; font-size: 20px;'> 
            <a style='color: #8B4513; text-decoration: none;' href='https://charlotteg1224-scenarioweek-homepage-zb4jfq.streamlit.app/'target='_blank'>Home</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://ewanyeo-search-searchpage-ga2mq2.streamlit.app/'target='_blank'>Search</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://ewanyeo-readytowear-productspage-14irvc.streamlit.app/'target='_blank'>Ready To Wear</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://rajatk21-sw-doggy-pe2mzu.streamlit.app/' target='_blank'>Team</a> |
            <a style='color: #8B4513; text-decoration: none;' href='https://georginapalmer-contactus-streamlitcontactus-49oqai.streamlit.app/'target='_blank'>Contact</a> 
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
if __name__ == '__main__':
     main()

#images on Homepage 
image2 = Image.open('oui.jpeg')
st.image(image2)

image3 = Image.open('nony.jpeg')
st.image(image3)


def main():
    # Create a banner at the Bottom of Homepage, with text on Jorge & Jeff
    with st.container():
        st.markdown(
            """
            <div style='background-color: white; padding: 5px;'>
            <h1 style='font-family:Optima;color: #8B4513;font-size: 11px;text-align: center;'>At Jorge & Jeff, we are dedicated to providing high-quality, stylish clothing that empowers you to express yourself and feel confident. Our mission is to create timeless pieces that not only look great but also stand the test of time</h1>
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()

