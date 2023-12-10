import os

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


import streamlit as st
from kivy.app import App
import numpy as np
from PIL import Image as PILImage

# Import your Kivy app
from faceApp import CamApp

def run_kivy_app():
    app = CamApp()  # Create an instance of your Kivy app
    app.run()

def main():
    st.title("Face Verification Streamlit App")  # Set the title of your Streamlit app

    # Add any Streamlit components or customizations here

    st.write("This is a Streamlit app that embeds a Kivy application.")
    st.write("The Kivy app is running below:")

    # Run your Kivy app within Streamlit
    run_kivy_app()

if __name__ == '__main__':
    main()
