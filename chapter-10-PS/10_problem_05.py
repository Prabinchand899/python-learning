

'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways'''

from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,f,to):
        print(f"Ticket is booked in train no. : {self.trainNo} from {f} to {to}")

    def get_status(self):
        print(f"Train no. {self.trainNo} is running on time.")

    
    def fare_info(self,f,to):
        print(f"Ticket fare in train no. {self.trainNo} from {f} to {to} is {randint(22,543)}")

    
        


t = Train(3332)
t.book("banbasa","Delhi")
t.get_status()
t.fare_info("Banbasa","Delhi")