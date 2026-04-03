---
title: Cyber Threat Detection Env
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
app_file: inference.py
pinned: false
---

# Cyber Threat Detection Environment

This project simulates a cybersecurity environment where an AI agent analyzes network logs and decides whether to allow or block suspicious activity.

## Tasks

- Detect suspicious login attempts
- Detect brute-force attacks
- Detect abnormal network behavior

## Actions

block_ip  
monitor  
allow

## Reward

Correct action → 1.0  
Incorrect action → 0.0

## Example

Log:
20 failed login attempts from same IP

Action:
block_ip

Reward:
1.0

## Real World Use

This environment can help train reinforcement learning agents for automated cyber threat detection in enterprise networks.
