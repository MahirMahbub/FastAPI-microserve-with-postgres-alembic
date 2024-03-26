from fastapi import APIRouter


test_router: APIRouter = APIRouter()

@test_router.get("/hello/{name}")
def say_hello(name: str) -> dict[str, str]:

    return {"message": f"Hello {name}"}