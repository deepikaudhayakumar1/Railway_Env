from fastapi import FastAPI
from inference import main as inference_main

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Railway Env Running"}

@app.post("/reset")
def reset():
    result = inference_main()
    return {"result": result}

@app.post("/step")
def step():
    result = inference_main()
    return {"result": result}

# 👇 ADD THIS
def main():
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=7860)

# 👇 THIS IS VERY IMPORTANT
if __name__ == "__main__":
    main()