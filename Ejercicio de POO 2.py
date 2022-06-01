import datetime

class Tweet:

    def __init__(self,message,sender):
        gcr = datetime.datetime.today()
        self.time = gcr
        self.message = message
        self.sender = sender


class DirectMessage(Tweet):

    def __init__(self,message,sender,receiver):
        super().__init__(message,sender)
        self.receiver = receiver

class Retweet(Tweet):

    def __init__(self,message,sender,resender):
        super().__init__(message,sender)
        self.resender = resender


tweet1 = Tweet("hola","Jorge")
tweet2 = DirectMessage("zapato","Raúl","Jorge")
tweet3 = Retweet("hola","Jorge","Raúl")


print(tweet1.message)
print(tweet1.sender)
print(tweet1.time)


print(tweet2.message)
print(tweet2.sender)
print(tweet2.time)
print(tweet2.receiver)


print(tweet3.message)
print(tweet3.sender)
print(tweet3.time)
print(tweet3.resender)



















