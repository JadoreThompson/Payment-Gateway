from typing import Any
from pydantic import BaseModel, Field


# Auth Models
class LoginUser(BaseModel):
    email: str
    password: str = Field(min_length=10, max_length=50)


class SignUpUser(LoginUser):
    fname: str = Field(min_length=3, max_length=20)
    sname: str = Field(min_length=3, max_length=20)
    company_name: str


# Payment Models
class PaymentIntent(BaseModel):
    amount: int = Field(ge=50, le=99999999)
    currency: str


class CardPaymentIntent(BaseModel):
    email: str
    card_number: int = Field(min_length=12, max_length=12)
    expiry_date: str
    security_code: int = Field(min_length=3, max_length=3)
    country: str
    postal_code: str
