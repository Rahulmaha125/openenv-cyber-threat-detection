---
title: Cyber Threat Detection Env
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
app_file: inference.py
pinned: false
---
# 🛡️ Cyber Threat Detection & SOC Monitoring System

An AI-powered cybersecurity simulation platform that detects suspicious network activities and visualizes threats using a professional **Security Operations Center (SOC) dashboard**.

This project demonstrates how artificial intelligence can analyze network logs, detect cyber threats, and assist security teams in responding to attacks.

---

# 📌 Project Overview

Cyber attacks such as brute-force login attempts, abnormal access patterns, and suspicious account activity are common in modern networks.

This system simulates a **cybersecurity environment** where an AI agent analyzes network logs and decides the appropriate security action.

Possible actions:

• Allow normal activity
• Monitor suspicious behavior
• Block malicious IP addresses

The platform also provides a **SOC dashboard** that visualizes threat activity.

---

# 🎯 Objectives

• Detect cyber threats using AI
• Simulate realistic security logs
• Provide explainable AI threat analysis
• Visualize attacks using a SOC dashboard
• Demonstrate automated cybersecurity monitoring

---

# 🚀 Key Features

### 🔍 AI Threat Detection

Analyzes network activity logs and identifies suspicious behavior.

### 🧠 Explainable AI

Explains **why the system detected a threat**.

### ⚡ Cyber Attack Simulation

Simulates common cyber attacks such as:

* Brute-force login attempts
* Suspicious login locations
* Abnormal authentication activity

### 📊 SOC Dashboard

A professional **Security Operations Center dashboard** displaying:

• Threat statistics
• Attack monitoring graphs
• Security logs
• Network activity

### 📈 Attack Visualization

Graph-based representation of cyber attack patterns.

---

# 🧰 Technologies Used

* Python
* FastAPI
* Streamlit
* NumPy
* Pandas
* Scikit-learn
* Gymnasium

---

# 📁 Project Structure

openenv-cyber-threat-detection

│
├── app.py
├── inference.py
├── environment.py
├── explain.py
├── dashboard_soc.py
├── requirements.txt
└── README.md

---

# ⚙️ Installation

Clone the repository:

git clone https://github.com/Rahulmaha125/openenv-cyber-threat-detection.git
cd openenv-cyber-threat-detection

Install dependencies:

pip install -r requirements.txt

---

# 🧪 How Judges Can Run the Project

Follow these steps to run the project.

---

## 1️⃣ Run AI Threat Detection

python inference.py

Example Output:

[START]
task_name: threat_detection
step: 1
reward: 0.90
analysis: Multiple password reset attempts detected. Suspicious account activity.
[END]

This output demonstrates the AI analyzing a network log and detecting a threat.

---

## 2️⃣ Run SOC Dashboard

python -m streamlit run dashboard_soc.py

Open browser:

http://localhost:8501

The dashboard will display:

• Threat statistics
• Attack monitoring graphs
• Security logs
• Network activity

This simulates a **real Security Operations Center (SOC)**.

---

## 3️⃣ Run FastAPI Server (Optional)

python app.py

API will start at:

http://localhost:7860

Available endpoints:

GET /
POST /reset
POST /step

Example request:

POST /step
{
"action": "block_ip"
}

---

# 📊 Example Use Case

Example Network Log:

20 failed login attempts from same IP

AI Decision:

block_ip

Reward:

1.0

This demonstrates automated detection of brute-force attacks.

---

# 🌍 Real World Applications

This system can be used in:

• Enterprise network security monitoring
• Security Operations Centers (SOC)
• AI-based intrusion detection systems
• Cybersecurity research and training
• Automated threat detection platforms

---

# 🔮 Future Improvements

• Integration with real cybersecurity datasets
• Machine learning anomaly detection models
• Live network traffic monitoring
• Threat intelligence integration
• Automated incident response

---

# 👨‍💻 Author

Rahul Mahanavar
Cybersecurity & AI Enthusiast

---

# 📜 License

This project is developed for educational and research purposes.
