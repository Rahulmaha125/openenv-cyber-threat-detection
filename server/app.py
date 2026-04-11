from fastapi import FastAPI
from environment import CyberThreatEnv
import uvicorn

app = FastAPI()

env = CyberThreatEnv()


@app.get("/")
def home():
    return {"message": "Cyber Threat Detection Environment Running"}


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


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
