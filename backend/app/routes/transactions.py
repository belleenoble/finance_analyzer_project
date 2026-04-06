#Goal of this file: 
#1) Define endpoints related to ALL transactions
#2) Manual Input of transactions (for users who don't have CSV files)

from fastapi import APIRouter

#Pydantic = library for data validation -> BaseModel is a class within this library allowing us to define data shape (name + type)
# -> I believe it essentially overviews your data based on dictionaries to ensure its correct!
from pydantic import BaseModel
from datetime import date

#calling from our storage service (holds all data) essentially a list containing all data even upload.py
from app.services.storage import transactions_db

router = APIRouter()

#Determines what a transaction data should look like -> DETERMINING DATA SHAPE!
class Transaction(BaseModel):
    date: date                              #Format Expectation: "2026-02-23"
    description: str                        #Format Expectation: any text 
    amount: float                           #Format Expectation: numbers 
    category: str                           #Format Expectation: any text such as "Transport"

#endpoint 1 -> user should be able to manually a transaction
#since we want to SEND this data to be stored POST will be use /manual because of the API prefix in main.py
@router.post("/manual")
def add_manual_transaction(transaction: Transaction): #transaction is an object , Transaction is the class (give me an object  of type Transaction CLASS)

    #.model_dump() converts the Transaction OJBJECT into plain dictionary (to match CSV-parsed format)
    transaction_dict = transaction.model_dump()
    transaction_dict["date"] = str(transaction_dict["date"]) #convert date to match CSV format

    transactions_db.append(transaction_dict) #Append to the shared storage list (in storage.py)

    return {
        "message": "Transaction added sucessfully",
        "transaction": transaction_dict
    }

#endpoint 2 -> get all transactions

@router.get("/")
def get_all_transactions():

    if not transactions_db:
        return { "message": "No Valid Transactions in system!", "transactions": []
        }
    
    return {
        "count": len(transactions_db),
        "transactions": transactions_db
    }