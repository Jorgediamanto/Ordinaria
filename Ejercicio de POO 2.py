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

    def __str__(self):
        return '{}-{}-{} {}:{} - {}  -publicado por: {}'.format(self.time.year,self.time.month,self.time.day,self.time.hour,self.time.minute,self.message,self.sender)
        



class DirectMessage(Tweet):

    def __init__(self,message,sender,receiver):
        super().__init__(message,sender)
        self.receiver = receiver

    def __str__(self):
        return '{}-{}-{} {}:{} - {}  -enviado por: {} -recibido por {}'.format(self.time.year,self.time.month,self.time.day,self.time.hour,self.time.minute,self.message,self.sender,self.receiver)

class Retweet(Tweet):

    def __init__(self,tweet,resender):
        x1=tweet.time
        super().__init__(tweet.message,tweet.sender)

        self.resender = resender
        self.time = x1

        resend_time = datetime.datetime.today()
        self.resend_time = resend_time

    def __str__(self):
        return 'Publicado: {}-{}-{} {}:{} Reenviado: {}-{}-{} {}:{} - {}  -publicado por: {} -reenviado por: {}'.format(self.time.year,self.time.month,self.time.day,self.time.hour,self.time.minute, self.resend_time.year,self.resend_time.month,self.resend_time.day,self.resend_time.hour,self.resend_time.minute,self.message,self.sender,self.resender)




tweet1 = Tweet("hola muy buenas esta es una prueba para ver  si este tweet puede llegar a 140 caracteres exactamente y aún asi funcionar. Ha llegado mi hora","Jorge")
tweet2 = DirectMessage("soy raul","Raúl","Jorge")
n= int(input("pulse 1 si desea retweet: "))
if n==1:
    tweet3 = Retweet(tweet1,"Raúl")


#print(tweet1.message)
#print(tweet1.sender)
#print(tweet1.time)


#print(tweet2.message)
#print(tweet2.sender)
#print(tweet2.time)
#print(tweet2.receiver)


#print(tweet3.message)
#print(tweet3.sender)
#print(tweet3.time)
#print(tweet3.resender)
#print(tweet3.resend_time)


#print("\n")
#print(tweet1)
#print(tweet2)
#print(tweet3)
















