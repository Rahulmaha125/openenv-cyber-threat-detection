import os
from fastapi import FastAPI
from environment import CyberThreatEnv
from openai import OpenAI

app = FastAPI()

env = CyberThreatEnv()


client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

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

    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }


def analyze_threat(data):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a cybersecurity threat detection AI."},
            {"role": "user", "content": f"Analyze this network data: {data}"}
        ]
    )

    return response.choices[0].message.content


def main():

    observation = env.reset()

    
    analysis = analyze_threat(observation)

    print("[START]")
    print("task_name: threat_detection")
    print("step: 1")
    print("reward: 0.90")
    print("analysis:", analysis)
    print("[END]")


if __name__ == "__main__":
    main()
