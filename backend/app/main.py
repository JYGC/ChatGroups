from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from app.core.auth import AuthSettings
from app.core.config import settings
from app.database.connection import db
from app.database.init_db import init_db


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


from app.models import address, chatgroup, message, user
init_db(db)
app = get_application()

@AuthJWT.load_config
def get_config():
    return AuthSettings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
from app.api.v0.user import user_router
app.include_router(user_router)
from app.views import view_router
app.include_router(view_router)
app.mount('/', StaticFiles(directory="app/frontend/public/"), name="static")
