import streamlit as st
import requests
import pydeck as pdk

# Page Configuration
st.set_page_config(
    page_title="Sahayta.ai - Smart Relief",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling (using the same styling from the previous implementation)
st.markdown("""
    <style>
    /* [Previous CSS remains the same as in the original file] */
    </style>
""", unsafe_allow_html=True)

def get_weather(city_name):
    """Fetch weather data for a given city."""
    api_key = st.secrets["weather"]["api_key"]
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    return response.json() if response.status_code == 200 else None

def get_coordinates(city_name):
    """Get coordinates for a given city."""
    base_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    headers = {'User-Agent': 'SahaytaApp/1.0'}
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None, None

def generate_map(start_coords, end_coords=None):
    """Generate a map with route and location markers."""
    layers = []
    
    # Start location marker
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
        # Route layer
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

def weather_section():
    """Streamlit section for weather monitoring."""
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
                        st.markdown(f"""
                            <div class="metric-container">
                                <div class="metric-label">Temperature</div>
                                <div class="metric-value">{weather_data['main']['temp']}°C</div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            <div class="metric-container">
                                <div class="metric-label">Humidity</div>
                                <div class="metric-value">{weather_data['main']['humidity']}%</div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with col1b:
                        st.markdown(f"""
                            <div class="metric-container">
                                <div class="metric-label">Wind Speed</div>
                                <div class="metric-value">{weather_data['wind']['speed']} m/s</div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            <div class="metric-container">
                                <div class="metric-label">Conditions</div>
                                <div class="metric-value">{weather_data['weather'][0]['description'].capitalize()}</div>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("Unable to fetch weather data. Please check the city name.")
    st.markdown('</div>', unsafe_allow_html=True)

def route_section():
    """Streamlit section for emergency route planning."""
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

def main():
 
    
    st.divider()

    # Create tabs for different sections
    tab1, tab2 = st.tabs(["🌦️ Weather Monitor", "🗺️ Route Planner"])
    
    with tab1:
        weather_section()
    
    with tab2:
        route_section()

    # Footer with quick tips
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
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
