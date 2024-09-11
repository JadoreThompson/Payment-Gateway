import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Directory Modules
from API.auth import auth
from API.payments import payments


app = FastAPI()

# TODO: Setup HTTPS Connection
# Including the custom routes
app.include_router(auth, prefix="/auth", tags=["auth"])
app.include_router(payments, prefix="/payments", tags=["payments"])


@app.get("/")
async def read_root():
    return {"status": 200}


@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=400, content={"detail": f"{type(exc).__name__}: {str(exc)}"})


if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)