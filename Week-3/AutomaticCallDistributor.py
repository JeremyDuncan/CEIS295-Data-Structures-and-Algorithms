# Name: Jeremy Duncan
# Date: November 9th 2022
# Machine: 2021 14" MacBook Pro

import random
import time
from Queue import Queue
from Call import Call
from datetime import date

# display name and date in input
print("Name:", "Jeremy Duncan")
print("Date:", date.today())
print("Machine: 2021 14\" Macbook Pro")
print()

calls = []

# Read call records into the list
input_file_name = "ClientData.csv"
with open(input_file_name) as infile:
    for line in infile:
        # Split line based on commas
        s = line.split(',')
        client_id = int(s[0])
        client_name = s[1]
        client_phone = s[2]

        # Create a call object based on data from line
        a_call = Call(client_id, client_name, client_phone)

        # Add a Call object to the list
        calls.append(a_call)

calls_waiting = Queue()
call_number = 0

# how long is the simulation?
seconds = int(input("How many seconds do you want to simulate? (y/n): "))

# Run the simulation for the given number of seconds
for i in range(seconds):
    print("-" * 40)
    time.sleep(2) # Pause app for given time
    random_event = random.randint(1, 3)
    
    # do event based on random number generated
    if random_event == 1:
        print("Call received. Caller added to queue. ")
        calls_waiting.enqueue(calls[call_number])
        call_number += 1 # Set-up the next call
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())
    elif random_event == 2:
        print("Call sent to representative for service. ")
        if calls_waiting.get_length() > 0:
            print("Caller information:")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty.")
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())
    else:
        print("Nothing happened during this second in time. ")
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())
print("\tThe 'Automatic Call Distributor' simulation has completed." )
    
    