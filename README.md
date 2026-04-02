# Cyber Threat Detection OpenEnv

This project simulates a cyber security environment where an AI agent learns to detect suspicious network activity from logs.

## Problem

Cyber attacks such as brute force login attempts and suspicious login activities are common in modern networks. 

This environment simulates these scenarios so that an AI agent can learn to take appropriate actions.

## Agent Actions

block_ip  
monitor  
allow  

## Tasks

easy  
medium  
hard  

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