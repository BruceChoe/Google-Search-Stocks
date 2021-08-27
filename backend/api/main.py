# from typing import List

from fastapi import FastAPI  # Depends, Response, status
from fastapi.middleware.cors import CORSMiddleware
import dustyapi

from .routers import dummies
from .dependencies import get_session

tags_metadata = [{"name": "dummies", "description": "An example resource."}]

app = FastAPI(openapi_tags=tags_metadata)

origins = ["http://localhost:3000"]  # TODO: Get these from environment variables.

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(dummies.router)

app.dependency_overrides[dustyapi.dependencies.get_session] = get_session


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Google Search Stocks API!",
        "docs": "/docs"
    }
