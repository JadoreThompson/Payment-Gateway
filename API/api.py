import uvicorn
from fastapi import FastAPI, HTTPException

# Directory Modules
from API.models import *


app = FastAPI()


@app.get("/")
async def read_root():
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)