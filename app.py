from fastapi import FastAPI
from inference import main

app = FastAPI()

# Root endpoint (optional)
@app.get("/")
def home():
    return {"message": "App is running"}

# RESET endpoint (IMPORTANT)
@app.post("/reset")
def reset():
    try:
        observation = main()   # your environment reset logic

        return {
            "observation": observation,
            "info": {}
        }

    except Exception as e:
        return {
            "error": str(e)
        }

# STEP endpoint (IMPORTANT)
@app.post("/step")
def step():
    try:
        observation = main()   # your step logic (update if needed)

        return {
            "observation": observation,
            "reward": 0,
            "done": False,
            "info": {}
        }

    except Exception as e:
        return {
            "error": str(e)
        }