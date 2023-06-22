from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .data_base import engine, Base
from .routes import car_router, user_router


ALLOWED_ORIGINS = [
    "http://localhost:8080",
]


def create_app():
    Base.metadata.create_all(bind=engine)
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(car_router)
    app.include_router(user_router)
    return app


app = create_app()
