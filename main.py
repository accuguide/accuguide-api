import json

from fastapi import FastAPI

from routes import root, search

with open("metadata.json") as f:
    metadata = json.load(f)

app = FastAPI(**metadata)
app.include_router(root.router)
app.include_router(search.router)
