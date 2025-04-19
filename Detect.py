import streamlit as st
from PIL import Image
import cv2
from ultralytics import YOLO
import pandas as pd
import os

class ImgDectection:

  def __init__(self,image):
    self.image= image
  
  def Img_Detect(self):
    strpath = "/content/drive/MyDrive/Final_Project/Prediction_results/"
      
    model = YOLO("/content/drive/MyDrive/Final_Project/yolov8n-cls-best.pt")

    pred =model.predict(source=image, conf=0.25,save=True, project=strpath)
    predicted=pred[0].probs.top1
    class_names = pred[0].names
    predicted_label = class_names[int(predicted)]
    res_list = pred[0].probs.top5
    conf_list = [class_names[int(i)] for i in res_list]

    # get the confidence score for the predicted class
    conf_score = [float(f"{conf:.2f}") for conf in pred[0].probs.top5conf.tolist()]

    # Create a mapping from class names to Confidence scores
    conf_map = pd.DataFrame({
      'Disease_Name' : conf_list,
      'Confidence Score':[conf_score[0],conf_score[1],conf_score[2]]
      })
    
    pred[0].save(filename= os.path.join(pred[0].save_dir,"result.png"))

    return predicted_label,conf_map,pred[0].save_dir

# Code for Streamlit app
st.text("Considered only image resizing to size 256x256 as Pre-processing technique for X-ray images as other techniques tend to lose some image features")

uploaded_file = st.file_uploader("Upload X-ray Image for Detection", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
  # Display the image
  image = Image.open(uploaded_file)

# Create a 1x2 grid using columns
row1 = st.columns(2)

Imdetect = ImgDectection(image)

predicted,conf_map,strpath = Imdetect.Img_Detect()

pred_path = os.path.join(strpath,"result.png")
result_image = Image.open(pred_path)
# Display images in each column
with row1[0]:
    image = image.resize((256,256))
    st.subheader("Resized Image")
    st.image(image)

with row1[1]:
    st.subheader("Predicted image")
    st.image(result_image)

st.write(f"Predicted Result: {predicted}")
st.write("\n Confidence Score:")
st.dataframe(conf_map)
