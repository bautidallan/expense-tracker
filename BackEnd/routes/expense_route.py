from fastapi import APIRouter,HTTPException
from datetime import datetime
from database import db
from models.expense import ExpenseResponse,Expense



router=APIRouter(
    prefix="/expense"
    
)

@router.get("/",response_model=list[ExpenseResponse])
async def getAll():
    responseList=[]
    try:
        listExpenses=await db.expenses.find().to_list(length=100)
        for expense in listExpenses:
            responseList.append(ExpenseResponse(**expense))
        return responseList
            
    except:
        raise HTTPException(
            status_code=400,
            detail="Erorr fetching data"
        )
    

@router.get("/summary/{category}")
async def getCategory(category:str):
    response_list=[]
    try:
        list=await db.expenses.find({"category":category}).to_list()
        for expense in list:
            response_list.append(ExpenseResponse(**expense))
    except:
        raise HTTPException(
            status_code=409,
            detail="Not found"
        )
    
@router.post("/",response_model=ExpenseResponse)
async def createExpense(newExpense:Expense):
    createdId=await db.category.insert_one(dict(newExpense))
    new_doc=await db.category.find_one({"_id":createdId.inserted_id})
    return ExpenseResponse.from_mongo(new_doc)
    


