# Image QA Assistant using Multi-Model LLM (Gemini 1.5 Flash) and Streamlit Deployment

## Project Overview
This project implements an Image Question Answering (QA) system using the Gemini 1.5 Flash multi-modal large language model. The system is designed to understand images and generate answers to questions based on the content of those images. The model is deployed as a user-friendly web application using Streamlit, enabling users to upload images and interactively ask questions about them.

## Introduction
Image Question Answering (QA) is a challenging task that involves understanding and reasoning about visual content to generate accurate responses to questions related to the images. This project leverages the Gemini 1.5 Flash model, a state-of-the-art multi-modal large language model, to address this challenge. The model integrates visual and textual information, allowing it to process and answer questions based on images. The entire system is deployed using Streamlit, providing an easy-to-use web interface for end users.

## Model Overview
The Gemini 1.5 Flash model is a multi-modal large language model that can handle both visual and textual data. It combines deep learning techniques for image processing with natural language understanding, enabling it to perform tasks like image captioning, visual question answering, and more.

## Installation
To run this project, you will need Python 3.x installed along with the following libraries:

- langchain_google_genai
- langchain_core
- Streamlit
- pyngrok
- PIL
- base64

You can install the required packages using pip:
```bash
pip install langchain_google_genai langchain_core streamlit pyngrok PIL base64
