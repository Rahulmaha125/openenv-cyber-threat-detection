import random

class CyberThreatEnv:

    def __init__(self):

        self.logs = [
            ("20 failed login attempts from same IP", "block_ip"),
            ("Login attempt from unusual country", "monitor"),
            ("Normal user login activity", "allow"),
            ("Multiple password reset attempts", "monitor"),
            ("Suspicious brute force attack detected", "block_ip")
        ]

        self.current_log = None


    def reset(self):

        self.current_log = random.choice(self.logs)

        return self.state()


    def state(self):

        return {
            "network_log": self.current_log[0]
        }


    def step(self, action):

        correct_action = self.current_log[1]

        if action == correct_action:
            reward = 1.0
        else:
            reward = 0.0

        done = True

        return self.state(), reward, done