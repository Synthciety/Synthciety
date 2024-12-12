import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="3D Pet World", layout="wide")

# Custom HTML with Three.js
threejs_code = """
<div id="canvas-container" style="height: 500px; width: 100%;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    // Set up scene
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x87CEEB);  // Sky blue

    // Set up camera
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;
    camera.position.y = 2;

    // Set up renderer
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('canvas-container').appendChild(renderer.domElement);

    // Add lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
    directionalLight.position.set(0, 1, 1);
    scene.add(directionalLight);

    // Create ground
    const groundGeometry = new THREE.PlaneGeometry(10, 10);
    const groundMaterial = new THREE.MeshStandardMaterial({color: 0x90EE90});  // Light green
    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -1;
    scene.add(ground);

    // Create pet (simple sphere for now)
    const petGeometry = new THREE.SphereGeometry(0.5, 32, 32);
    const petMaterial = new THREE.MeshPhongMaterial({color: 0x4169E1});  // Royal blue
    const pet = new THREE.Mesh(petGeometry, petMaterial);
    scene.add(pet);

    // Add eyes
    const eyeGeometry = new THREE.SphereGeometry(0.1, 16, 16);
    const eyeMaterial = new THREE.MeshPhongMaterial({color: 0xFFFFFF});
    const leftEye = new THREE.Mesh(eyeGeometry, eyeMaterial);
    const rightEye = new THREE.Mesh(eyeGeometry, eyeMaterial);
    leftEye.position.set(-0.2, 0.1, 0.4);
    rightEye.position.set(0.2, 0.1, 0.4);
    pet.add(leftEye);
    pet.add(rightEye);

    // Add trees
    function createTree(x, z) {
        const trunkGeometry = new THREE.CylinderGeometry(0.1, 0.1, 1);
        const trunkMaterial = new THREE.MeshPhongMaterial({color: 0x8B4513});
        const trunk = new THREE.Mesh(trunkGeometry, trunkMaterial);
        trunk.position.set(x, 0, z);

        const leavesGeometry = new THREE.ConeGeometry(0.5, 1, 8);
        const leavesMaterial = new THREE.MeshPhongMaterial({color: 0x228B22});
        const leaves = new THREE.Mesh(leavesGeometry, leavesMaterial);
        leaves.position.set(x, 1, z);

        scene.add(trunk);
        scene.add(leaves);
    }

    createTree(-2, -2);
    createTree(2, -2);
    createTree(0, -3);

    // Animation
    let time = 0;
    function animate() {
        requestAnimationFrame(animate);
        
        // Make pet bob up and down
        time += 0.05;
        pet.position.y = Math.sin(time) * 0.1;
        
        // Rotate pet slightly
        pet.rotation.y = Math.sin(time * 0.5) * 0.2;

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

    // Add orbit controls
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
</script>
"""

# Layout
col1, col2 = st.columns([3,1])

with col1:
    st.title("🌈 3D Pet World")
    # Render 3D scene
    components.html(threejs_code, height=600)

with col2:
    # Stats
    st.markdown("### Pet Stats")
    st.progress(0.8, "Happiness")
    st.progress(0.7, "Energy")
    st.progress(0.9, "Food")

    # Actions
    st.markdown("### Actions")
    if st.button("🎾 Play"):
        st.write("Playing with pet!")
    if st.button("🍖 Feed"):
        st.write("Feeding pet!")
    if st.button("🌳 Add Tree"):
        st.write("Adding tree!")

# Controls
st.markdown("### Movement Controls")
cols = st.columns(4)
with cols[0]:
    st.button("⬅️ Left")
with cols[1]:
    st.button("⬆️ Forward")
with cols[2]:
    st.button("⬇️ Back")
with cols[3]:
    st.button("➡️ Right")
