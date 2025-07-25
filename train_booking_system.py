'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under U.S. Railways. 
'''
from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time") 

    def getfare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is ${randint(222,5555)}")

t = Train(12399)
t.book("Surat","Delhi")
t.getStatus()
t.getfare("Surat","Delhi")