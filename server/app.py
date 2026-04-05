from fastapi import FastAPI
from inference import main as inference_main

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Railway Env Running"}

@app.post("/reset")
def reset():
    return {
        "observation": "reset done",
        "reward": 0,
        "done": False
    }

@app.post("/step")
def step():
    return {
        "observation": "step done",
        "reward": 1,
        "done": False
    }
# IMPORTANT
def main():
    return app