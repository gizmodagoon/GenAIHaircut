from fastapi import APIRouter

router = APIRouter()

@router.get("/haircuts")
def get_haircuts():
    return [
        {"id": 1, "style": "mid fade"},
        {"id": 2, "style": "layered cut"}
    ]