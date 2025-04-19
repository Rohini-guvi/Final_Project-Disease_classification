# Final_Project-Disease_classification
Diseases Detection and Diagnosis - Classification of Chest-X-ray images for diseases- Effusion, Nodule and Pneumothorax using Python and Deep Learning-Computer Vision.
YOLOv8n-cls is the pretrained model used for classifying Chest-X-ray images.

**Objective:**

The objective is to automate the diagnosis process and identify critical conditions among 14 chest diseases like Atelectasis,Fibrosis,Effusion, Mass and many other disases, across different patient demographics and imaging positions.
For this Project, Classification of 3 diseases- Effusion, Nodule and Pneumothorax is considered.

**Brief Description about chosen diseases:**

- Effusion- An abnormal collection of fluid between the lungs and chest wall
- Nodule- A small, abnormal growth within the lung tissue
- Pneumothorax- Air accumulation in the pleural space, the area between the lung and chest wall

**Code flow:**

Streamlit App is created for classifying the uploaded X-ray into 3 classes- Effusion, Nodule and Pneumothorax.
Below is the Streamlit App Page structure

app.py

|---------------Home.py

|---------------Preprocess.Py

|---------------Detect.py

**Attachments to the Repository:**
- app.py
- Home.py
- Preprocess.py
- Detect.py
- Data_temp.csv
- model.ipynb(colab file)
- best.pt for model YOLOv8n-cls
- best.pth for model YOLOv8n-cls
