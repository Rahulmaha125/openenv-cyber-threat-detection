import random

class CyberThreatEnv:

    def __init__(self):

        self.logs = [
            ("20 failed login attempts from same IP", "block_ip", 0.95),
            ("Login attempt from unusual country", "monitor", 0.70),
            ("Normal user login", "allow", 0.10),
            ("Multiple password reset attempts", "monitor", 0.65),
            ("Brute force attack detected", "block_ip", 0.98)
        ]

        self.current_log = None

    def reset(self):

        self.current_log = random.choice(self.logs)

        return {
            "network_log": self.current_log[0],
            "risk_score": self.current_log[2]
        }

    def step(self, action):

        correct_action = self.current_log[1]

        reward = 1.0 if action == correct_action else 0.0

        done = True

        return {
            "network_log": self.current_log[0],
            "risk_score": self.current_log[2]
        }, reward, done, {"correct_action": correct_action}
