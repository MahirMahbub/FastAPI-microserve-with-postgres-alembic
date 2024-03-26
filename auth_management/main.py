import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from auth_management.controllers.router import api_router

if os.getenv("ENVIRONMENT") == "development":
    auth_app = FastAPI(
        title="AuthApp",
        description="Authentication Application",
        version="1.0.0",
        debug=True
        # openapi_url="/api/v1/auth/openapi.json",
        # docs_url="/api/v1/auth/docs",
        # root_path="/api/v1"
    )
else:
    auth_app = FastAPI(
        title="AuthApp",
        description="Authentication Application",
        version="1.0.0",
        openapi_url="/api/v1/auth/openapi.json",
        docs_url="/api/v1/auth/docs",
        debug=False
        # root_path="/api/v1"
    )
auth_app.add_middleware(GZipMiddleware)
auth_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

auth_app.include_router(api_router, prefix='/api/v1/auth')

# @auth_app.on_event("startup")
# async def startup_event():
#     from auth_management.config.db import initialize_db
#     await initialize_db()

if __name__ == "__main__":
    # install_packages()
    # uvicorn.run("hello:app", host=BIND, port=int(PORT), reload=RELOAD, debug=RELOAD, workers=int(WORKERS))
    uvicorn.run("main:auth_app", host="localhost", port=int(7003), reload=True, workers=int(1), env_file='.env')