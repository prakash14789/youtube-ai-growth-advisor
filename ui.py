import streamlit as st

def apply_custom_style():
    """Applies custom CSS styles to the Streamlit app."""
    # Hide Streamlit default UI
    hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Animated Background + Glassmorphism + Other Custom Styles
    st.markdown("""
    <style>
    body {
        background: linear-gradient(-45deg, #0f172a, #1e293b, #111827, #0f172a);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .title {
        text-align: center;
        font-size: 60px;
        font-weight: bold;
        background: linear-gradient(90deg, #6366f1, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 30px;
        text-shadow: 0px 0px 20px rgba(99, 102, 241, 0.5); /* Glowing text effect */
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        opacity: 0.8;
        margin-bottom: 40px;
        color: #cbd5e1;
    }

    .glass {
        background: rgba(255, 255, 255, 0.05); /* Slightly more transparent */
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1); /* Subtle border for glass effect */
        margin-bottom: 20px;
    }

    /* Streamlit Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #6366f1, #06b6d4);
        color: white;
        border: none;
        border-radius: 12px;
        height: 3em;
        font-size: 18px;
        font-weight: 600;
        transition: transform 0.2s, box-shadow 0.2s;
    }

    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
    }

    /* Selectbox Styling */
    div[data-baseweb="select"] > div {
        background-color: rgba(30, 41, 59, 0.8);
        color: white;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    label {
        color: #e2e8f0 !important;
        font-weight: 500;
    }
    
    /* Fix Dropdown/Popover Z-Index and Styling */
    div[data-baseweb="popover"] {
        z-index: 2000 !important;
    }
    
    div[data-baseweb="menu"] {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1);
    }

    div[data-baseweb="select"] > div:first-child {
        background-color: rgba(30, 41, 59, 0.8);
        color: white;
        border-color: rgba(255,255,255,0.1);
    }
    
    /* Ensure the dropdown list items are visible */
    li[data-baseweb="menu-item"] {
        color: white !important;
    }
    li[data-baseweb="menu-item"]:hover {
        background-color: #334155 !important;
    }
    
    li[data-baseweb="menu-item"]:hover {
        background-color: #334155 !important;
    }
    
    /* Base state for the dropdown arrow */
    div[data-baseweb="select"] svg {
        transition: transform 0.2s ease;
        transform: rotate(0deg);
    }

    /* Rotate dropdown arrow when open */
    div[data-baseweb="select"] div[aria-expanded="true"] svg {
        transform: rotate(180deg);
    }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Renders the application header."""
    st.markdown("<div class='title'>🚀 AI YouTube Growth Advisor</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Your Personal AI Growth Strategist for YouTube 📈</div>", unsafe_allow_html=True)

def start_glass_div():
    """Starts a glassmorphism container div."""
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

def end_glass_div():
    """Ends a glassmorphism container div."""
    st.markdown("</div>", unsafe_allow_html=True)

def render_metrics(growth_momentum, engagement_score, upload_consistency):
    """Renders the metrics section."""
    st.markdown("<br>", unsafe_allow_html=True)
    start_glass_div()
    st.subheader("📊 Channel Profile")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Growth Momentum", growth_momentum, "Upward trend")
    with col2:
        st.metric("Engagement Score", engagement_score, "+4")
    with col3:
        st.metric("Upload Consistency", upload_consistency, "Needs improvement")
        
    st.success("🔥 AI Strategy Engine Coming Next...")
    end_glass_div()

def render_channel_form():
    """Renders the channel information input form inside a glass container."""
    start_glass_div()
    
    with st.form("channel_info_form"):
        col1, col2 = st.columns(2)

        with col1:
            selected_niche = st.selectbox("Channel Niche",
                ["Gaming","Finance","Tech","Education","Food","Vlogs","Fitness","Other"])

            if selected_niche == "Other":
                niche = st.text_input("Enter your custom niche", placeholder="e.g. ASMR, Coding...")
            else:
                niche = selected_niche

            audience_age = st.selectbox("Target Audience",
                ["13-18","18-25","25-40","40+"])

            primary_goal = st.selectbox("Primary Goal",
                ["Subscribers","Views","Revenue","Brand Deals"])

        with col2:
            content_type = st.selectbox("Content Type",
                ["Shorts","Long Videos","Both"])

            upload_frequency = st.selectbox("Upload Frequency",
                ["Daily","3-4/week","Once/week","Rarely"])

        submitted = st.form_submit_button("Generate AI Strategy")

    end_glass_div()
    
    return submitted, niche, audience_age, primary_goal, content_type, upload_frequency
