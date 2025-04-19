from PIL import Image
import streamlit as st

st.title("**Diseases Detection and Diagnosis**")

st.subheader("Objective:")

st.write("The objective is to automate the diagnosis process and identify critical conditions such as Effusion, Nodule and Pneumothorax, across different patient demographics and imaging positions.")

st.subheader("Brief Description about chosen diseases:")

st.text("-- Effusion- An abnormal collection of fluid between the lungs and chest wall")

st.text("-- Nodule- A small, abnormal growth within the lung tissue")

st.text("-- Pneumothorax- Air accumulation in the pleural space, the area between the lung and chest wall")

# Create a 1x3 grid using columns
row1 = st.columns(3)

eff_img = Image.open("/content/drive/MyDrive/Final_Project/effusion.jpg")
nod_img = Image.open("/content/drive/MyDrive/Final_Project/nodule.jpg")
pneumo_img = Image.open("/content/drive/MyDrive/Final_Project/pneumothorax.jpg")

# Display images in each column
with row1[0]:
    st.subheader("Effusion")
    st.image(eff_img)

with row1[1]:
    st.subheader("Nodule")
    st.image(nod_img)

with row1[2]:
    st.subheader("Pneumothorax")
    st.image(pneumo_img)
