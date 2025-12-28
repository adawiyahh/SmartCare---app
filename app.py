import streamlit as st
import time

st.set_page_config(page_title="SmartCare", layout="wide")

# Splash Screen
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    st.image("assets/smartcare_logo.jpg", width=200)
    st.markdown("### Intelligent. Empowered. Connected Elder Care")
    time.sleep(2)
    st.session_state.loaded = True
    st.rerun()

# Caregiver Dashboard
st.title("Caregiver Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Heart Rate", "72 bpm")
col2.metric("Elder Status", "Safe 🟢")
col3.metric("Last Medication", "Taken ✅")

st.divider()

# Meds taken

st.subheader("Medication Tracker")

med_taken = st.checkbox("Morning Medication Taken")

if med_taken:
    st.success("Medication confirmed")
else:
    st.warning("Medication not taken yet")

# Caregiver chat
st.subheader("Secure Caregiver Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

message = st.text_input("Send message to elder")

if st.button("Send"):
    st.session_state.messages.append(f"Caregiver: {message}")

for msg in st.session_state.messages:
    st.write(msg)

# Notification alert
st.subheader("Alerts")

if st.button("Trigger Emergency Alert"):
    st.error("🚨 Fall detected! Caregiver notified.")

# Fall Detection
st.subheader("Fall Detection System")

fall_detected = st.toggle("Simulate Fall Event")

if fall_detected:
    st.error("Fall detected from wristband sensor")
    st.write("Alert sent to caregiver & emergency contact")
else:
    st.success("No abnormal activity detected")



