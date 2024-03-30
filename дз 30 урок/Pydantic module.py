from pydantic import BaseModel

class User(BaseModel):
    name: str
    mail: str
    address: str

class Banks(BaseModel):
    bank_name: str
    rating: float
    opened: str

class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: str

class Balance(BaseModel):
    card: Cards
    amount: int
    currency: str
