from fastapi import APIRouter

from app.core.result_cache import result_cache

router = APIRouter(tags=["Analyze"])


@router.post("/analyze")

def analyze():

    result = result_cache.get_result()

    if result is None:

        return {

            "success": False,

            "message": "AI Worker has not produced any result."

        }

    return {

        "success": True,
        "result": result

    }