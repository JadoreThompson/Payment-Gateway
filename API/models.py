from pydantic import BaseModel


class CardInfo(BaseModel):
    full_name: str
    card_number: int
    sort_code: int
    account_number: int
    cvv: int
    expiry_date: int
