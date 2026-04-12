from fastapi import FastAPI
from environment import CyberThreatEnv
from inference import analyze_threat   
import uvicorn
import random

app = FastAPI()

env = CyberThreatEnv()


@app.get("/")
def home():
    
    obs = env.reset()
    log = obs["network_log"]

    analysis = analyze_threat(log)

    return {
        "status": "Cyber Threat Detection System",
        "network_log": log,
        "analysis": analysis
    }


@app.get("/health")
def health():
    return {"status": "running"}


@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}


@app.post("/step")
def step(data: dict):

    try:
        action = data.get("action")

        obs, reward, done, info = env.step(action)

        return {
            "observation": obs,
            "reward": reward,
            "done": done,
            "info": info
        }

    except Exception as e:
        return {"error": str(e)}



@app.get("/dashboard")
def dashboard():

    logs = [
        "20 failed login attempts from same IP",
        "Brute force attack detected",
        "Normal user login",
        "SQL Injection attempt",
        "Multiple password reset attempts"
    ]

    data = []

    for i in range(10):
        log = random.choice(logs)

        status = "Threat" if "attack" in log.lower() or "failed" in log.lower() else "Safe"

        data.append({
            "log": log,
            "status": status
        })

    return {
        "total_logs": random.randint(200, 500),
        "active_threats": random.randint(10, 50),
        "blocked_ips": random.randint(5, 30),
        "logs": data
    }


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
