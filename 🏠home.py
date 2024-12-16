import streamlit as st
import requests
import pydeck as pdk
import base64
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
    
)

# Modern and Animated CSS
st.markdown("""
    <style>

    
    /* Main container styling */
    .main > div {
        padding: 1.5rem;
        max-width: 1200px;
        margin: 0 auto;
        font-family: 'Inter', sans-serif;
    }
    
    /* Card styling with subtle shadow */
    .stCard {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .stCard:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px -1px rgba(0, 0, 0, 0.1), 0 3px 6px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Header styling with vibrant gradient */
    .header-container {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #00B4DB, #0083B0);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: white;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        color: white;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* About section styling */
    .about-section {
        background: linear-gradient(135deg, #f6f9fc, #f1f4f8);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        animation: slideIn 0.8s ease-out;
    }
    
    .about-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Metric styling */
    .metric-container {
        background-color: white;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin-bottom: 0.8rem;
        transition: transform 0.2s ease;
    }
    
    .metric-container:hover {
        transform: translateY(-2px);
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #64748b;
        margin-bottom: 0.25rem;
        font-weight: 500;
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: #0083B0;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #00B4DB, #0083B0);
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        border: none;
        width: 100%;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #0083B0, #00B4DB);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transform: translateY(-1px);
    }
    
    /* Input field styling */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        padding: 0.6rem;
        transition: border-color 0.2s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #00B4DB;
        box-shadow: 0 0 0 2px rgba(0, 180, 219, 0.1);
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(135deg, #f6f9fc, #f1f4f8);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Success message styling */
    .element-container:has(.stSuccess) div {
        background-color: #10B981 !important;
        border-radius: 8px;
        animation: slideIn 0.5s ease-out;
    }

    /* Info message styling */
    .element-container:has(.stInfo) div {
        background-color: #0083B0 !important;
        border-radius: 8px;
        animation: slideIn 0.5s ease-out;
    }

    /* Warning message styling */
    .element-container:has(.stWarning) div {
        background-color: #F59E0B !important;
        border-radius: 8px;
        animation: slideIn 0.5s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

def get_weather(city_name):
    api_key = st.secrets["weather"]["api_key"]

    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    return response.json() if response.status_code == 200 else None

def get_coordinates(city_name):
    base_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    headers = {'User-Agent': 'SahaytaApp/1.0'}
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None, None

def generate_map(start_coords, end_coords=None):
    layers = []
    
    # Start location marker with improved styling
    layers.append(
        pdk.Layer(
            "ScatterplotLayer",
            data=[{"position": [start_coords[1], start_coords[0]], "color": [46, 204, 113], "radius": 350}],
            get_position="position",
            get_color="color",
            get_radius="radius",
            pickable=True,
        )
    )
    
    if end_coords:
        # Route layer with improved styling
        layers.append(
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
                get_color=[52, 152, 219],
                width_scale=2,
                width_min_pixels=3,
            )
        )
        # End location marker
        layers.append(
            pdk.Layer(
                "ScatterplotLayer",
                data=[{"position": [end_coords[1], end_coords[0]], "color": [231, 76, 60], "radius": 350}],
                get_position="position",
                get_color="color",
                get_radius="radius",
                pickable=True,
            )
        )

    view_state = pdk.ViewState(
        latitude=start_coords[0],
        longitude=start_coords[1],
        zoom=10,
        pitch=45,
    )
    
    return pdk.Deck(
        layers=layers,
        initial_view_state=view_state,
        map_style="light",
        tooltip={"text": "Location"},
    )

def main():
    # Header Section with animation
    st.markdown("""
        <div class="header-container">
            <div class="header-title"> Sahayta.ai </div>
            <div class="header-subtitle">Transforming Disaster Response Through AI</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    st.subheader("About This Application")
    st.markdown("""
    This application provides a user-friendly interface for analyzing wildfire risks 
    using cutting-edge machine learning models and satellite imagery. The goal is to 
    offer insights and predictions that assist in disaster management and mitigation efforts.
    - **Real-Time Monitoring:** Process satellite images to identify potential wildfire zones.
    - **Actionable Insights:** Inform disaster relief teams to plan and respond effectively.
    - **Technology-Driven:** Utilize advanced Deep Learning techniques for accurate predictions.
    """)
    st.divider()

    

    # Main content area
    col1, col2 = st.columns([1, 1])

    # Weather Information Section
    with col1:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("📍 Weather Monitor")
        city_name = st.text_input("Enter City Name:", placeholder="e.g., New Delhi", key="weather_city")
        
        if st.button("Get Weather Updates", key="weather_button"):
            if city_name:
                with st.spinner('Fetching weather data...'):
                    weather_data = get_weather(city_name)
                    if weather_data:
                        st.success(f"Current Weather in {city_name}")
                        
                        # Weather metrics in a grid
                        col1a, col1b = st.columns(2)
                        with col1a:
                            st.markdown("""
                                <div class="metric-container">
                                    <div class="metric-label">Temperature</div>
                                    <div class="metric-value">%d°C</div>
                                </div>
                            """ % weather_data['main']['temp'], unsafe_allow_html=True)
                            
                            st.markdown("""
                                <div class="metric-container">
                                    <div class="metric-label">Humidity</div>
                                    <div class="metric-value">%d%%</div>
                                </div>
                            """ % weather_data['main']['humidity'], unsafe_allow_html=True)
                        
                        with col1b:
                            st.markdown("""
                                <div class="metric-container">
                                    <div class="metric-label">Wind Speed</div>
                                    <div class="metric-value">%.1f m/s</div>
                                </div>
                            """ % weather_data['wind']['speed'], unsafe_allow_html=True)
                            
                            st.markdown("""
                                <div class="metric-container">
                                    <div class="metric-label">Conditions</div>
                                    <div class="metric-value">%s</div>
                                </div>
                            """ % weather_data['weather'][0]['description'].capitalize(), unsafe_allow_html=True)
                    else:
                        st.error("Unable to fetch weather data. Please check the city name.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Route Planning Section
    with col2:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("🗺️ Emergency Route Planner")
        
        start_location = st.text_input("Start Location:", placeholder="e.g., Mumbai", key="start_loc")
        destination_location = st.text_input("Destination:", placeholder="e.g., Pune", key="dest_loc")
        
        if st.button("Plan Emergency Route", key="route_button"):
            if start_location and destination_location:
                with st.spinner('Planning route...'):
                    start_coords = get_coordinates(start_location)
                    end_coords = get_coordinates(destination_location)
                    if start_coords and end_coords:
                        st.success(f"Emergency Route: {start_location} → {destination_location}")
                        map_deck = generate_map(start_coords, end_coords)
                        st.pydeck_chart(map_deck)
                        
                        st.info(f"""
                        📍 Start: {start_location} (Lat: {start_coords[0]:.4f}, Lon: {start_coords[1]:.4f})
                        🎯 End: {destination_location} (Lat: {end_coords[0]:.4f}, Lon: {end_coords[1]:.4f})
                        """)
                    else:
                        st.error("Could not locate one or both locations. Please check the names.")
            else:
                st.warning("Please enter both start and destination locations.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer with updated styling
    st.markdown("""
        <div class="footer">
            <h3>💡 Quick Tips</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div style="padding: 1rem; background: white; border-radius: 8px;">
                    <h4>📌 Location Tips</h4>
                    <p>Use specific city names for better accuracy</p>
                </div>
                <div style="padding: 1rem; background: white; border-radius: 8px;">
                    <h4>🌤️ Weather Updates</h4>
                    <p>Check conditions before planning routes</p>
                </div>
                <div style="padding: 1rem; background: white; border-radius: 8px;">
                    <h4>🔄 Regular Updates</h4>
                    <p>Data refreshes every 30 minutes</p>
                </div>
            </div>
            <p style="text-align: center; margin-top: 1.5rem; color: #64748b;">
               
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
