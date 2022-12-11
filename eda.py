
import streamlit as st
import os
from PIL import Image

def EDA_Page():
    st.header('Exploratory data analysis')

    data_path = 'dataset/'
    img_list = []
    labels = []
    count = 0

    # Fill in the labels & img_list lists
    for class_name in os.listdir(data_path):
        if class_name not in labels:
            labels.append(class_name)
        img_dir = data_path + class_name + "/"
        for img_filename in os.listdir(img_dir):
            img_path = img_dir + img_filename
            img_list.append([img_path, class_name])

    # Filter on the label part of the sublist (eg: [[img_path, label], ...]
    def get_filtered_list(filter: str, list: list = img_list):
        return [x[0] for x in list if x[1] == filter]

    # Calculate the average resolution for a given list of images
    def get_average_img_resolution(images: list):
        widths = []
        heights = []

        for img in images:
            im = Image.open(img)
            widths.append(im.size[0])
            heights.append(im.size[1])

        avg_width = round(sum(widths) / len(widths))
        avg_height = round(sum(heights) / len(heights))
        return [avg_width, avg_height]

    # --- Tabs ---
    tab1, tab2, tab3 = st.tabs(labels)

    # A tab for each of the labels
    for index, tab in enumerate([tab1, tab2, tab3]):
        with tab:
            images = get_filtered_list(labels[index])
            total_imgs = len(images)
            avg_w, avg_h = get_average_img_resolution(images)
            st.header(labels[index])
            st.write(f'Total Samples:  {total_imgs} ')
            st.write(f'Average Image Resolution: {avg_w}x{avg_h}')
            to_show = st.slider('Slide to adjust samples being displayed', 0, total_imgs,
                                15, key=count)
            st.image(images[:to_show], width=200)
            count += 1
