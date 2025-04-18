import streamlit as st
from gtts import gTTS
import os
from tempfile import NamedTemporaryFile


st.set_page_config(page_title="🗣️ Text to Speech App", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    textarea {
        border: 2px solid #45B7D1 !important;
        border-radius: 5px !important;
    }

    .stButton > button {
        background-color: #45B7D1  !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }

    .stButton > button:hover {
        background-color: #ebadee  !important;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

st.image("image.png", use_container_width=True)

# --- Banner ---
st.markdown("""
    <h1 style='text-align: center; color: #eeadd2;'>🗣️ Text to Speech Web App</h1>
    <p style='text-align: center;'>Convert your thoughts into speech in seconds!</p>
""", unsafe_allow_html=True)

# --- Get Voice Options ---
# engine_preview = pyttsx3.init()
# voices = engine_preview.getProperty('voices')
# voice_map = {f"{'Male' if 'male' in v.name.lower() else 'Female'} - {v.name}": v.id for v in voices}


st.sidebar.image("side.webp")
# --- Sidebar Voice Options ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3884/3884421.png", width=120)
st.sidebar.header("🎙️ Voice Settings")
language = st.sidebar.selectbox("🌐 Language", ["en", "ur", "fr", "es", "de"], index=0)
slow = st.sidebar.checkbox("🐢 Slow Mode", value=False)
st.sidebar.markdown("Choose your language and speed.")
st.sidebar.markdown("---")

# --- Main Input ---
st.subheader("📝 Enter Text Below")
default_text = "Hello, this is a demo of the text-to-speech application built using Python and Streamlit."
text_input = st.text_area("Type something...", value=default_text, height=200)

# --- Speak Button ---
if st.button("🔊 Speak"):
    if text_input.strip():
        with st.spinner("Generating speech..."):
            tts = gTTS(text=text_input, lang=language, slow=slow)
            with NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                tts.save(tmpfile.name)
                st.success("✅ Speech generated!")
                st.audio(tmpfile.name, format="audio/mp3")
    else:
        st.warning("⚠️ Please enter some text before speaking.")


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