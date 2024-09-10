# Directory Modules
from API.models import *

# FastAPI Modules
from fastapi import APIRouter


payments = APIRouter()


@payments.get("/")
async def read_root():
    return {"status": 200, "message": "payment"}


@payments.post("/create")
async def create_payment(payment_info: PaymentInfo):
    return payment_info
