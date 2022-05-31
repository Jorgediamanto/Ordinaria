




class UserAccount:

    def __init__(self, alias, email, tweets, followers, timeline):
        self.alias = alias #string {es un nombre}
        self.email = email #string {es un email}
        self.tweets = tweets #List of strings [time(string)/message(string)/sender(string)]  {cada tweet tiene 3 componentes, por lo que un tweet estará compuesto por 3 string independientes, lo único que en este caso el sender es el mismo}   
        self.followers = followers #List of strings [lista de alias]  {lista de nombres de los seguidores}
        self.timeline = timeline #List of strings [time(string)/message(string)/sender(string)]   {lo mismo que en los tweets, pero esta vez si hay diferentes senders}

    #este método recibe la instancia del usuario al que desea seguir
    def follow(self,user):

        f=0
        for y in range(len(user.followers)):
            if user.followers[y] == self.alias:
                f=1

        if user.alias == self.alias:
            f=2

        if f==2:
            print("Un usuario no se puede seguir a sí mismo")
        elif f==1:
            print("Este usuario ya sigue a "+user.alias)
        else:
            user.followers.extend([self.alias])
            user.timeline.extend(self.tweets)


    def tweet(self,tweet):
        self.tweets.extend(tweet)

    def tweet_aux(self):
        pass






user1 = UserAccount("elvargas","elvarginhos@gmail.com",[["12/10/2001 22:10","Hoy he nacido","elvargas"],["12/10/2091 22:10","Hoy he muerto","elvargas"]],["roberto"],[["31/01/2031 22:10","Adiós","roberto"]])
user2 = UserAccount("roberto","roberto@yahoo.com",[["31/01/2031 22:10","Adiós","roberto"]],["elvargas"],[["12/10/2001 22:10","Hoy he nacido","elvargas"],["12/10/2091 22:10","Hoy he muerto","elvargas"]])
user3 = UserAccount("fede","federico@uax.es",[["30/6/2022 22:10","no me sigue nadie D:","fede"]],[],[])



#user1.follow(user3)
#print(user3.timeline)


tweet1 = [["03/04/1990 21:10"],["slavaje "],["fede"]]

user3.tweet(tweet1)

    
print(user3.tweets)
    



















