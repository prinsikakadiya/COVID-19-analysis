import streamlit as st
from PIL import Image  

menu=["Patient","Vaccine","Overview"]

choice = st.sidebar.selectbox("Menu",menu)

if choice =='Patient':
    st.title('CORONA ANALYSIS')
    img = Image.open('./static/covid.jpg')
    st.image(img,use_column_width=True)

    col1, col2, col3 = st.columns(3)
    col1.error('hello1')
    col2.success('hello2')
    col3.warning('hello3')

elif choice =='Vaccine':
    st.subheader('vaccine information')

elif choice =='Overview':
    st.subheader('Overview of covid') 

#******

col1, col2 = st.columns(2)

original = Image.open('./static/covid.jpg')
col1.header("Original")
col1.image(original, use_column_width=True)

grayscale = original.convert('LA')
col2.header("Grayscale")
col2.image(grayscale, use_column_width=True)

#*******
# Create three columns of equal width
col1, col2, col3 = st.columns(3)

    # Container 1
with col1:
        st.subheader("Container 1")
        st.write("Content for Container 1")

    # Container 2
with col2:
        st.subheader("Container 2")
        st.write("Content for Container 2")

    # Container 3
with col3:
        st.subheader("Container 3")
        st.write("Content for Container 3")

       