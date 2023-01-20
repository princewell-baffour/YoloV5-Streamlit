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
from pathlib import Path

os_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def yolov5():
    ## CFG
    cfg_model_path = "models/yolov5best.pt" 


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
            vidpath = os.path.join('data/uploads', str(ts)+uploaded_video.name)
            file_name = str(ts)+uploaded_video.name
            outputpath = os.path.join('exp', os.path.basename(file_name))
            #outputpath = os.path.join('/run/detect/exp/', os.path.basename(file_name))

            

            with open(vidpath, mode='wb') as f:
                f.write(uploaded_video.read())  # save video to disk

            st_video = open(vidpath, 'rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Uploaded Video")
            #detect(weights=cfg_model_path, source=imgpath, device=0) if device == 'cuda' else detect(weights=cfg_model_path, source=imgpath, device='cpu')
            detect(weights=cfg_model_path, source=vidpath)
            #print("Files:", os.listdir("runs/detect/exp"))

            #convert_vid = os.path.join('runs/detect/exp', str(ts)+'converted_video.mp4')
            #os.system('ffmpeg -i {} -vcodec libx264 {}'.format(outputpath, convert_vid))

            st_video2 = open(outputpath, 'rb')
            video_bytes2 = st_video2.read()
            st.video(video_bytes2)

            
           
            st.write("Model Prediction")
            print("Output path:", outputpath)
            print("Uploaded video path:",vidpath)



    st.header('Project 4.0  - Yolov8 Model')
    st.subheader('YOLOv8 Model Trained on our Custom Dataset(Strawberry)')
    st.title('Options')
        
    source = ("Image Detection", "Video Detection")
    selection_index = st.selectbox("Select input", range(
        len(source)), format_func=lambda x: source[x])


    
    if selection_index == 0:    
        imageInput()
    else:
        videoInput()

