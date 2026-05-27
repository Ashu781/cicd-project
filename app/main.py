from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "version 2 deployed automatically"}