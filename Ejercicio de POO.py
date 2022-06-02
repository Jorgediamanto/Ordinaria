import datetime

class UserAccount:
    usuarios = []

    def __init__(self, alias, email, tweets, followers, timeline):
        self.alias = alias
        self.email = email
        self.tweets = tweets
        self.followers = followers
        self.timeline = timeline
        self.usuarios.append(self)

    #este método recibe la instancia del usuario al que desea seguir
    def follow(self, user):
        f=0
        for x in range(len(user.followers)):
            if user.followers[x] == self.alias:
                f=1

        if user.alias == self.alias:
            print("Un usuario no se puede seguir a si mismo")
        elif f==1:
            print("Este usuario ya le sigue")
        else:
            user.followers.extend([self.alias])
            self.timeline.extend(user.tweets)
            self.organizar_timeline()
            user.organizar_followers()
            

    #este metodo recibe el tweet que se desea publicar
    def tweet(self,tweet):
        tweet.extend([self.alias])
        self.tweets.extend([tweet])
        for x in range(len(self.usuarios)):
            for y in range(len(self.followers)):
                if self.usuarios[x].alias == self.followers[y]:
                    self.usuarios[x].timeline.extend([tweet])
                    self.usuarios[x].organizar_timeline()

    def organizar_timeline(self): #organiza timeline por fecha publicado (mas reciente a menos como twitter)
        
        x11 = []
        for x in range(len(self.timeline)):
            time_datetime = datetime.datetime.strptime(self.timeline[x][0], "%d/%m/%Y")
            x11.append(time_datetime)

        x11.sort()
        x12=[]
        for y in range(len(self.timeline)):
            for z in range(len(self.timeline)):
                time_datetime = datetime.datetime.strptime(self.timeline[z][0], "%d/%m/%Y")
                if time_datetime==x11[y]:
                    x12.append(self.timeline[z])
            
        x12.reverse()
        self.timeline = x12
        

    def organizar_followers(self): #organiza followers en orden alfabetico
        self.followers.sort()

user1 = UserAccount("user1","user1@gmail.com",[["12/10/2022","Hola he nacido","user1"],["13/10/2022","Primer dia con vida pog","user1"]],["user2"],[["02/11/2011","solvaje","user2"]])
user2 = UserAccount("user2","user2@gmail.com",[["02/11/2011","solvaje","user2"]],["user1"],[["12/10/2022","Hola he nacido","user1"],["13/10/2022","Primer dia con vida pog","user1"]])
user3 = UserAccount("user3","user3@gmail.com",[["12/10/2012","nadie me sigue sadge","user3"]],[],[])


tweet1=["07/05/2022","Rabadins"]

user2.tweet(tweet1)
user2.follow(user3)
#user1.follow(user3)




print(user1.timeline)

















