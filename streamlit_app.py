import streamlit as st

def main():
    st.title("Streamlit + Kivy Facial Verification App")

    # Embed the Kivy app as an iframe using HTML
    st.write('<iframe src="https://appapppy-vo46dnnbvkbjrtzelqxt4a.streamlit.app/" width=400 height=600 style="border:none;"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
