from fastapi import FastAPI
from app.database import engine, Base
from app.models import User  # noqa

app = FastAPI(title="Health AI Platform")

@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok", "service": "api"}

@app.get("/")
def root():
    return {"message": "Health AI Platform API"}
