import streamlit as st
import streamlit.components.v1 as components

# Initialize session state
if 'pet_state' not in st.session_state:
    st.session_state.pet_state = {
        'happiness': 80,
        'energy': 70,
        'food': 90,
        'position_x': 0,
        'position_z': 0
    }

# Page config
st.set_page_config(page_title="3D Pet World", layout="wide")

# Create the Three.js scene with communication back to Python
threejs_code = """
<div id="canvas-container" style="height: 500px; width: 100%;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    // Scene setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x87CEEB);

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 5, 10);

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('canvas-container').appendChild(renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
    directionalLight.position.set(0, 10, 5);
    scene.add(directionalLight);

    // Ground
    const groundGeometry = new THREE.PlaneGeometry(20, 20);
    const groundMaterial = new THREE.MeshStandardMaterial({color: 0x90EE90});
    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = -Math.PI / 2;
    scene.add(ground);

    // Pet
    const pet = new THREE.Group();
    
    // Body
    const bodyGeometry = new THREE.SphereGeometry(1, 32, 32);
    const bodyMaterial = new THREE.MeshPhongMaterial({color: 0x4169E1});
    const body = new THREE.Mesh(bodyGeometry, bodyMaterial);
    pet.add(body);

    // Eyes
    const eyeGeometry = new THREE.SphereGeometry(0.2, 16, 16);
    const eyeMaterial = new THREE.MeshPhongMaterial({color: 0xFFFFFF});
    const leftEye = new THREE.Mesh(eyeGeometry, eyeMaterial);
    const rightEye = new THREE.Mesh(eyeGeometry, eyeMaterial);
    leftEye.position.set(-0.4, 0.2, 0.8);
    rightEye.position.set(0.4, 0.2, 0.8);
    pet.add(leftEye);
    pet.add(rightEye);

    // Pupils
    const pupilGeometry = new THREE.SphereGeometry(0.1, 16, 16);
    const pupilMaterial = new THREE.MeshPhongMaterial({color: 0x000000});
    const leftPupil = new THREE.Mesh(pupilGeometry, pupilMaterial);
    const rightPupil = new THREE.Mesh(pupilGeometry, pupilMaterial);
    leftPupil.position.set(-0.4, 0.2, 0.9);
    rightPupil.position.set(0.4, 0.2, 0.9);
    pet.add(leftPupil);
    pet.add(rightPupil);

    scene.add(pet);

    // Animation variables
    let isJumping = false;
    let jumpHeight = 0;
    let bounceSpeed = 0.1;

    function jump() {
        isJumping = true;
        setTimeout(() => { isJumping = false; }, 500);
    }

    function movePet(x, z) {
        pet.position.x = x;
        pet.position.z = z;
    }

    function animate() {
        requestAnimationFrame(animate);

        // Bouncing animation
        if (isJumping) {
            jumpHeight += bounceSpeed;
            if (jumpHeight > 2) bounceSpeed = -0.1;
            if (jumpHeight < 0) {
                jumpHeight = 0;
                bounceSpeed = 0.1;
                isJumping = false;
            }
        }
        
        pet.position.y = jumpHeight + Math.sin(Date.now() * 0.003) * 0.1;
        pet.rotation.y = Math.sin(Date.now() * 0.001) * 0.2;

        renderer.render(scene, camera);
    }

    // Handle window resize
    window.addEventListener('resize', onWindowResize, false);
    function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    }

    animate();

    // Make functions available to Python
    window.jump = jump;
    window.movePet = movePet;
</script>
"""

# Layout
col1, col2 = st.columns([3,1])

with col1:
    st.title("🌈 3D Pet World")
    components.html(threejs_code, height=600)

    # Movement controls
    st.markdown("### Movement Controls")
    cols = st.columns(4)
    with cols[0]:
        if st.button("⬅️ Left"):
            st.session_state.pet_state['position_x'] -= 1
            st.experimental_rerun()
    with cols[1]:
        if st.button("⬆️ Forward"):
            st.session_state.pet_state['position_z'] -= 1
            st.experimental_rerun()
    with cols[2]:
        if st.button("⬇️ Back"):
            st.session_state.pet_state['position_z'] += 1
            st.experimental_rerun()
    with cols[3]:
        if st.button("➡️ Right"):
            st.session_state.pet_state['position_x'] += 1
            st.experimental_rerun()

with col2:
    # Stats
    st.markdown("### Pet Stats")
    happiness = st.progress(st.session_state.pet_state['happiness']/100, "Happiness")
    energy = st.progress(st.session_state.pet_state['energy']/100, "Energy")
    food = st.progress(st.session_state.pet_state['food']/100, "Food")

    # Actions
    st.markdown("### Actions")
    if st.button("🎾 Play"):
        st.session_state.pet_state['happiness'] = min(100, st.session_state.pet_state['happiness'] + 10)
        st.session_state.pet_state['energy'] = max(0, st.session_state.pet_state['energy'] - 5)
        st.write("Playing with pet!")
        st.experimental_rerun()
        
    if st.button("🍖 Feed"):
        st.session_state.pet_state['food'] = min(100, st.session_state.pet_state['food'] + 20)
        st.session_state.pet_state['happiness'] = min(100, st.session_state.pet_state['happiness'] + 5)
        st.write("Feeding pet!")
        st.experimental_rerun()

    if st.button("🦴 Treat"):
        st.session_state.pet_state['happiness'] = min(100, st.session_state.pet_state['happiness'] + 15)
        st.write("Gave pet a treat!")
        st.experimental_rerun()

# Inject JavaScript to update pet position
st.markdown(f"""
<script>
    if (window.movePet) {{
        window.movePet({st.session_state.pet_state['position_x']}, 
                      {st.session_state.pet_state['position_z']});
    }}
</script>
""", unsafe_allow_html=True)
