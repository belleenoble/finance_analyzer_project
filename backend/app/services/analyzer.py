#Analyzes total data and returns insights! (this file will work with insights.py)

#this files needs to access transaction data, do math, and then the
#routes will call the functions and return the results to the user. 

#three main functions 
#1)Overall Summary of Finances
#2)Breakdown by Category
#3)Breakdown by Month


from .storage import transactions_db

#Function 1 - Overall Summary
def get_summary():
    if not transactions_db:
        return{"message": "There are no transactions avaliable!"} #Error handling making sure that theres no math applied to an empty list
    
    #Focus: filter only negative amounts then sum the total of the transactions
    #Focus: Total money coming IN (income) We are looking at positive numbers now
    #We are classifying NEGATIVE NYMBERS as money going transactions!

    total_spent = 0
    total_income = 0

    #loop through every transaction on by one
    for t in transactions_db:

        if t["amount"] < 0:                      #t["amount"] grabs the value at the "amount" key
            total_spent += t["amount"]           #adds the negative number to the total spent (which is also negative)
   
        if t["amount"] > 0:
            total_income += t["amount"]          #adds the positive number to the total income

    return {
        "Total_Transactions": len(transactions_db),
        "total_spent": abs(total_spent), #abs() removes negative sign V(abs val)
        "total_income": total_income,
        "net" : total_income + total_spent
    }

#Function 2 - Transactions Breakdown by Category
def get_by_category():
    if not transactions_db:
        return {"messege": "There are no transactions avaliable!"} #Error Handling 
    
    category_totals = {} #empty dictionary to store the totals per category

    for t in transactions_db:
        
        if t["amount"] < 0:  # Check amount instead of category
            category = t["category"]
            amount = t["amount"]

            #If the category isn't tracked in the list already, it's inital value is 0
            if category not in category_totals:
                category_totals[category] = 0
            
            #add this category running amount to the total of category
            category_totals[category] += amount

    #new format should be {"Food": -120, etc}

    #breakdown the new dict into a list of dicitonary
    breakdown = []
    for category, total in category_totals.items():
        breakdown.append({
            "category": category,
            "total": round(total, 2) #round 2 decimal places
        })

    breakdown.sort(key=lambda x: x["total"])

    return {"category_breakdown": breakdown}

#Function 3: Breakdown by month
def get_by_month():
    if not transactions_db:
        return {"message": "No monthly transactions avaliable!"}
    
    month_totals = {}

    for t in transactions_db:

        parts = t["date"].split("-") #splitting the dash is cruicial for putting the date into list format (2026,01,23)
        month = parts[0] + "-" + parts[1]       #grabs just the year and month

        amount = t["amount"]

        if month not in month_totals:
            month_totals[month] = 0

        month_totals[month] += amount

    #same breakdown concept as the categories
    breakdown = []

    for month, total in month_totals.items():
        breakdown.append({
            "month": month,
            "total": round(total, 2)  # Use variable, not string
        })

    breakdown.sort(key=lambda x: x["total"])

    return {"monthly_breakdown": breakdown}