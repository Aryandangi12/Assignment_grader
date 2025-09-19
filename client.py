import streamlit as st
import requests
import json
import os
import tempfile
import time

st.set_page_config(
    page_title="Assignment Grader",
    page_icon="📝",
    layout="wide"
)

#main title
st.title("📄 Assignment Grader")
st.markdown("Upload assignment and grade them automatically with ai")

#side bar
st.sidebar.header("About")
st.sidebar.info("""
This is a demo of the Assignment Grader using FastMCP and OpenAI.  
Upload assignments in PDF or DOCX format, set your grading rubric,  
and get instant AI-powered grades with detailed feedback.
""")


#create tabs
tab1, tab2, tab3 = st.tabs(["Upload Assignment", "Grade Assignment", "Result"])
