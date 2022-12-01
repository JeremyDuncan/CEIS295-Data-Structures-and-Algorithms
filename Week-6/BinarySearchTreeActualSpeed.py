# Name: Jeremy Duncan
# Date: December 1st 2022

from datetime import date
import sys
import random
import time
from BinarySearchTree import BinarySearchTree
from Client import Client

# display name and date in input
print("Name:", "Jeremy Duncan")
print("Date:", date.today())
print("Machine: 2021 14\" Macbook Pro")
print()

clients = []

input_file_name = "ClientData.csv"
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on the commas
        s = line.split(',')
        client_id = int(s[0])  # convert to number
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

my_bst = BinarySearchTree()

# ===============================================================================
# Scenario 1: Printer Queue or Call Queue
# ===============================================================================
section_title = "Scenario: Printer Queue or Call Queue"
print(section_title)
print("-" * len(section_title))

# how long does it take to add records from the front (smallest)
start_time = time.time()

for i in range(num_records):
    my_bst.insert(clients[i])

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records: {:.6f}".format(total_time))

# how long does it take to remove the records
start_time = time.time()

for i in range(num_records):
    my_bst.insert(clients[i])

end_time = time.time()
total_time = end_time - start_time
print("Seconds to remove records: {:.6f}".format(total_time))

# ===============================================================================
# Scenario 2: Customer Service Center
# ===============================================================================
answer = input("Continue (y/n)?")
if answer.lower() != "y":
    sys.exit()

section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

for i in range(num_records):
    my_bst.insert(clients[i])

# how long does it take to randomly display 1000 records?
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_bst.search(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to display 1000 random records: {:.6f}".format(total_time))

# ===============================================================================
# Scenario 3: Call Center
# ===============================================================================
answer = input("Continue (y/n)?")
if answer.lower() != "y":
    sys.exit()

section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))

for i in range(num_records):
    my_bst.insert(clients[i])

# how long does it take to add records, randomly display 1000 records, and
# randomly remove 1000 records?
start_time = time.time()

# add records
current_id = 100001 + num_records + 1
for i in range(1000):
    my_bst.insert(Client(current_id))
    current_id += 1

# display random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_bst.search(Client(random_num)))

# remove random num_records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    my_bst.remove(Client(random_num))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add, display, and remove records: {:.6f}".format(total_time))
