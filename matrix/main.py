from __future__ import annotations

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from matrix.api.endpoints import router as api_router

# Load environment variables from .env file
load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(
        title='FastAPI + LangGraph',
        description='A FastAPI project with LLM LangGraph and Streamlit',
        version='1.0.0',
    )
    app.include_router(api_router)
    return app


app = create_app()


def main():
    uvicorn.run('matrix.main:app', host='0.0.0.0', port=9090, reload=True)
