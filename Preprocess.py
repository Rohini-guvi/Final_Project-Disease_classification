import streamlit as st
from PIL import Image,ImageFilter,ImageEnhance

class ImgPreprocessing:
  def __init__(self,image):
    self.image= image

  def Img_Contrast(self,new_con):
    # Enhance Contrast 
    curr_con = ImageEnhance.Contrast(self.image) 
    img_contrasted = curr_con.enhance(new_con)
    return img_contrasted

  def Edge_Detect(self):
    edges = self.image.filter(ImageFilter.FIND_EDGES)
    return edges

  def Img_Resize(self,imgsize):
    resize_img = self.image.resize(imgsize)
    return resize_img,resize_img.size

  def Img_Blur(self):
    blur_img = self.image.filter(ImageFilter.GaussianBlur(2))
    return blur_img

# Code for Streamlit app
uploaded_file = st.file_uploader("Upload X-ray Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
  # Display the image
  image = Image.open(uploaded_file)
  st.image(image, caption='Original Image')

  # To read file as bytes:
  bytes_data = uploaded_file.getvalue()
  img_shape = image.size
  st.write(f"Image size: {len(bytes_data)} bytes")
  st.write(f"Image shape: {img_shape}")

    
image = Image.open(uploaded_file)
Imprep = ImgPreprocessing(image)

# Create a 2x2 grid using columns
row1 = st.columns(2)
row2 = st.columns(2)

contrast_image = Imprep.Img_Contrast(0.3)
resize_image,newsize = Imprep.Img_Resize((224,224))
blur_image = Imprep.Img_Blur()
edge_image = Imprep.Edge_Detect()

# Display images in each column
with row1[0]:
    st.subheader("Resized Image")
    st.image(resize_image)
    st.write(f"New size: {newsize}")

with row1[1]:
    st.subheader("Contrast Image")
    st.image(contrast_image)

with row2[0]:
    st.subheader("Edge Detections")
    st.image(edge_image)

with row2[1]:
    st.subheader("Blurred Image")
    st.image(blur_image)