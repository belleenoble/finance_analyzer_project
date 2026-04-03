# Finance_Analyzer_Project
A full-stack personal finance analyzer that allows users to upload financial statment data (.csv) files or manually input transations, then processes the data to detect spending patterns and provide actionable insights. Built with React (frontend) and FastAPI (backend), featuring file upload, API integration, and real-time data handling. 

# Finance Analyzer
A finance analysis project for cleaning, analyzing, and visualizing financial data.

## Project Overview 
This finance analyzer should help users:
- Upload or manually input financial transaction data
- save transaction history for future sessions
- analyze data to detect anomalies and unsual spending patterns overtime
- generate summaries and visualizations
- provide actionable insights for better financial decisions. 

## Goals
- Keep data processing reproducible
- Seperate raw data, code, outputs and documents
- Make results easy to review and compare across each session.
- Allow users to understand their financial spending habits.

## Setup and Running the Project
1.) Clone the repository
```bash
git clone https://github.com/belleenoble/finance_analyzer_project.git

cd finance_analyzer
```
2.) Setup the backend (FastAPI)
```bash
cd backend

python -m venv .venv

source / venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```
The backend server should run at: http://localhost:8000

3.) Setup the frontend (React)
```bash
cd frontend

npm install

npm start
```
The frontend server should run at: http://localhost:5173
