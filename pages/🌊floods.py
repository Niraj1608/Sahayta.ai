import streamlit as st

st.set_page_config(page_title='Flood Segmentation', page_icon='🌊', initial_sidebar_state='expanded')

# Title and Introduction
st.title("Flood Segmentation and Analysis Model 🌊")
st.markdown("""
Natural disasters like floods have devastating impacts on lives and infrastructure. 
Our model leverages cutting-edge AI to analyze satellite imagery for effective flood masking and segmentation, 
enabling faster and more precise emergency response planning.
""")
st.divider()

# How It Works Section
st.subheader("How Does It Work?")
st.markdown("""
Using advanced deep learning techniques, specifically the **U-NET architecture**, 
our model performs semantic segmentation of satellite images to identify and analyze flood-affected areas accurately.
""")
st.divider()

# Technologies Section
st.subheader("Technologies Used")
st.markdown("""
- **Model:** U-NET Deep Learning Model  
- **Architecture Highlights:** Designed for semantic segmentation tasks with skip connections to capture spatial details.  
- **Accuracy:** Achieved an impressive **91.76%** segmentation accuracy.
""")
st.image('./assets/floods/model_plot.png', caption="U-NET Model Architecture")
st.divider()

# Results Section
st.subheader("Model Performance")
st.markdown("""
The model demonstrates exceptional performance in identifying flood-affected areas from satellite images. 
Below is an example of segmented outputs produced by the model:
""")
st.image('./assets/floods/output_flood_segmentation.png', caption="Flood Segmentation Results")
