import datetime

class Tweet:

    n=0

    def __init__(self,message,sender):
        
        if self.n==0:
            gcr = datetime.datetime.today()
            self.time = gcr
            self.ayuda()

        if len(message)>140:
            raise ValueError("El tweet debe ser igual o menor a 140 caracteres")

        self.message = message


        self.sender = sender

    def ayuda(self):
        self.n=self.n+1
        



class DirectMessage(Tweet):

    def __init__(self,message,sender,receiver):
        super().__init__(message,sender)
        self.receiver = receiver

class Retweet(Tweet):

    def __init__(self,tweet,resender):
        x1=tweet.time
        super().__init__(tweet.message,tweet.sender)
        self.resender = resender
        self.time = x1
        resend_time = datetime.datetime.today()
        self.resend_time = resend_time




tweet1 = Tweet("hola","Jorge")
tweet2 = DirectMessage("soy raul","Raúl","Jorge")
n= int(input("pulse 1 si dese retweet"))
if n==1:
    tweet3 = Retweet(tweet1,"Raúl")


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
print(tweet3.resend_time)




















