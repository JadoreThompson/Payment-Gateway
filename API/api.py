import uvicorn
from fastapi import FastAPI, HTTPException

# Directory Modules
from API.auth import auth
from API.payments import payments


app = FastAPI()

# Including the custom routes
app.include_router(auth, prefix="/auth", tags=["auth"])
app.include_router(payments, prefix="/payments", tags=["payments"])


@app.get("/")
async def read_root():
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)