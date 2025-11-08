from fastapi import FastAPI

app = FastAPI(title="Hello World FASTAPI")

@app.get("/")
def read_root():
    return {"message": "World FASTAPI"}