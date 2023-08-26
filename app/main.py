from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}



