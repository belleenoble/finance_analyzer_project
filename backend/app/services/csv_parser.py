#importing two built-in libraries 1) reads csv files 2) treats text as a file-like object
import csv 
import io

async def parse_csv(file: object) -> list:

    #reads contents in file (using await is cruicial for I/O operation)
    contents = await file.read()
    decoded = contents.decode("utf-8") #decoding so that csv.DictReader can work with normal strings

    #io.StringIO wraps the string so csv.DictReader thinks
    #its reading a real file. 
    reader = csv.DictReader(io.StringIO(decoded))

    #each row becomes a dict
    #example -> {"date": "2024-01-13", "description": "starbuks"}
    transactions = [row for row in reader]

    return transactions

