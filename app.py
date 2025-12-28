import streamlit as st
import time

# -------------------------
# PAGE CONFIG (MOBILE FIRST)
# -------------------------
st.set_page_config(
    page_title="SmartCare",
    layout="centered"
)

# -------------------------
# PHONE FRAME STYLING
# -------------------------
st.markdown("""
<style>
.phone-frame {
    max-width: 390px;
    margin: auto;
    border: 2px solid #e5e7eb;
    border-radius: 28px;
    padding: 16px;
    background-color: white;
}
.center {
    text-align: center;
}
.big-button button {
    width: 100%;
    height: 3rem;
    font-size: 1rem;
}
</style>

<div class="phone-frame">
""", unsafe_allow_html=True)

# -------------------------
# SPLASH SCREEN
# -------------------------
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    st.markdown("<div class='center'>", unsafe_allow_html=True)
    st.image("assets/smartcare_logo.jpg", width=160)
    st.markdown("### Intelligent • Empowered • Connected")
    st.markdown("##### Elder Care Made Simple")
    st.markdown("</div>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.loaded = True
    st.rerun()

# -------------------------
# CAREGIVER DASHBOARD
# -------------------------
st.markdown("## 👩‍⚕️ Caregiver Dashboard")

st.markdown("### 👴 Elder Overview")

st.metric("❤️ Heart Rate", "72 bpm")
st.metric("🟢 Status", "Safe")
st.metric("💊 Medication", "Taken")

st.divider()

# -------------------------
# MEDICATION TRACKER
# -------------------------
st.markdown("### 💊 Medication Tracker")

if "med_taken" not in st.session_state:
    st.session_state.med_taken = False

st.session_state.med_taken = st.checkbox("Morning medication taken")

if st.session_state.med_taken:
    st.success("Medication confirmed")
else:
    st.warning("Medication not taken yet")

st.divider()

# -------------------------
# CAREGIVER CHAT
# -------------------------
st.markdown("### 💬 Secure Caregiver Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

message = st.text_input("Type a message")

if st.button("Send Message"):
    if message.strip():
        st.session_state.messages.append(f"👩‍⚕️ Caregiver: {message}")

for msg in st.session_state.messages:
    st.info(msg)

st.divider()

# -------------------------
# ALERTS
# -------------------------
st.markdown("### 🚨 Alerts")

if st.button("Trigger Emergency Alert"):
    st.error("🚨 Fall detected! Caregiver notified immediately.")

st.divider()

# -------------------------
# FALL DETECTION (SIMULATED)
# -------------------------
st.markdown("### 🛑 Fall Detection System")

fall_event = st.toggle("Simulate fall from wristband")

if fall_event:
    st.error("Fall detected via wristband sensor")
    st.write("Alert sent to caregiver and emergency contact")
else:
    st.success("No abnormal activity detected")

# -------------------------
# CLOSE PHONE FRAME
# -------------------------
st.markdown("</div>", unsafe_allow_html=True)



