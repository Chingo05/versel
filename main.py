from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет! Это моё первое API на Vercel"}

@app.get("/about")
def about():
    return {"project": "FastAPI на Vercel", "author": "Твоё имя"}

@app.get("/api/hello/{name}")
def hello(name: str):
    return {"greeting": f"Привет, {name}!"}
