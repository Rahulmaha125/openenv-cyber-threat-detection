from fastapi import FastAPI
from environment import CyberThreatEnv

app = FastAPI()

env = CyberThreatEnv()

@app.get("/")
def home():
    return {"message": "Cyber Threat Detection Environment"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: str):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }
