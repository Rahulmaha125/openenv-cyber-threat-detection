from environment import CyberThreatEnv
from baseline_agent import agent_action

env = CyberThreatEnv()

def reset():
    return env.reset()

def step(action):
    return env.step(action)

if __name__ == "__main__":
    obs = env.reset()
    print("Observation:", obs)

    action = agent_action(obs)
    obs, reward, done, info = env.step(action)

    print("Action:", action)
    print("Reward:", reward)