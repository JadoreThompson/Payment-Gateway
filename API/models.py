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
class PaymentInfo(BaseModel):
    full_name: str
    card_number: int
    sort_code: int
    account_number: int
    cvv: int
    expiry_date: int


# Exceptions
class HTTPResponse(BaseModel):
    status: int
    detail: Any
