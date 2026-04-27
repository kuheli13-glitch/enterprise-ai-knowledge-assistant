from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Enterprise AI Knowledge Assistant API is running"
    }


@router.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "Server is healthy"
    }