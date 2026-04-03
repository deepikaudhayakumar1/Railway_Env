from fastapi import FastAPI
from inference import main

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Railway Env Running"}

@app.post("/reset")
def reset():
    result = main()
    return {"result": result}

@app.post("/step")
def step():
    result = main()
    return {"result": result}