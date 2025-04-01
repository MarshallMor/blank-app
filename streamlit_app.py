import streamlit as st
from datetime import datetime, timedelta
import time

# Page Configuration
st.set_page_config(page_title="Happy Birthday Cel!", layout="wide")

# Title and Video
st.title("🎉 Happy Birthday, Cel! 🎂")
st.markdown("### *A Special Surprise Awaits You!*")
VIDEO_URL = "https://www.youtube.com/watch?v=J_y9MqOYyiQ"
st.video(VIDEO_URL)
st.markdown(f"If the video is not working, click [here]({VIDEO_URL})")

st.caption(
    "This is a quick webpage I made to celebrate your birthday! 🎈 "
    "The bigger project I was working on is taking a little longer than expected, "
    "but here's a countdown to your real present! 🎁"
)

# Sidebar Info
st.sidebar.image("https://i.imgur.com/4M34hi2.png", width=200)  # Example image (replace)
st.sidebar.markdown("## 🎂 Birthday Countdown!")
st.sidebar.write("Your special gift will be revealed soon!")

# Countdown Logic
target_date = datetime(2025, 4, 8, 23, 59, 59)

# Placeholder for countdown
placeholder = st.empty()

# Progress bar
progress_placeholder = st.empty()
while datetime.now() < target_date:
    time_left = target_date - datetime.now()
    
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    with placeholder.container():
        st.header("Countdown to Your Special Gift")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Days", days)
        col2.metric("Hours", hours)
        col3.metric("Minutes", minutes)
        col4.metric("Seconds", seconds)
        
        if minutes % 1 == 0 and seconds == 0:
            st.balloons()
    
    time.sleep(1)
placeholder.empty()
st.success(f"🎁 Your special gift is ready! Happy {target_date.strftime('%B %d, %Y')}!")
 
