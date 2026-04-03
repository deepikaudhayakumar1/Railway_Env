---
title: Railway Env
emoji: 🚆
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# 🚆 Railway Crack Detection RL Environment

## 📌 Description
This project implements a Reinforcement Learning (RL) environment using the OpenEnv framework.  
The environment simulates a real-world railway monitoring system where an AI agent detects track faults based on sensor data.

---

## 🎯 Objective
The goal of the agent is to:
- Monitor railway track conditions
- Detect possible cracks
- Take appropriate actions to ensure safety

---

## 🧠 Environment Details

### 🔹 State (Observation Space)
The agent observes:
- `vibration` → Track vibration level
- `crack_prob` → Probability of crack occurrence

---

### 🔹 Actions (Action Space)
The agent can take 3 actions:
- `0` → Ignore  
- `1` → Inspect  
- `2` → Send Alert  

---

### 🔹 Reward Function
The reward system is designed to encourage correct decisions:

- Correct crack detection → **+1**
- Missed crack → **-1**
- False alert → **-0.5**
- Safe action → **+0.2**

---

## 🧪 Tasks

The environment includes 3 tasks with increasing difficulty:

### 🟢 Easy
- Detect obvious cracks  
- Simple decision logic  

### 🟡 Medium
- Detect moderate cracks  
- Conditional decision making  

### 🔴 Hard
- Detect subtle cracks  
- Combine multiple sensor inputs for decision  

---

## 📊 Scoring
Each task returns a score between: