# Name: Jeremy Duncan
# Date: November 17th 2022
# Machine: 2021 14" MacBook Pro

from MergeSort import MergeSort
from Client import Client
from datetime import date
import time     # use this library to time code executions

# display name and date in input
print("Name:", "Jeremy Duncan")
print("Date:", date.today())
print("Machine: 2021 14\" Macbook Pro")
print()

# input_file_name = 'ClientData100.csv'
# input_file_name = 'ClientData1000.csv'
input_file_name = 'ClientData10000.csv'
# input_file_name = 'ClientData100000.csv'

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
section_title = "Scenario: Sorting " + str(num_records) + " Queue or Call Queue" 
print(section_title)
print("-" * len(section_title))



# how long does it take to sort the record
start_time = time.time()
    
MergeSort.sort(clients)    
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to sort {0} records: {1:.6f}".format(num_records, total_time))

# Display sorted list
# for clt in clients:
#     print(clt)
