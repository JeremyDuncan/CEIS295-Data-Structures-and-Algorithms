# Name: Jeremy Duncan
# Date: November 25th 2022
# Machine: 2021 14" MacBook Pro

import random
from BinarySearch import BinarySearch
from Client import Client
from datetime import date
import time
from Quicksort import Quicksort     # use this library to time code executions

# display name and date in input
print("Name:", "Jeremy Duncan")
print("Date:", date.today())
print("Machine: 2021 14\" Macbook Pro")
print()

# input_file_name = 'ClientData100.csv'
# input_file_name = 'ClientData1000.csv'
# input_file_name = 'ClientData10000.csv'
input_file_name = 'ClientData100000.csv'

# create a list
clients = []

# read the records from the ClientData.csv file
# into Client objects and place the CLient objects into the list
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on the commas
        s = line.split(',')
        client_id = int(s[0]) # convert to number
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        # create client object using the data from the file
        clt = Client(client_id, f_name, l_name, phone, email)
        # add the client object to the list
        clients.append(clt)
   
# how many client objects do we have?
num_records = len(clients)

#===============================================================================
# Scenario 1: Sorting records in a from a datafile
#===============================================================================
section_title = "Scenario: Searching through " + str(num_records) + " Queue" 
print(section_title)
print("-" * len(section_title))

Quicksort.sort(clients)

# Start and end record numbers
start_record = 100001
end_record = start_record + num_records

# how long does it take to random linear search
start_time = time.time()
    
for i in range(1000):
    client_id = random.randint(start_record, end_record)
    clt = Client(client_id)
    result = BinarySearch.search(clients, clt)
    if result is None:
        print(clt, "was not found.")
    else:
        print(result) 
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to Binary search for 1000 random records: {:.6f}".format(total_time))
