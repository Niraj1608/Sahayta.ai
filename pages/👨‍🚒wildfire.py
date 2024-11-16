import streamlit as st

st.set_page_config(page_title='Wildfire Detection', page_icon='🔥', initial_sidebar_state='expanded')

# Title and Introduction
st.title("Early Wildfire Detection System🔥")
st.markdown("""
Wildfires pose significant threats to ecosystems, property, and lives. 
Our solution leverages satellite imagery, particularly data from **NOAA-20 satellites (VIIRS)**, 
to detect wildfires at their earliest stages, enabling faster and more effective disaster response planning.
""")
st.divider()

# How It Works Section
st.subheader("How Does It Work?")
st.markdown("""
The system uses advanced **Deep Learning models (CNN)** to analyze satellite images. 
By identifying subtle changes in vegetation density and landscape patterns, 
the model can detect potential wildfire hotspots with remarkable precision.
""")
st.divider()

# Technologies Section
st.subheader("Technologies Used")
st.markdown("""
- **Model:** Pretrained **RESNET101** (with Transfer Learning to improve performance)  
- **Accuracy:** Achieved **90.5%** in identifying wildfire occurrences.  
- **Area Under Curve (AUC):** Scored an impressive **94.23%**, showcasing the model's robustness.  
- **Confusion Matrix:** A detailed visualization of classification performance:
""")
st.image('./assets/wildfire/confusion_mat.png', caption="Confusion Matrix for Wildfire Detection")
st.divider()

# Results Section
st.subheader("Model Performance")
st.markdown("""
The results highlight the model's ability to accurately identify wildfire zones 
from satellite imagery. Below is an example of predictions made by the system:
""")
st.image('./assets/wildfire/results.png', caption="Wildfire Detection Results")
