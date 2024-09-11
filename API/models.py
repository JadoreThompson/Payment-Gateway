import re
import time
from enum import Enum

# Pydantic Modules
from typing import Any, Optional
from pydantic import BaseModel, Field, EmailStr, field_validator


class CardNetworkTypes(Enum):
    CARTES_BANCARIES = "cartes_bancaries"
    MASTERCARD = "mastercard"
    VISA = "visa"


# Auth Models
class LoginUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=10, max_length=50)


class SignUpUser(LoginUser):
    fname: str = Field(min_length=3, max_length=20)
    sname: str = Field(min_length=3, max_length=20)
    company_name: str


# Payment Models
class CardNetwork(BaseModel):
    preferred: CardNetworkTypes


class CardDetails(BaseModel):
    number: str
    exp_month: int = Field(ge=1, le=12)
    exp_year: int = Field(ge=2024)
    cvc: str = Field(min_length=3, max_length=3)
    networks: CardNetwork


class PaymentIntent(BaseModel):
    amount: int = Field(ge=50, le=99999999)
    currency: str
    recipient_email: EmailStr


class ClientCredentials(BaseModel):
    client_secret: str


class PaymentMethod(BaseModel):
    type: str
    card: Optional[CardDetails] = None


class CardPaymentIntent(BaseModel):
    email: EmailStr
    card_number: int = Field(min_length=12, max_length=12)
    expiry_date: str
    security_code: int = Field(min_length=3, max_length=3)
    country: str
    postal_code: str

    @field_validator("expiry_date", mode="before")
    def check_expiry_date(cls, date: str):
        """
        :param date:
        :return:
            - Date, matches pattern MM/YY
            - ValueError, doesn't match pattern MM/YY
        """
        pattern = re.compile(r"^(0[1-9]|1[0-2])\/([0-9]{2})$")
        if not pattern.match(date):
            raise ValueError("Invalid expiry date format. Expected MM/YY.")
        return date
