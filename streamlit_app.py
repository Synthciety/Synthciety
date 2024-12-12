import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Synthciety - AI Simulated Environment", layout="wide")

# HTML content for the landing page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Synthciety - AI Simulated Environment</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            background: url('low-poly-bubble-render.jpg') no-repeat center center;
            background-size: cover;
        }
        #keyhole {
            width: 200px;
            height: 400px;
            background: url('keyhole.png') no-repeat center center;
            background-size: contain;
            cursor: pointer;
            animation: glow 1.5s infinite alternate;
        }
        @keyframes glow {
            from {
                box-shadow: 0 0 10px #fff;
            }
            to {
                box-shadow: 0 0 20px #fff;
            }
        }
    </style>
</head>
<body>
    <div id="keyhole"></div>
    <script>
        document.getElementById('keyhole').addEventListener('click', () => {
            window.location.href = 'interactive_scene.html';
        });
    </script>
</body>
</html>
"""

# Display the HTML content in Streamlit
components.html(html_content, height=800)
