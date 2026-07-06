from operator import gt
from pydantic import BaseModel,Field
from datetime import date


class Expense(BaseModel):
    amount:float 
    category:str = Field(min_length=3,max_length=10)
    description:str
    date:date

class ExpenseResponse(Expense):
    id: str  

    @classmethod
    def from_mongo(cls, doc: dict):
        doc["id"] = str(doc["_id"])  # ObjectId → string
        return cls(**doc)