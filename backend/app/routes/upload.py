#Using APIRouter () from FastAPI -> lets this file define its own endpoints, 
# which then main.py should register (already established with prefix)

from fastapi import APIRouter, UploadFile, File

#importing the service that knows how to parse a CSV file
from app.services import csv_parser

#importing shared list where all transactions are stored
from app.services.storage import transactions_db

router = APIRouter() #creates router object (where the main.py should imoprt)

# general pattern for FastAPI Endpoint: def 'function_name'(param_name: expected type = File(...)) <- end file means where it comes from
# remember -> param_name = variable you use inside function. 
@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    parsed = await csv_parser.parse_csv(file) # gives file to parser service then returns clean list of transcaction dictionary

    #adds every parsed transation into a shared storage list
    transactions_db.extend(parsed) #.extend adds multiple times at once.

    return {
        "filename": file.filename,
        "message": f"{len(parsed)} transactions loaded sucessfully",
        "preview": parsed[:3] 
    }