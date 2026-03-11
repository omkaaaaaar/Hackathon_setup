from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/test")
def test():
    return {"message": "API working"}