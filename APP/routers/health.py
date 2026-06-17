from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
def liveness() -> dict:
    return {"status": "alive"}


@router.get("/ready")
def readiness() -> dict:
    return {"status": "ready"}
