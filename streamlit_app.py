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
            background: #000;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <iframe src="https://skybox.blockadelabs.com/e/a27b3cf0457413435fc4b313d73d320a" allow="fullscreen"></iframe>
</body>
</html>
"""

# Display the HTML content in Streamlit
components.html(html_content, height=800)
