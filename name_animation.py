import streamlit as st
import time

# Title for the Streamlit app
st.title("Animated Name in Streamlit")

# Adding custom CSS for animation
st.markdown(
    """
    <style>
    .animated-name {
        font-size: 48px;
        color: #4CAF50;
        animation: fade 3s infinite;
    }

    @keyframes fade {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display animated name using HTML
st.markdown('<div class="animated-name">Ravindra Nath</div>', unsafe_allow_html=True)

# If you want the name to change dynamically over time, you can use st.empty and a loop
placeholder = st.empty()

name = "Ravindra Nath"
while True:
    for char in name:
        placeholder.markdown(f'<div class="animated-name">{char}</div>', unsafe_allow_html=True)
        time.sleep(1.0)  # Adjust speed of animation
