from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():

    return {
        "application": "Perto AI Engine",
        "version": "1.0.0",
        "status": "running",
        "camera": "not initialized"
    }