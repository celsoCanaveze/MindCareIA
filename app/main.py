from fastapi import FastAPI
from app.routes import ia_routes

app = FastAPI(title="MindCareIA", version="1.0")

app.include_router(ia_routes.router, prefix="/api/ia", tags=["IA Generativa"])

@app.get("/")
def root():
    return {"message": "MindCareIA API está ativa 🚀"}