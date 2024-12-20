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

# CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .footer {
        background: #1e2127;
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        color: #ffffff;
    }
    .footer-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
    }
    .footer-card {
        background: #2a2d35;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .footer-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    .footer-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #00B4DB;
    }
    .footer-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .footer-text {
        font-size: 1rem;
        line-height: 1.5;
        color: #b3b3b3;
    }
    </style>
""", unsafe_allow_html=True)

# Helper Functions
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

# Main Sections
def weather_section():
    st.subheader("📍 Weather Monitor")
    city_name = st.text_input("Enter City Name:", placeholder="e.g., New Delhi")
    if st.button("Get Weather Updates"):
        if city_name:
            weather_data = get_weather(city_name)
            if weather_data:
                st.success(f"Current Weather in {city_name}")
                st.write(f"Temperature: {weather_data['main']['temp']}°C")
                st.write(f"Humidity: {weather_data['main']['humidity']}%")
                st.write(f"Conditions: {weather_data['weather'][0]['description'].capitalize()}")
            else:
                st.error("Unable to fetch weather data. Please check the city name.")

def route_section():
    st.subheader("🗺️ Emergency Route Planner")
    start_location = st.text_input("Start Location:", placeholder="e.g., Mumbai")
    destination_location = st.text_input("Destination:", placeholder="e.g., Pune")
    if st.button("Plan Emergency Route"):
        if start_location and destination_location:
            start_coords = get_coordinates(start_location)
            end_coords = get_coordinates(destination_location)
            if start_coords and end_coords:
                st.success(f"Emergency Route: {start_location} → {destination_location}")
                st.pydeck_chart(generate_map(start_coords, end_coords))
            else:
                st.error("Could not locate one or both locations. Please check the names.")

# Footer
def footer_section():
    st.markdown("""
        <div class="footer">
            <h3 style="text-align: left;">💡 Quick Tips</h3>
            <div class="footer-container">
                <div class="footer-card">
                    <div class="footer-icon">📌</div>
                    <div class="footer-title">Location Tips</div>
                    <div class="footer-text">Use specific city names for better accuracy.</div>
                </div>
                <div class="footer-card">
                    <div class="footer-icon">🌤️</div>
                    <div class="footer-title">Weather Updates</div>
                    <div class="footer-text">Check conditions before planning routes.</div>
                </div>
                <div class="footer-card">
                    <div class="footer-icon">🔄</div>
                    <div class="footer-title">Regular Updates</div>
                    <div class="footer-text">Data refreshes every 30 minutes.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    tab1, tab2 = st.tabs(["🌦️ Weather Monitor", "🗺️ Route Planner"])
    with tab1:
        weather_section()
    with tab2:
        route_section()
    footer_section()

if __name__ == "__main__":
    main()
