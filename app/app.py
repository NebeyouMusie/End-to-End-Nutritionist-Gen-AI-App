import streamlit as st
from PIL import Image
from utils import get_gemini_response, input_image_setup

st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
user_input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.")

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
"""

# Debugging statement to check if the submit button was clicked
print(f"Submit button clicked: {submit}")

if submit:
    image_data = input_image_setup(uploaded_file)
    print(f"Image data: {image_data}")  # Debugging statement to check the image data
    
    response = get_gemini_response(input_prompt, image_data, user_input)
    print(f"Response: {response}")  # Debugging statement to check the response
    
    st.subheader("The Response is")
    st.write(response)