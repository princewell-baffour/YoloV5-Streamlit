import streamlit as st
from streamlit_option_menu import option_menu
from yolov5 import *
from yolov7 import *
from eda import *

def nav():
    #1. as slidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title= "AI Team 6",
            options = ["YoloV5", "YoloV7", "EDA"],
            icons=['binoculars', 'binoculars-fill','file-earmark-bar-graph'],
            menu_icon="bullseye", default_index=0
        )

    if selected == "YoloV5":
        yolov5()

    if selected == "YoloV7":
        yolov7()

    if selected == "EDA":
        EDA_Page()

    st.sidebar.subheader('Objects Detectable')
    st.sidebar.write("Strawberry flowers")
    st.sidebar.write("Unripe strawberry")
    st.sidebar.write("Duck")
    st.sidebar.write("Chicken")
    st.sidebar.write("Grapes")
    st.sidebar.write("Watermelon")