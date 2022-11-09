# Name: Jeremy Duncan
# Date: November 9th 2022
# Machine: 2021 14" MacBook Pro

from Queue import Queue
from Call import Call
from datetime import date

# display name and date in input
print("Name:", "Jeremy Duncan")
print("Date:", date.today())
print("Machine: 2021 14\" Macbook Pro")
print()

calls= []

# Read call records into the list
input_file_name = "CallsData.csv"
with open(input_file_name) as infile:
    for line in infile:
        # Split line based on commas
        s = line.split(',')
        client_id = int( s[0] )
        client_name = s[1]
        client_phone = s[2]
        
        # Create a call object based on data from line
        a_call = Call(client_id, client_name, client_phone)
        
        # Add a Call object to the list
        calls.append(a_call)
        
calls_waiting = Queue()
call_number = 0
