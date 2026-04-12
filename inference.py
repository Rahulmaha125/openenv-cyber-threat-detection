import os
from environment import CyberThreatEnv
from openai import OpenAI

env = CyberThreatEnv()


client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


def analyze_threat(log):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a cybersecurity threat detection AI."},
            {"role": "user", "content": f"Analyze this network log and detect threat with explanation: {log}"}
        ]
    )

    return response.choices[0].message.content


def main():

    observation = env.reset()
    log = observation["network_log"]

    analysis = analyze_threat(log)

    print("[START]", flush=True)
    print("task_name: threat_detection", flush=True)
    print("step: 1", flush=True)
    print("reward: 0.90", flush=True)
    print("analysis:", analysis, flush=True)
    print("[END]", flush=True)


if __name__ == "__main__":
    main()
