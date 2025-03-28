from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def read_root():
    return {'message': 'Welcome to FastAPI with LangGraph and Streamlit'}


@router.get('/health')
def health_check():
    return {'status': 'ok'}
