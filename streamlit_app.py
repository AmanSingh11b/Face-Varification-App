import streamlit as st

def main():
    st.title("Streamlit + Kivy Facial Verification App")

    # Embed the Kivy app as an iframe using HTML
    st.markdown('<iframe src="http://localhost:8080" width=400 height=600 style="border:none;"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
