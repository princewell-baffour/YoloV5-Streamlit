import streamlit as st
import torch
from detect import detect
from PIL import Image
from io import *
import glob
from datetime import datetime
import os
import wget
import time

## CFG
cfg_model_path = "models/best.pt" 


def imageInput():
    
    image_file = st.file_uploader("Upload An Image", type=['png', 'jpeg', 'jpg'])
    col1, col2 = st.columns(2)
    if image_file is not None:
        img = Image.open(image_file)
        with col1:
                st.image(img, caption='Uploaded Image', use_column_width='always')
        ts = datetime.timestamp(datetime.now())
        imgpath = os.path.join('data/uploads', str(ts)+image_file.name)
        outputpath = os.path.join('data/outputs', os.path.basename(imgpath))
        with open(imgpath, mode="wb") as f:
            f.write(image_file.getbuffer())

            #call Model prediction--
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=cfg_model_path, force_reload=True) 
            
        pred = model(imgpath)
        pred.render()  # render bbox in image
        for im in pred.ims:
            im_base64 = Image.fromarray(im)
            im_base64.save(outputpath)

            #--Display predicton
            
        img_ = Image.open(outputpath)
        with col2:
            st.image(img_, caption='Model Prediction(s)', use_column_width='always')




def videoInput():
    uploaded_video = st.file_uploader("Upload Video", type=['mp4', 'mpeg', 'mov'])
    if uploaded_video != None:

        ts = datetime.timestamp(datetime.now())
        imgpath = os.path.join('data/uploads', str(ts)+uploaded_video.name)
        outputpath = os.path.join('runs\detect\exp', os.path.basename(imgpath))

        with open(imgpath, mode='wb') as f:
            f.write(uploaded_video.read())  # save video to disk

        st_video = open(imgpath, 'rb')
        video_bytes = st_video.read()
        st.video(video_bytes)
        st.write("Uploaded Video")
        #detect(weights=cfg_model_path, source=imgpath, device=0) if device == 'cuda' else detect(weights=cfg_model_path, source=imgpath, device='cpu')
        detect(weights=cfg_model_path, source=imgpath)
        st_video2 = open(outputpath, 'rb')
        video_bytes2 = st_video2.read()
        st.video(video_bytes2)
        st.write("Model Prediction")


def main():
    # -- Sidebar
    st.sidebar.title('Options')
        
    source = ("Image Detection", "Video Detection")
    selection_index = st.sidebar.selectbox("Select input", range(
        len(source)), format_func=lambda x: source[x])

    st.sidebar.subheader('Objects Detectable')
    st.sidebar.write("Strawberry flowers")
    st.sidebar.write("Unripe strawberry")
    st.sidebar.write("Duck")
    st.sidebar.write("Chicken")
    st.sidebar.write("Grapes")
    st.sidebar.write("Watermelon")
    # -- End of Sidebar

    st.header('AI Project - Object Detection')
    st.subheader('Using YoloV5')
    if selection_index == 0:    
        imageInput()
    else:
        videoInput()

    

if __name__ == '__main__':
  
    main()
