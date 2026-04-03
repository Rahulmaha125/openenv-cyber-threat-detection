from environment import CyberThreatEnv

env = CyberThreatEnv()

obs = env.reset()

print("Network Log:", obs)

log = obs["network_log"]

if "failed login" in log or "brute force" in log:
    action = "block_ip"
elif "unusual country" in log or "password reset" in log:
    action = "monitor"
else:
    action = "allow"

print("Agent Action:", action)

obs, reward, done, info = env.step(action)

print("Reward:", reward)
