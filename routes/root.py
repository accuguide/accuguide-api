from fastapi import APIRouter, Depends

from middleware.security import verify_api_key

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.get("/")
def root():
    return {"message": "success"}
