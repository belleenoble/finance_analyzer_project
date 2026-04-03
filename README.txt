# Project Name 
- Smart Expense Insight Dashboard

===================================================

## Description
The Smart Expense Insight Dashboard is a web-based tool that helps users understand 
their spending behavior by analyszing transation data from CSV files

It automatically categorizes expennses, detects unual spending patterns, 
identifies recurring subscriptions, and generates actionable finciacial insights.

This project was built to solve a common problem: most people have access to their finacial data,
but lack clear, automated insights into where their money is going. 

===================================================
## Features
-CSV Transaction Upload
    -> Upload Bank/eported transaction files for analysis

-Automatic Cateforization
    -> Classifies transations into categories like groceries, dining, transportation,
    and subscriptions.

-Anomaly Dectection
    -> Identifies unusual spending such as large purchases or category spikes. 

-Subscription Dectection
    ->Detects recurring payments and estimates monthly costs/ anual costs

-Spending Insights Dashboard
    -> Summarizes total spending, top categories, and key financial patterns. 

-Plain-English Insights
    -> generates readable summaries:
            ex| "You spent 35% more on dining this month"

===================================================

## Tech Stack
- Backend: Python, FastAPI
- Data Processing: Pandas (https://www.geeksforgeeks.org/python/data-processing-with-pandas/)
- Front End: React or HTML, CSS (Jinja Templates)
- Containerization: Docker
- Other Tools: uviCorn

## Installation
Steps to run locally.
-OPTION 1 - run locally w/o docker
    ---
    git clone https://github.com/your-username/finance-analyzer.git
    cd finance-analyzer

    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

    pip install -r requirements.txt

    uvicorn app.main:app --reload
    ---
    then open your browser and go to 
    http://127.0.0.1:8000

-OPTION 2 - run with docker
    ---
    docker compose up --build
    ---
    then open:
    http://localhost:8000

## Usage
Export your transaction history from your bank as a CSV file
Open the app in your browser
Upload the CSV file
View:
categorized expenses
detected anomalies
recurring subscriptions
financial insights


## License