import streamlit as st
import requests
import pydeck as pdk
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Page Configuration
st.set_page_config(
    page_title="Sahayta.ai - Wildfire Risk Monitoring",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI
def load_custom_css():
    st.markdown("""
    <style>
    /* Main container styling */
    .main > div {
        padding: 1.5rem;
        max-width: 1400px;
        margin: 0 auto;
        font-family: 'Inter', sans-serif;
    }
    
    /* Modern card styling */
    .stCard {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }
    
    .stCard:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Dynamic gradient header */
    .header-container {
        background: linear-gradient(135deg, #ff6b6b, #ff4757);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Responsive metric cards */
    .metric-container {
        background-color: #f9fafb;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        transition: transform 0.2s;
    }
    
    .metric-container:hover {
        transform: scale(1.05);
    }
    
    .metric-label {
        color: #6b7280;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: #ff4757;
    }
    
    /* Responsive button styling */
    .stButton>button {
        background: linear-gradient(135deg, #ff6b6b, #ff4757);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)

# Utility Functions for API Calls
def get_weather(city_name):
    try:
        api_key = st.secrets.get("OPENWEATHER_API_KEY")
        if not api_key:
            st.error("Weather API key not configured")
            return None
        
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Weather API error: {e}")
        return None

def get_coordinates(city_name):
    try:
        base_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
        headers = {'User-Agent': 'SahaytaAI/1.0'}
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        return None, None
    except requests.exceptions.RequestException as e:
        logging.error(f"Geocoding API error: {e}")
        return None, None

def generate_route_map(start_coords, end_coords):
    if not start_coords or not end_coords:
        return None
    
    layers = [
        pdk.Layer(
            "ScatterplotLayer",
            data=[{"position": [start_coords[1], start_coords[0]], "color": [46, 204, 113]}],
            get_position="position",
            get_color="color",
            radius_scale=250,
        ),
        pdk.Layer(
            "LineLayer",
            data=[{
                "start_lat": start_coords[0],
                "start_lon": start_coords[1],
                "end_lat": end_coords[0],
                "end_lon": end_coords[1],
            }],
            get_source_position=["start_lon", "start_lat"],
            get_target_position=["end_lon", "end_lat"],
            get_color=[231, 76, 60],
            width_scale=3,
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=[{"position": [end_coords[1], end_coords[0]], "color": [231, 76, 60]}],
            get_position="position",
            get_color="color",
            radius_scale=250,
        )
    ]

    view_state = pdk.ViewState(
        latitude=(start_coords[0] + end_coords[0]) / 2,
        longitude=(start_coords[1] + end_coords[1]) / 2,
        zoom=6,
        pitch=40
    )

    return pdk.Deck(layers=layers, initial_view_state=view_state, map_style="mapbox://styles/mapbox/light-v10")

def main():
    # Load custom CSS
    load_custom_css()

    # Header
    st.markdown("""
    <div class="header-container">
        <div class="header-title">Sahayta.ai 🔥</div>
        <div class="header-subtitle">Intelligent Disaster Response and Risk Management</div>
    </div>
    """, unsafe_allow_html=True)

    # Application Overview
    st.markdown("""
    ### 🚨 Emergency Preparedness Platform
    
    Sahayta.ai is an advanced disaster response solution leveraging AI and real-time data to:
    - 🌍 Monitor environmental risks
    - 🚒 Plan emergency routes
    - 📊 Provide actionable insights
    """)

    # Columns for Weather and Route Planning
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("🌤️ Weather Monitor")
        
        city_name = st.text_input("Enter City Name", placeholder="e.g., New Delhi")
        
        if st.button("Get Weather Details"):
            with st.spinner("Fetching weather data..."):
                weather_data = get_weather(city_name)
                
                if weather_data:
                    st.success(f"Current Weather in {city_name}")
                    
                    col_temp, col_humid = st.columns(2)
                    with col_temp:
                        st.markdown(f"""
                        <div class="metric-container">
                            <div class="metric-label">Temperature</div>
                            <div class="metric-value">{weather_data['main']['temp']}°C</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_humid:
                        st.markdown(f"""
                        <div class="metric-container">
                            <div class="metric-label">Humidity</div>
                            <div class="metric-value">{weather_data['main']['humidity']}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.info(f"Conditions: {weather_data['weather'][0]['description'].capitalize()}")
                else:
                    st.error("Unable to retrieve weather data")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("🗺️ Emergency Route Planner")
        
        start_location = st.text_input("Start Location", placeholder="e.g., Mumbai")
        destination_location = st.text_input("Destination", placeholder="e.g., Pune")
        
        if st.button("Plan Emergency Route"):
            with st.spinner("Calculating route..."):
                start_coords = get_coordinates(start_location)
                end_coords = get_coordinates(destination_location)
                
                if start_coords[0] and end_coords[0]:
                    route_map = generate_route_map(start_coords, end_coords)
                    st.success("Emergency Route Generated")
                    st.pydeck_chart(route_map)
                    
                    st.markdown(f"""
                    **Route Details:**
                    - Start: {start_location} (Lat: {start_coords[0]:.4f}, Lon: {start_coords[1]:.4f})
                    - End: {destination_location} (Lat: {end_coords[0]:.4f}, Lon: {end_coords[1]:.4f})
                    """)
                else:
                    st.error("Unable to locate one or both locations")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer with tips and resources
    st.markdown("""
    ## 💡 Disaster Preparedness Tips
    
    1. **Stay Informed**: Monitor local weather and emergency channels
    2. **Have an Emergency Kit**: Include water, first-aid, and essential supplies
    3. **Create an Evacuation Plan**: Know multiple routes and meeting points
    4. **Stay Connected**: Keep communication devices charged
    """)

if __name__ == "__main__":
    main()
