import lanchain_helper as lch
import streamlit as st


st.image('./namakarana_logo.png',width=100,output_format="webp")
st.title("AI Baby Namkarana")
st.write('An ai powered bot with the da-vinci generative text generative model to list Indian names based on the vibe. Here vibe refers to the attribute and features of the particular gender selected name. This project is developed under general license and is crafted with love by vignesh.')
user_animal_type = st.selectbox("What is your baby's gender?", ("Boy","Girl"))
#cat---------------------cat--------------cat
if user_animal_type == "Boy":
    pet_color = st.text_area(label="Type name vibe do you want for your baby boy and hit ctrl + enter ", max_chars=50)
#Dog---------------------Dog--------------Dog
if user_animal_type == "Girl":
    pet_color = st.text_area(label="Type name vibe do you want for your baby girl and hit ctrl + enter", max_chars=50)

#----------------------------------------------------------------------------------

if pet_color:
    response = lch.generate_pet_name(user_animal_type,pet_color)
    st.text(response['pet_name'])