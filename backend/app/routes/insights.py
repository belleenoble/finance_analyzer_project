#insights.py should recieve a request -> call to analyzer -> return the result
#there should be no logic here because of analyzer.py
#Three endpoints in this file for the three functions in analyzer

from fastapi import APIRouter
from ..services import analyzer #importing analyzer.py

router = APIRouter()

#Endpoint 1: Overall Summary
@router.get("/summary")
def get_summary():
    return analyzer.get_summary()

#Endpoint 2: Transaction BreakDown by Category
@router.get("/categories")
def get_by_category():
    return analyzer.get_by_category()

#Endpoint 3: Breakdown by Month
@router.get("/monthly")
def get_by_month():
    return analyzer.get_by_month()
