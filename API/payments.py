from typing import Tuple
import aiohttp
from cryptography.fernet import Fernet
import base64

import os
from dotenv import load_dotenv

# Directory Modules
from API.models import *

# FastAPI Modules
from fastapi import APIRouter
from fastapi.responses import JSONResponse


load_dotenv("../.env")

# Environment Variables
BASE_URL = "https://api.stripe.com/v1/"
HEADER = {
    "Authorization": f"Bearer {os.getenv("STRIPE_SANDBOX_SECRET_KEY")}"
}


FERNET_KEY = base64.b64encode(bytes(os.getenv("FERNET_KEY").encode()))
fernet = Fernet(FERNET_KEY)


def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(encrypted_data: str) -> str:
    return fernet.decrypt(encrypted_data.encode()).decode()


# API Instantiation
payments = APIRouter()


@payments.get("/")
async def read_root():
    return {"status": 200, "message": "payment"}


# Call this when user decides to enter basket as they have made their intent to pay
@payments.post("/payment-intent")
async def create_payment_intent(info: PaymentIntent):
    """
    :param info: class PaymentIntent
    :return: str(Client Secret Key)
    :notes: Allows client to securely create payment transaction
    """

    try:
        async with aiohttp.ClientSession(headers=HEADER) as session:
            async with session.post(
                    BASE_URL + "payment_intents",
                    data={"amount": info.amount, "currency": info.currency, "receipt_email": info.recipient_email}) as rsp:
                data = await rsp.json()
                encrypted_client_secret = encrypt_data(data["client_secret"])
                return JSONResponse(status_code=200, content={"detail": encrypted_client_secret})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"{type(e)}, {str(e)}"})


@payments.post("/create-payment-method")
async def create_payment_method(payment_info: PaymentMethod):
    return payment_info
