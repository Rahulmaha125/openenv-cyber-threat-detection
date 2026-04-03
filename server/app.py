from fastapi import FastAPI
from environment import CyberThreatEnv
import uvicorn

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
def step(data: dict):

    action = data["action"]

    obs, reward, done = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
