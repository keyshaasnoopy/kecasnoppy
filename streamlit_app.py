import streamlit as st

st.title("aku sayang snoppy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("a5aa66feb1115140297b638bc1876240.jpg", width=200)




st.title("aplikasi sederhana") 
st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("tulis sebuah angka:" , value=0, step=1)

if (angka % 2) == 0:
    st write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")
    
