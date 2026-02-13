import streamlit as st
import ui

st.set_page_config(layout="wide", page_title="AI YouTube Growth Advisor")

# Apply custom styling
ui.apply_custom_style()

# Header
ui.render_header()

# Input Form
submitted, niche, age, goal, content_type, upload_freq = ui.render_channel_form()

# Results
if submitted:
    # In a real app, you would process the inputs here to generate metrics
    # For now, we use the placeholder values as per original design
    ui.render_metrics(
        growth_momentum="▲ 12%",
        engagement_score="78/100",
        upload_consistency="Moderate"
    )
