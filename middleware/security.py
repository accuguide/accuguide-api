import os

from dotenv import load_dotenv
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

load_dotenv()

API_KEYS = [k.strip() for k in os.getenv("API_KEYS", "").split(",") if k.strip()]

api_key_header = APIKeyHeader(name="x-api-key")


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or Invalid API Key",
        )
