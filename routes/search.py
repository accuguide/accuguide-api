from fastapi import APIRouter, Depends

from middleware.security import verify_api_key

router = APIRouter(prefix="/search", dependencies=[Depends(verify_api_key)])


@router.get("")
def search():
    return {"results": "a"}
