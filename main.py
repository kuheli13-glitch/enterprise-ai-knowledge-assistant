from fastapi import FastAPI
from app.api.routes import router
from app.core.database import engine, Base
from app.adapters import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    version="1.0.0"
)

app.include_router(router)