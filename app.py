from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import(
    view_transactions,
    add_transaction,
    update_transaction,
    delete_transaction
)
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/transactions")
def get_transactions():
    return view_transactions()
@app.post("/transactions")
def create_transactions(data: dict):
    add_transaction(
        data["amount"],
        data["category"],
        data["type"],
        data["date"],
        data["description"],
    )
    return {
        "message": "Transaction added successfully"
    }
@app.put("/transactions/{transactions_id}")
def edit_transaction(transaction_id: int, data: dict):
    update_transaction(
        transaction_id,
        data["choice"],
        data["value"]
    )
    return {
        "message": "Transaction updated successfully"
    }
@app.delete("/transaction/{transaction_id}")
def remove_transactions(transaction_id: int):
    delete_transaction(transaction_id)
    return {
        "message": "Transaction deleted successfully"
    }