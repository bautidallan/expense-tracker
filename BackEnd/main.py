from fastapi import FastAPI
from routes.expense_route import router as expense_rout

app=FastAPI()

app.include_router(expense_rout)