




class UserAccount:

    usuarios = []

    def __init__(self, alias, email, tweets, followers, timeline):
        self.alias = alias #string {es un nombre}
        self.email = email #string {es un email}
        self.tweets = tweets #List of strings [time(string),message(string),sender(string)]  {cada tweet tiene 3 componentes, por lo que un tweet estará compuesto por 3 string independientes, lo único que en este caso el sender es el mismo}   
        self.followers = followers #List of strings [lista de alias]  {lista de nombres de los seguidores}
        self.timeline = timeline #List of strings [time(string),message(string),sender(string)]   {lo mismo que en los tweets, pero esta vez si hay diferentes senders}
        self.usuarios.append(self) 

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
            self.timeline.extend(user.tweets)



    def tweet(self,tweet):
        self.tweets.extend([tweet])
        #self.usuarios[0].timeline.extend([tweet])

        for x in range(len(self.usuarios)):
            for y in range(len(self.followers)):
                if self.usuarios[x].alias == self.followers[y]:
                    self.usuarios[x].timeline.extend([tweet])

        
            
            

    def tweet_aux(self):
        pass






user1 = UserAccount("user1","elvarginhos@gmail.com",[["12/10/2001 22:10","Hoy he nacido","user1"],["12/10/2091 22:10","Hoy he muerto","user1"]],["user2"],[["31/01/2031 22:10","Adiós","user2"]])
user2 = UserAccount("user2","roberto@yahoo.com",[["31/01/2031 22:10","Adiós","user2"]],["user1"],[["12/10/2001 22:10","Hoy he nacido","user1"],["12/10/2091 22:10","Hoy he muerto","user1"]])
user3 = UserAccount("user3","federico@uax.es",[["30/6/2022 22:10","no me sigue nadie D:","user3"]],[],[])



user1.follow(user3)



tweet1 = ["03/04/1990 21:10","slavaje ","user3"]

user3.tweet(tweet1)




#print(user1.usuarios[1].alias)
#print(user2.usuarios)
#print(user3.usuarios)



















