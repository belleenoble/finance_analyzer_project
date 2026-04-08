#Analyzes anomalies in the data and returns the insights.
#"Unusual" = the amount is much larger than the average transaction. 

from app.services.storage import transactions_db

def dectect_anomalies():
    if not transactions_db:
        return {"message": "There are no transaction avaliable!"} 
    
    #Step 1: calculate the average transaction amount (negative amounts)
    spending = []
    for t in transactions_db:
        if t["amount"] < 0:
            spending.append(t)
    
    #Gaurd clause: if no spending transactions exsist
    if not spending:
        return {"message": "No spending transactions avaliable!"} 
    
    #step 2: calculate the average spending amount 
    #abs() removes negative signs 
    total = 0
    for t in spending:
        total += abs(t["amount"])

    average = total / len(spending)


    #step 3: flag anything more than 2x the average spent
    THRESHOLD = 2 #This is the multiplier for the average to determine if a transaction is an anomaly

    anomalies = []
    for t in spending:
        if abs(t["amount"]) > average * THRESHOLD:
            anomalies.append(t)

   

    #step 4: return the anomalies
    return {
        "average_transaction": round(average,2),
        "threshold_used": f"{THRESHOLD}x average = ${round(average * THRESHOLD, 2)}",
        "anomalies_found": len(anomalies),
        "anomalies": anomalies
    }