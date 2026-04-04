from fastapi import FastAPI
from inference import main

app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "App is running"}

# RESET endpoint
@app.post("/reset")
def reset():
    try:
        observation = main()

        return {
            "observation": observation,
            "info": {}
        }

    except Exception as e:
        # ✅ Always return correct format
        return {
            "observation": [],
            "info": {"error": str(e)}
        }

# STEP endpoint
@app.post("/step")
def step():
    try:
        observation = main()

        return {
            "observation": observation,
            "reward": 0,
            "done": False,
            "info": {}
        }

    except Exception as e:
        # ✅ Always return correct format
        return {
            "observation": [],
            "reward": 0,
            "done": True,
            "info": {"error": str(e)}
        }