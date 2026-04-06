''' 
Filename: main.py

Project: Smart Expense Insight Dashboard

File Purpose: Starting point of the backend for this project. 
This file should initalize the FastAPI application and define the API routes that
the frontend of the project will use to work together. (Front end on react).

Note: Project is a learning opportunity, where I will writing comments for most lines/
chunks of code, so I can actively learn and recall how the application is being made.

Note: React frontend and FastAPI backend run on different ports:
         Frontend: http://localhost:5173
         Backend:  http://127.0.0.1:8000

Run the Code: CHECK NOTES

Author: Belle Noble
Last Updated: 4/3/26
'''

# Imports FastAPI from the fastapi library.
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# imports the router frmo each route file -> its all brought together here!
from app.routes import upload, transactions, insights, anomalies

print("Main.py is loading")

# INITIALIZES the actual web application.
app = FastAPI() #"FastAPI()" is currently a CLASS that is creating a web server object.

#Allow React to interact with the backend (CORS)
app.add_middleware(
    CORSMiddleware, # react will be blocked without
    allow_origins=["http://localhost:5173"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Decorator -> when user goes to run the given URL, it will run the function
@app.get("/")
def read_root ():

    # Will return JSON 
    return {"message": "Backend of project is currently running"}


# Another route(endpoint) -> Checks if the server is alive
@app.get("/health")
def health_check():
    return{"status": "Okay"}

# note for later: main.py becomes the entry point + router manager 
# when we implement the different routes as seperate files.


#now that we are implementing different file routers, each route file is registered with a prefix
#*prefix = "api/upload" means every endpoint inside upload.py

#-> we are making it so that when you call each route, it takes all endpoints within 1 route file



app.include_router(upload.router,       prefix="/api/upload",       tags=["Upload"])
# app.include_router(transactions.router, prefix="/api/transaction",  tags=["Transactions"])
# app.include_router(insights.router,     prefix="/api/insights",     tags=["Insights"])
# app.include_router(anomalies.router,    prefix="/api/anomalies",    tags=["Anomalies"])