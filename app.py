import streamlit as st
import pyttsx3
import subprocess
import os


st.set_page_config(page_title="🗣️ Text to Speech App", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    textarea {
        border: 2px solid #4CAF50 !important;
        border-radius: 5px !important;
    }

    .stButton > button {
        background-color: #4CAF68 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }

    .stButton > button:hover {
        background-color: #45a049 !important;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)


# --- Banner ---
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🗣️ Text to Speech Web App</h1>
    <p style='text-align: center;'>Convert your thoughts into speech in seconds!</p>
""", unsafe_allow_html=True)

# --- Get Voice Options ---
engine_preview = pyttsx3.init()
voices = engine_preview.getProperty('voices')
voice_map = {f"{'Male' if 'male' in v.name.lower() else 'Female'} - {v.name}": v.id for v in voices}

# --- Sidebar Voice Options ---
st.sidebar.header("🎙️ Voice Settings")
selected_voice = st.sidebar.selectbox("Choose Voice", list(voice_map.keys()))
rate = st.sidebar.slider("Speech Rate", 100, 250, 150)

# --- Main Input ---
st.subheader("📝 Enter Text Below")
text_input = st.text_area("Type something to convert into speech", height=200)

if st.button("🔊 Speak"):
    if text_input.strip():
        with st.spinner("Speaking..."):
            # Escape double quotes in text
            safe_text = text_input.replace('"', '\\"')
            command = f'python speak.py --text "{safe_text}" --voice "{voice_map[selected_voice]}" --rate {rate}'
            subprocess.Popen(command, shell=True)
        st.success("✅ Done! Text is being spoken.")
    else:
        st.warning("⚠️ Please enter some text before clicking 'Speak'.")

st.markdown("---")
st.sidebar.info("💡 Tip: You can try quotes, affirmations, or tongue-twisters!")


st.sidebar.markdown("---")
# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
st.sidebar.markdown("---")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")