import streamlit as st
import numpy as np
import time
from datetime import datetime
import random

# Page config
st.set_page_config(page_title="AI Pet World", layout="wide")

# Initialize game state
if 'pet_pos' not in st.session_state:
    st.session_state.pet_pos = {"x": 300, "y": 200}
if 'world_objects' not in st.session_state:
    st.session_state.world_objects = {
        'trees': [(100, 100), (500, 150), (200, 400)],
        'rocks': [(400, 300), (150, 250)],
        'toys': [(250, 200)],
        'food': [(350, 350)]
    }

# Custom CSS
st.markdown("""
    <style>
    .game-container {
        background: #f0f8ff;
        border-radius: 15px;
        padding: 10px;
        margin: 10px 0;
    }
    .stat-bar {
        height: 20px;
        border-radius: 10px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Create the game world SVG
def create_world():
    world_svg = f"""
    <svg width="600" height="400" viewBox="0 0 600 400">
        <!-- Sky gradient -->
        <defs>
            <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#E0F6FF;stop-opacity:1" />
            </linearGradient>
            <pattern id="grass" width="10" height="10" patternUnits="userSpaceOnUse">
                <path d="M0,0 L10,10 M-2,8 L2,12 M8,-2 L12,2" 
                      stroke="#90EE90" stroke-width="1" />
            </pattern>
        </defs>

        <!-- Background -->
        <rect width="600" height="400" fill="url(#skyGradient)" />
        <rect width="600" height="100" y="300" fill="url(#grass)" />

        <!-- Sun -->
        <circle cx="50" cy="50" r="30" fill="yellow" filter="url(#glow)">
            <animate attributeName="opacity" values="0.8;1;0.8" dur="3s" repeatCount="indefinite" />
        </circle>
        
        <!-- Trees -->
    """
    
    # Add trees
    for x, y in st.session_state.world_objects['trees']:
        world_svg += f"""
        <g transform="translate({x},{y})">
            <path d="M-20,0 L20,0 L0,-40 Z" fill="#228B22" />
            <path d="M-15,-30 L15,-30 L0,-60 Z" fill="#228B22" />
            <rect x="-5" y="0" width="10" height="20" fill="#8B4513" />
        </g>
        """

    # Add rocks
    for x, y in st.session_state.world_objects['rocks']:
        world_svg += f"""
        <path d="M{x},{y} Q{x+20},{y-20} {x+40},{y} T{x+80},{y}"
              fill="#808080" stroke="#666" />
        """

    # Add toys
    for x, y in st.session_state.world_objects['toys']:
        world_svg += f"""
        <circle cx="{x}" cy="{y}" r="10" fill="#FF69B4">
            <animate attributeName="transform" 
                     attributeType="XML"
                     type="rotate"
                     from="0 {x} {y}"
                     to="360 {x} {y}"
                     dur="4s"
                     repeatCount="indefinite"/>
        </circle>
        """

    # Add food bowls
    for x, y in st.session_state.world_objects['food']:
        world_svg += f"""
        <ellipse cx="{x}" cy="{y}" rx="15" ry="10" fill="#CD853F" />
        <ellipse cx="{x}" cy="{y-2}" rx="12" ry="8" fill="#DEB887" />
        """

    # Add AI Pet (more detailed)
    pet_x = st.session_state.pet_pos['x']
    pet_y = st.session_state.pet_pos['y']
    world_svg += f"""
        <!-- AI Pet -->
        <g transform="translate({pet_x},{pet_y})" class="pet">
            <!-- Body -->
            <ellipse cx="0" cy="0" rx="25" ry="20" fill="#4169E1" filter="url(#glow)">
                <animate attributeName="ry" 
                         values="20;22;20" 
                         dur="1s" 
                         repeatCount="indefinite" />
            </ellipse>
            
            <!-- Eyes -->
            <circle cx="-8" cy="-5" r="4" fill="white" />
            <circle cx="8" cy="-5" r="4" fill="white" />
            <circle cx="-8" cy="-5" r="2" fill="black">
                <animate attributeName="cy" 
                         values="-5;-4;-5" 
                         dur="2s" 
                         repeatCount="indefinite" />
            </circle>
            <circle cx="8" cy="-5" r="2" fill="black">
                <animate attributeName="cy" 
                         values="-5;-4;-5" 
                         dur="2s" 
                         repeatCount="indefinite" />
            </circle>
            
            <!-- Mouth -->
            <path d="M-10,5 Q0,15 10,5" stroke="black" fill="none" stroke-width="2">
                <animate attributeName="d" 
                         values="M-10,5 Q0,15 10,5;M-10,8 Q0,18 10,8;M-10,5 Q0,15 10,5" 
                         dur="3s" 
                         repeatCount="indefinite" />
            </path>
            
            <!-- Glow effect -->
            <animate attributeName="opacity" 
                     values="0.9;1;0.9" 
                     dur="2s" 
                     repeatCount="indefinite" />
        </g>
    </svg>
    """
    
    return world_svg

# Create the main layout
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("## 🌈 AI Pet World")
    # Display the game world
    st.markdown(f'<div class="game-container">{create_world()}</div>', unsafe_allow_html=True)
    
    # Movement controls
    move_cols = st.columns(4)
    with move_cols[1]:
        if st.button("⬆️"):
            st.session_state.pet_pos['y'] = max(50, st.session_state.pet_pos['y'] - 20)
    with move_cols[0]:
        if st.button("⬅️"):
            st.session_state.pet_pos['x'] = max(25, st.session_state.pet_pos['x'] - 20)
    with move_cols[2]:
        if st.button("➡️"):
            st.session_state.pet_pos['x'] = min(575, st.session_state.pet_pos['x'] + 20)
    with move_cols[1]:
        if st.button("⬇️"):
            st.session_state.pet_pos['y'] = min(350, st.session_state.pet_pos['y'] + 20)

with col2:
    st.markdown("### Pet Stats")
    energy = st.progress(0.8, "Energy")
    happiness = st.progress(0.9, "Happiness")
    hunger = st.progress(0.7, "Food")
    
    st.markdown("### Actions")
    if st.button("🎾 Play Fetch"):
        new_toy_x = random.randint(50, 550)
        new_toy_y = random.randint(50, 350)
        st.session_state.world_objects['toys'].append((new_toy_x, new_toy_y))
        st.experimental_rerun()

    if st.button("🍖 Add Food"):
        new_food_x = random.randint(50, 550)
        new_food_y = random.randint(50, 350)
        st.session_state.world_objects['food'].append((new_food_x, new_food_y))
        st.experimental_rerun()

    if st.button("🌳 Plant Tree"):
        new_tree_x = random.randint(50, 550)
        new_tree_y = random.randint(50, 350)
        st.session_state.world_objects['trees'].append((new_tree_x, new_tree_y))
        st.experimental_rerun()

# Add some ambient sounds
st.sidebar.markdown("### 🎵 Ambient Sounds")
st.sidebar.checkbox("Enable background music")
st.sidebar.checkbox("Enable sound effects")

# Weather effects
st.sidebar.markdown("### ⛅ Weather")
weather = st.sidebar.selectbox("Select Weather", 
    ["Sunny", "Rainy", "Snowy", "Rainbow"])

# Time of day
st.sidebar.markdown("### 🕒 Time of Day")
time_of_day = st.sidebar.select_slider("", 
    options=["Dawn", "Morning", "Noon", "Afternoon", "Dusk", "Night"])
