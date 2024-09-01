
import streamlit as st
import base64
from PIL import Image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Customize initial app landing page
st.set_page_config(page_title="Image QA Assistant", page_icon="🤖")
st.title("🤖 Welcome to the Image QA Assistant")

# Function to process uploaded images and generate base64 encoded strings
def process_uploaded_image(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        file_content = uploaded_file.getvalue()
        base64_image = base64.b64encode(file_content).decode('utf-8')
        return base64_image
    return None

# Initialize the AI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Image upload section
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file:
    base64_image = process_uploaded_image(uploaded_file)

    # Question input
    question = st.text_input("Ask a question about the image")

    # If a question is provided
    if st.button("Get Answer"):
        if base64_image and question:
            # Create a message with the image and question
            message = HumanMessage(
                content=[
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            )

            # Invoke the model with the message
            response = model.invoke([message])

            # Display the model's response
            st.write("Response:", response.content)
        else:
            st.write("Please upload an image and ask a question.")
