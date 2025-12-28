import streamlit as st
import time

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="SmartCare", layout="centered")

# -------------------------
# STYLING (PHONE FRAME + BUTTONS)
# -------------------------
st.markdown("""
<style>
/* Phone frame container */
.phone-frame {
    max-width: 390px;
    min-height: 700px;
    margin: auto;
    border: 2px solid #e5e7eb;
    border-radius: 28px;
    padding: 0;
    background-color: white;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
    overflow-y: auto;
}

/* Top bar */
.top-bar {
    background-color: #2254c5;
    color: white;
    padding: 12px;
    border-top-left-radius: 28px;
    border-top-right-radius: 28px;
    text-align: center;
    font-weight: bold;
    font-size: 1.2rem;
}

/* Center content */
.center {
    text-align: center;
    padding: 16px;
}

/* Full width buttons */
.full-btn button {
    width: 100% !important;
    height: 3rem;
    font-size: 1rem;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SPLASH SCREEN
# -------------------------
if "loaded" not in st.session_state:
    st.session_state.loaded = False
if not st.session_state.loaded:
    st.markdown("<div class='phone-frame center'>", unsafe_allow_html=True)
    st.image("assets/smartcare_logo.jpg", width=160)
    st.markdown("### Intelligent • Empowered • Connected")
    st.markdown("##### Elder Care Made Simple")
    time.sleep(2)
    st.session_state.loaded = True
    st.experimental_rerun()

# -------------------------
# NAVIGATION STATE
# -------------------------
if "screen" not in st.session_state:
    st.session_state.screen = "home"

# -------------------------
# PHONE FRAME START
# -------------------------
st.markdown("<div class='phone-frame'>", unsafe_allow_html=True)

# -------------------------
# TOP BAR
# -------------------------
st.markdown("<div class='top-bar'>SmartCare</div>", unsafe_allow_html=True)

# -------------------------
# NAVIGATION BAR
# -------------------------
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1,1,1,1])
with nav_col1:
    if st.button("🏠 Home"):
        st.session_state.screen = "home"
with nav_col2:
    if st.button("💊 Meds"):
        st.session_state.screen = "meds"
with nav_col3:
    if st.button("💬 Chat"):
        st.session_state.screen = "chat"
with nav_col4:
    if st.button("🚨 Alerts"):
        st.session_state.screen = "alerts"

st.divider()

# -------------------------
# HOME SCREEN
# -------------------------
if st.session_state.screen == "home":
    st.markdown("## 👴 Elder Overview")
    st.metric("❤️ Heart Rate", "72 bpm")
    st.metric("🟢 Status", "Safe")
    st.metric("💊 Last Medication", "Taken ✅")
    st.divider()

    st.markdown("### 🛡️ Emergency")
    if st.button("Simulate Fall Event"):
        st.session_state.screen = "alerts"
        st.experimental_rerun()

# -------------------------
# MEDICATION SCREEN
# -------------------------
elif st.session_state.screen == "meds":
    st.markdown("## 💊 Medication Tracker")
    if "med_taken" not in st.session_state:
        st.session_state.med_taken = False
    st.session_state.med_taken = st.checkbox("Morning medication taken")
    if st.session_state.med_taken:
        st.success("Medication confirmed")
    else:
        st.warning("Medication not taken yet")

# -------------------------
# CHAT SCREEN
# -------------------------
elif st.session_state.screen == "chat":
    st.markdown("## 💬 Secure Caregiver Chat")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    message = st.text_input("Type a message")
    if st.button("Send Message"):
        if message.strip():
            st.session_state.messages.append(f"👩‍⚕️ Caregiver: {message}")

    for msg in st.session_state.messages:
        st.info(msg)

# -------------------------
# ALERT SCREEN
# -------------------------
elif st.session_state.screen == "alerts":
    st.markdown("## 🚨 Emergency Alerts")
    st.error("🚨 Fall detected! Caregiver notified immediately.")
    st.write("Simulated alert sent to caregiver and emergency contact.")
    if st.button("Mark as Resolved"):
        st.session_state.screen = "home"

# -------------------------
# CLOSE PHONE FRAME
# -------------------------
st.markdown("</div>", unsafe_allow_html=True)



