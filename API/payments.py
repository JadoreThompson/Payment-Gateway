import aiohttp

import os
from dotenv import load_dotenv

from urllib.parse import urlencode

# Directory Modules
from API.models import *

# FastAPI Modules
from fastapi import APIRouter


load_dotenv("../.env")

# Environment Variables
BASE_URL = "https://api.stripe.com/v1/"
HEADER = {
    "Authorization": f"Bearer {os.getenv("STRIPE_SANDBOX_SECRET_KEY")}"
}

# API Instantiation
payments = APIRouter()


@payments.get("/")
async def read_root():
    return {"status": 200, "message": "payment"}


@payments.post("/payment_intent")
async def create_payment(info: PaymentIntent):
    async with aiohttp.ClientSession(headers=HEADER) as session:

        # First we get the currency and amount as the user's intent to purchase an item
        async with session.post(
                BASE_URL + "payment_intents",
                data={"amount": info.amount, "currency": info.currency}
        ) as rsp:
            data = await rsp.json()
            return data["client_secret"]


