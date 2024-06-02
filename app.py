from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey



# Initialize your image generation client
client=OpenAI(api_key=apikey)

# Funtion
def generate_images(image_description,num_image):

    img_response = client.images.generate(
    model="dall-e-3",
    prompt=image_description,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    return image_url

st.set_page_config(page_title="Dalle-Image-Generation",page_icon=":camera:",layout="wide")
st.title("Dalle-Image-Gen")
st.subheader("Wrold of Ai is Here")
img_description = st.text_input("Enter a Description for the image")
num_of_image = st.slider("Select the number of image you want to generate",1,10,1)

if st.button("Generate Images"):
    generate_image=generate_images(img_description,num_image=1)
    st.image(generate_image)