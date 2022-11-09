# Name: Jeremy Duncan
# Date: November 9th 2022
# Machine: 2021 14" MacBook Pro

# Used for current time and date
from time import strftime

class Call:
    def __init__(self, client_id=0, client_name="Unknown", client_phone="Unknown"):
        self.client_id = client_id
        self.client_name = client_name
        self.client_phone = client_phone
        self.call_date = strftime("%m/%d/%Y")
        self.call_time = strftime("%H:%M")
        
    