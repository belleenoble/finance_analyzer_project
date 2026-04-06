'''
-storage.py should store all data!
-Both manual and CSV uploads should append to this same list as long as the server is running. 
- Since both upload.py and transactions.py need to have it's data in the SAME list, importing data from
one solidified file lets both files point to the exact sam object in storage.

->basically everything depends on this file
'''

transactions_db = []