from fastapi import APIRouter

from app.core.result_cache import result_cache

router = APIRouter(tags=["Status"])


@router.get("/latest")

def latest():

    result = result_cache.get_result()

    if result is None:

        return {

            "success": False,

            "message": "No AI result available"

        }

    return {

        "success": True,

        "result": result

    }