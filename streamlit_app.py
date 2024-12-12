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
        #start-button {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 10px 20px;
            font-size: 20px;
            background-color: #fff;
            border: none;
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
        iframe {
            width: 100%;
            height: 100%;
            border: none;
            display: none;
        }
        .clickable-object {
            position: absolute;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <button id="start-button">Start</button>
    <iframe id="skybox-iframe" src="https://skybox.blockadelabs.com/e/a27b3cf0457413435fc4b313d73d320a" allow="fullscreen"></iframe>
    <div class="clickable-object" id="object1" style="top: 30%; left: 40%; width: 50px; height: 50px;"></div>
    <div class="clickable-object" id="object2" style="top: 60%; left: 70%; width: 50px; height: 50px;"></div>
    <div class="clickable-object" id="object3" style="top: 20%; left: 20%; width: 50px; height: 50px;"></div>
    <div class="clickable-object" id="object4" style="top: 50%; left: 80%; width: 50px; height: 50px;"></div>
    <script>
        document.getElementById('start-button').addEventListener('click', () => {
            document.getElementById('start-button').style.display = 'none';
            document.getElementById('skybox-iframe').style.display = 'block';
        });

        document.getElementById('object1').addEventListener('click', () => {
            alert('You clicked on object 1!');
        });

        document.getElementById('object2').addEventListener('click', () => {
            alert('You clicked on object 2!');
        });

        document.getElementById('object3').addEventListener('click', () => {
            alert('You clicked on object 3!');
        });

        document.getElementById('object4').addEventListener('click', () => {
            alert('You clicked on object 4!');
        });
    </script>
</body>
</html>
"""

# Display the HTML content in Streamlit
components.html(html_content, height=800)
