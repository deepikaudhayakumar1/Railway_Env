from fastapi import FastAPI
from inference import main as env_main

app = FastAPI()

# REQUIRED by OpenEnv
def main():
    return app

# Root endpoint
@app.get("/")
def home():
    return {"message": "App is running"}

# RESET endpoint
@app.post("/reset")
def reset():
    try:
        observation = env_main()

        return {
            "observation": observation,
            "info": {}
        }

    except Exception as e:
        return {
            "observation": [],
            "info": {"error": str(e)}
        }

# STEP endpoint
@app.post("/step")
def step():
    try:
        observation = env_main()

        return {
            "observation": observation,
            "reward": 0,
            "done": False,
            "info": {}
        }

    except Exception as e:
        return {
            "observation": [],
            "reward": 0,
            "done": True,
            "info": {"error": str(e)}
        }