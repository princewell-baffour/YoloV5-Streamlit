import streamlit as st
from streamlit_option_menu import option_menu
from yolov5 import *
import webbrowser

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

    url = 'https://yolov7.streamlit.app/'

    if selected == "YoloV5":
        yolov5()

    if selected == "YoloV7":
        webbrowser.open_new_tab(url)

    if selected == "EDA":
        EDA_Page()

    st.sidebar.subheader('Objects Detectable')
    st.sidebar.write("Strawberry flowers")
    st.sidebar.write("Unripe strawberry")
    st.sidebar.write("Duck")
    st.sidebar.write("Chicken")
    st.sidebar.write("Grapes")
    st.sidebar.write("Watermelon")