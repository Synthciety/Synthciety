import streamlit as st

# Page config
st.set_page_config(page_title="AI Pet World", layout="wide")

# Initialize session state for pet stats
if 'happiness' not in st.session_state:
    st.session_state.happiness = 100
if 'food' not in st.session_state:
    st.session_state.food = 100

# Main title
st.title("🌈 AI Pet World")

# Create two columns
col1, col2 = st.columns([3,1])

with col1:
    # Simple pet display
    st.markdown("### Your Pet")
    st.markdown("🐾")  # Pet emoji placeholder
    
    # Basic controls
    if st.button("Move Left"):
        st.write("Moving left!")
    if st.button("Move Right"):
        st.write("Moving right!")

with col2:
    # Stats
    st.markdown("### Stats")
    st.progress(st.session_state.happiness/100, "Happiness")
    st.progress(st.session_state.food/100, "Food")
    
    # Actions
    st.markdown("### Actions")
    if st.button("🎾 Play Fetch"):
        st.session_state.happiness = min(100, st.session_state.happiness + 10)
        st.write("Playing fetch!")
    
    if st.button("🍖 Feed"):
        st.session_state.food = min(100, st.session_state.food + 20)
        st.write("Eating!")
