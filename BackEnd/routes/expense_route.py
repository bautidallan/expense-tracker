from fastapi import APIRouter,HTTPException
from datetime import datetime
from database import db
from models.expense import ExpenseResponse,Expense



router=APIRouter(
    prefix="/expense"
)

@router.get("/summary", response_model=dict)
async def get_summary():
    try:
        listExpenses = await db.expenses.find().to_list(length=100)
        summary = {}
        for expense in listExpenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        return summary
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/summary/{category}", response_model=list[ExpenseResponse])
async def get_by_category(category: str):
    try:
        expenses = await db.expenses.find({"category": category}).to_list(length=100)
        return [ExpenseResponse(**expense) for expense in expenses]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/",response_model=ExpenseResponse)
async def createExpense(newExpense:Expense):
    createdId=await db.category.insert_one(dict(newExpense))
    new_doc=await db.category.find_one({"_id":createdId.inserted_id})
    return ExpenseResponse.from_mongo(new_doc)
    


