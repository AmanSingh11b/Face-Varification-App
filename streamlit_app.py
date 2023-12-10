import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

import streamlit as st
from streamlit.components.v1 import ComponentBase

class MyKivyApp(ComponentBase):
    def __init__(self):
        super().__init__(key="my_kivy_app")

    def render(self, **kwargs):
        from faceApp import CamApp  # Assuming your faceApp.py file contains the CamApp class
        CamApp().run()

def main():
    st.title("Streamlit + Kivy Facial Verification App")

    # Embed the Kivy app as a Streamlit component
    kivy_component = MyKivyApp()
    kivy_component

if __name__ == "__main__":
    main()
