from fastapi import FastAPI
from . import models, database
from .routes import user_routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(user_routes.router, tags=["Users"])
