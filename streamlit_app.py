import streamlit as st
from streamlit.components.v1 import components

def main():
    st.title("Streamlit + Kivy Facial Verification App")

    # Embed the Kivy app as an iframe
    components.iframe("http://localhost:8080", height=600, width=400, scrolling=True)

if __name__ == "__main__":
    main()
