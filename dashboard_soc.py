import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.set_page_config(page_title="Cyber Security SOC Dashboard", layout="wide")

# ---------- DARK STYLE ----------
st.markdown("""
<style>
body {
background-color: #0e1117;
}
.metric-card {
background-color:#111827;
padding:20px;
border-radius:10px;
text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🛡 Cyber Security SOC Dashboard")

# ---------- METRICS ----------
col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Logs", random.randint(200,500))
col2.metric("Active Threats", random.randint(10,50))
col3.metric("Blocked IPs", random.randint(5,30))
col4.metric("Safe Traffic", random.randint(100,300))

st.write("")

# ---------- LIVE ATTACK GRAPH ----------
col1,col2 = st.columns([2,1])

with col1:

    st.subheader("📈 Live Attack Activity")

    attack_data = pd.DataFrame({
        "time": list(range(1,15)),
        "attacks": [random.randint(0,5) for i in range(14)]
    })

    fig = px.line(attack_data, x="time", y="attacks")

    st.plotly_chart(fig, use_container_width=True)


# ---------- GLOBAL ATTACK MAP ----------
with col2:

    st.subheader("🌍 Global Attack Map")

    map_data = pd.DataFrame({
        "lat":[37.77,28.61,51.50,35.68,-33.86],
        "lon":[-122.41,77.20,-0.12,139.69,151.20],
        "attack":[5,3,4,2,3]
    })

    st.map(map_data)


# ---------- SECURITY LOGS ----------
st.subheader("📄 Recent Security Logs")

logs = [
"20 failed login attempts from same IP",
"Brute force attack detected",
"Normal user login",
"SQL Injection attempt",
"Multiple password reset attempts"
]

data=[]

for i in range(10):

    log=random.choice(logs)

    status="Threat" if "attack" in log.lower() or "failed" in log.lower() else "Safe"

    data.append({
        "Log":log,
        "Status":status
    })

df=pd.DataFrame(data)

st.dataframe(df,use_container_width=True)