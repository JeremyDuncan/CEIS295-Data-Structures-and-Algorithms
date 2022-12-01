# Name: Jeremy Duncan
# Date: December 1st 2022

class Client:
    def __init__(self, client_id=0, first_name="unknown", last_name="unknown", phone="unknown", email="unknown"):
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email

    # classes that compare object must implement __eq__ method and __lt__ methods
    # __lt__ means "less than" and must return boolean value
    # __eq__ means "equals" and it must return a boolean value
    def __lt__(self, other):
        return self.__client_id < other.__client_id

    def __le__(self, other):
        return self.__client_id <= other.__client_id

    def __eq__(self, other):
        return self.__client_id == other.__client_id

    # __str__() is automatically called when you print the object
    def __str__(self):
        return "[" + str(self.__client_id) + "]"

    # getters & setters
    def get_client_id(self):
        return self.__client_id 

    def get_client_id(self, client_id):
        self.__client_id = client_id

    def get_first_name(self):
        return self.__first_name

    def get_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def get_last_name(self, last_name):
        self.__last_name = last_name

    def get_phone(self):
        return self.__phone

    def get_phone(self, phone):
        self.__phone = phone

    def get_email(self):
        return self.__email

    def get_phone(self, email):
        self.__email = email
