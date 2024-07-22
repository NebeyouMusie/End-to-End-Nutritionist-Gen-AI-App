from config import get_google_api_key, load_config
import google.generativeai as genai
from PIL import Image

load_config()
genai.configure(api_key=get_google_api_key())

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerationConfig('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# function to setup image input
def input_image_setup(uploaded_image):
    # check if a file has been uploaded
    if uploaded_image is not None:
        # read the file into bytes
        bytes_data = uploaded_image.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_image.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
     

