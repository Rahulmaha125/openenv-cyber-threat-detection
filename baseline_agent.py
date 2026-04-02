from environment import CyberThreatEnv
import random

env = CyberThreatEnv()

state = env.reset()

print("Network Log:", state)

actions = ["block_ip", "monitor", "allow"]

action = random.choice(actions)

print("Agent Action:", action)

state, reward, done = env.step(action)

print("Reward:", reward)