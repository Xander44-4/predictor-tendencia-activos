from fastapi import FastAPI

app = FastAPI(title="Título Nuevo y Claro")

@app.get("/")
def read_root():
    return {"hello": "world"}
