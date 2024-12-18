import streamlit as st

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

# CSS Styling for Dark Mode
st.markdown("""
    <style>
    /* Main container styling */
    .main > div {
        padding: 1.5rem;
        max-width: 1200px;
        margin: 0 auto;
        font-family: 'Inter', sans-serif;
        color: white;
    }
    
    /* Hero section styling */
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
    
    /* Features section styling */
    .features-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .feature-card {
        background: #1e2127;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #00B4DB;
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Mission section styling */
    .mission-section {
        background: linear-gradient(135deg, #363795, #005C97);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        text-align: center;
    }
    
    .mission-title {
        font-size: 2.5rem;
        color: #00B4DB;
        margin-bottom: 1rem;
    }
    
    .mission-description {
        max-width: 800px;
        margin: 0 auto;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Key Technologies Section */
    .tech-section {
        background: #1e2127;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        text-align: center;
    }
    
    .tech-title {
        font-size: 2.5rem;
        color: #00B4DB;
        margin-bottom: 1.5rem;
    }
    
    .tech-cards {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
    }
    
    .tech-card {
        background: #2b2d34;
        padding: 1rem 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .tech-card h3 {
        color: #00B4DB;
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
    </style>
""", unsafe_allow_html=True)

def main():
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Sahayta.ai</div>
        <div class="hero-subtitle">
            Empowering Disaster Response with Artificial Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Section
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
    
    # Mission Section
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
    
 
    
    # Call to Action
    st.markdown("""
    <div style="background: linear-gradient(135deg, #005C97, #363795); color: white; padding: 3rem 2rem; border-radius: 15px; margin-top: 2rem; text-align: center;">
        <h2 style="margin-bottom: 1rem;">Join Our Mission</h2>
        <p style="max-width: 600px; margin: 0 auto 1.5rem; font-size: 1.1rem;">
            Together, we can build a more resilient world. Explore our tools, 
            learn about our technology, and help us make a difference.
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem;">
            <a href="#" style="background: #00B4DB; color: #1e2127; padding: 0.8rem 1.5rem; text-decoration: none; border-radius: 8px; font-weight: bold;">Learn More</a>
            <a href="#" style="background: transparent; color: #00B4DB; padding: 0.8rem 1.5rem; text-decoration: none; border: 2px solid #00B4DB; border-radius: 8px; font-weight: bold;">Contact Us</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
