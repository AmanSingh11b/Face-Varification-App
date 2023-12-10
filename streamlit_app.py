import streamlit as st

def main():
    st.title("Streamlit + Kivy Facial Verification App")

    # Embed the Kivy app as an iframe
    st.frame("kivy_frame", src="http://localhost:8080", height=600, width=400)

if __name__ == "__main__":
    main()
