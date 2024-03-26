from fastapi import APIRouter

from auth_management.controllers import test

api_router: APIRouter = APIRouter()
api_router.include_router(test.test_router)