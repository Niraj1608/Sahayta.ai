import streamlit as st
import streamlit.components.v1 as components

def local_css():
    """
    Define custom CSS for the application with responsive design and accessibility improvements
    """
    st.markdown("""
    <style>
    /* Global Styling */
    body {
        font-family: 'Inter', sans-serif;
        background-color: #1e2127;
        color: white;
    }
    
    /* Responsive Container */
    .main > div {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1.5rem;
    }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #005C97, #363795);
        color: white;
        padding: 4rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        opacity: 0.9;
        max-width: 800px;
        margin: 0 auto;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Features Section */
    .features-container {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        flex: 1;
        background: rgba(54, 55, 149, 0.7);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .features-container {
            flex-direction: column;
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
    }
    
    /* Mission Section */
    .mission-section {
        background: rgba(54, 55, 149, 0.3);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    
    .mission-title {
        font-size: 2rem;
        text-align: center;
        margin-bottom: 1rem;
        color: #00B4DB;
    }
    
    .mission-description {
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Call to Action */
    .cta-section {
        background: linear-gradient(135deg, #005C97, #363795);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
    }
    
    .cta-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
    }
    
    .cta-button {
        padding: 0.8rem 1.5rem;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .cta-primary {
        background: #00B4DB;
        color: #1e2127;
    }
    
    .cta-secondary {
        background: transparent;
        color: #00B4DB;
        border: 2px solid #00B4DB;
    }
    </style>
    """, unsafe_allow_html=True)

def render_hero_section():
    """Render the hero section of the homepage"""
    st.markdown("""
    <div class="hero-container" aria-label="Sahayta.ai Homepage">
        <div class="hero-title">Sahayta.ai</div>
        <div class="hero-subtitle">
            Empowering Disaster Response with Artificial Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_features_section():
    """Render the features section"""
    st.markdown("""
    <div class="features-container">
        <div class="feature-card">
            <div class="feature-icon">🛰️</div>
            <div class="feature-title">Satellite Imagery Analysis</div>
            <p>Advanced AI models process satellite data to detect potential disaster zones.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌍</div>
            <div class="feature-title">Real-Time Monitoring</div>
            <p>Continuous tracking of environmental conditions and potential risks.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🚨</div>
            <div class="feature-title">Early Warning System</div>
            <p>Proactive alerts to help communities prepare and respond quickly.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_mission_section():
    """Render the mission section"""
    st.markdown("""
    <div class="mission-section">
        <div class="mission-title">Our Mission</div>
        <div class="mission-description">
            At Sahayta.ai, we are committed to revolutionizing disaster response through cutting-edge 
            artificial intelligence. Our mission is to provide timely, accurate, and actionable insights 
            that can save lives, protect communities, and minimize the impact of natural disasters.
        </div>
    </div>
    """, unsafe_allow_html=True)




def render_technology_architecture():
    """Render the updated technology architecture SVG"""
    
    # Title and introductory text in Streamlit's markdown format
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
            <div style="width: 100%; max-width: 1000px; background: #1e2127; padding: 1.5rem; border-radius: 15px; text-align: center;">
                <p style="color: #00B4DB; font-size: 24px; font-weight: bold; margin: 0;">Sahayta.ai Architecture</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


    # SVG content with centered positioning
    components.html("""
    <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
        <div style="width: 880px; margin: 0 auto;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 580" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: auto;">
                <!-- Background -->
                <rect width="880" height="580" fill="#1e2127" rx="20"/>
                
                <!-- Problem Boxes -->
                <g transform="translate(90, 50)">
                    <!-- [Rest of the SVG content remains the same] -->
                    <!-- Problem 1 -->
                <rect x="0" y="0" width="220" height="100" rx="10" fill="#363795" opacity="0.9"/>
                <text x="110" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold" font-family="sans-serif">Problem 1:</text>
                <text x="110" y="55" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Inaccurate Resource</text>
                <text x="110" y="75" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Allocation </text>
                
                <!-- Problem 2 -->
                <rect x="240" y="0" width="220" height="100" rx="10" fill="#363795" opacity="0.9"/>
                <text x="350" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold" font-family="sans-serif">Problem 2:</text>
                <text x="350" y="55" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">15+ Minutes Delay in</text>
                <text x="350" y="75" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Disaster Information </text>
                
                <!-- Problem 3 -->
                <rect x="480" y="0" width="220" height="100" rx="10" fill="#363795" opacity="0.9"/>
                <text x="590" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold" font-family="sans-serif">Problem 3:</text>
                <text x="590" y="55" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Limited Situational</text>
                <text x="590" y="75" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Awareness </text>
                </g>

               
                <!-- Solution Architecture -->
                <g transform="translate(40, 170)">
                    <!-- Input Sources -->
                    <g transform="translate(0, 40)">
                        <rect x="20" y="0" width="160" height="60" rx="8" fill="#005C97"/>
                        <text x="100" y="25" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Satellite Imagery</text>
                        <text x="100" y="45" text-anchor="middle" fill="white" font-size="12" font-family="sans-serif">(NOAA-20 VIIRS) 🛰️</text>

                        <rect x="20" y="80" width="160" height="60" rx="8" fill="#005C97"/>
                        <text x="100" y="105" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Drone Feed</text>
                        <text x="100" y="125" text-anchor="middle" fill="white" font-size="12" font-family="sans-serif">(Aerial Imagery) 📷</text>

                        <rect x="20" y="160" width="160" height="60" rx="8" fill="#005C97"/>
                        <text x="100" y="185" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">Flood Data</text>
                        <text x="100" y="205" text-anchor="middle" fill="white" font-size="12" font-family="sans-serif">(Semantic Maps) 🗺️</text>

                        <rect x="20" y="240" width="160" height="60" rx="8" fill="#005C97"/>
                        <text x="100" y="265" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">API Integrations</text>
                        <text x="100" y="285" text-anchor="middle" fill="white" font-size="12" font-family="sans-serif">(Weather & Routes) 🌐</text>
                    </g>
                    
                    <!-- AI Core -->
                    <g transform="translate(280, 40)">
                        <rect x="0" y="0" width="240" height="300" rx="10" fill="#00B4DB"/>
                        <text x="120" y="35" text-anchor="middle" fill="white" font-size="18" font-weight="bold" font-family="sans-serif">AI Core</text>
                        <text x="120" y="70" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Wildfire Detection 🔥</text>
                        <text x="120" y="100" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Flood Detection 🌊</text>
                        <text x="120" y="130" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Flood Mask &amp; Segmentation 🎯</text>
                        <text x="120" y="160" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Weather Prediction ⛈️</text>
                        <text x="120" y="190" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Route Optimization 🛣️</text>
                    </g>
                    
                    <!-- Output -->
                    <g transform="translate(620, 40)">
                        <rect x="0" y="0" width="160" height="300" rx="10" fill="#005C97"/>
                        <text x="80" y="35" text-anchor="middle" fill="white" font-size="18" font-weight="bold" font-family="sans-serif">Services</text>
                        <text x="80" y="70" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Real-time Alerts ⚡</text>
                        <text x="80" y="100" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Disaster Maps 📍</text>
                        <text x="80" y="130" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Optimal Routes 🛣️</text>
                        <text x="80" y="160" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Weather Updates 🌡️</text>
                        <text x="80" y="190" text-anchor="middle" fill="white" font-size="14" font-family="sans-serif">• Resource Plans 📋</text>
                    </g>
                    
                    <!-- Arrows -->
                    <g>
                        <line x1="180" y1="70" x2="280" y2="70" stroke="#00B4DB" stroke-width="2" marker-end="url(#arrowhead)"/>
                        <line x1="180" y1="150" x2="280" y2="150" stroke="#00B4DB" stroke-width="2" marker-end="url(#arrowhead)"/>
                        <line x1="180" y1="230" x2="280" y2="230" stroke="#00B4DB" stroke-width="2" marker-end="url(#arrowhead)"/>
                        <line x1="180" y1="310" x2="280" y2="310" stroke="#00B4DB" stroke-width="2" marker-end="url(#arrowhead)"/>
                        <line x1="520" y1="180" x2="620" y2="180" stroke="#00B4DB" stroke-width="2" marker-end="url(#arrowhead)"/>
                    </g>
                </g>

                <!-- Arrow Marker -->
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#00B4DB"/>
                    </marker>
                </defs>
            </svg>
        </div>
    </div>
    """ ,height=650)

def render_cta_section():
    """Render the call to action section"""
    st.markdown("""
    <div class="cta-section">
        <h2 style="margin-bottom: 1rem;">Join Our Mission</h2>
        <p style="max-width: 600px; margin: 0 auto 1.5rem; font-size: 1.1rem;">
            Together, we can build a more resilient world. Explore our tools, 
            learn about our technology, and help us make a difference.
        </p>
        <div class="cta-buttons">
            <a href="https://github.com/Niraj1608/Sahayta.ai/blob/main/README.md" class="cta-button cta-primary" aria-label="Learn More About Sahayta.ai">Learn More</a>
            <a href="https://www.linkedin.com/in/niraj-parmar-531b5523a/" class="cta-button cta-secondary" aria-label="Contact Sahayta.ai">Contact Us</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application entry point"""
    # Page Configuration
    st.set_page_config(
        page_title="Sahayta.ai - Home",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.example.com',
            'Report a bug': 'https://www.example.com',
            'About': 'https://www.example.com'
        }
    )

    # Apply custom CSS
    local_css()

    try:
        # Render Page Sections
        render_hero_section()
        render_features_section()
        render_mission_section()
        render_technology_architecture()
        render_cta_section()

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.error("Please refresh the page or contact support.")

if __name__ == "__main__":
    main()
