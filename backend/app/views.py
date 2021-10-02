from fastapi import APIRouter
from fastapi.responses import FileResponse

view_router = APIRouter()

@view_router.get("/")
def home():
    return FileResponse('app/frontend/public/index.html')
