class UserAccount:
    usuarios = []

    def __init__(self, alias, email, tweets, followers, timeline):
        self.alias = alias
        self.email = email
        self.tweets = tweets
        self.followers = followers
        self.timeline = timeline
        self.usuarios.append(self)

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

    def tweet(self,tweet):
        tweet.extend([self.alias])
        self.tweets.extend([tweet])
        for x in range(len(self.usuarios)):
            for y in range(len(self.followers)):
                if self.usuarios[x].alias == self.followers[y]:
                    self.usuarios[x].timeline.extend([tweet])

    def organizar_timeline(self): #organiza timelibne por fecha publicado
        pass

    def organizar_followers(self): #organiza followers en orden alfabetico
        pass

user1 = UserAccount("user1","user1@gmail.com",[["12/10/2022","Hola he nacido","user1"],["13/10/2022","Primer dia con vida pog","user1"]],["user2"],[["02/11/2012","solvaje","user2"]])
user2 = UserAccount("user2","user2@gmail.com",[["12/10/2022","VIVA SALAMANACA","user2"]],["user1"],[["12/10/2022","Hola he nacido","user1"],["13/10/2022","Primer dia con vida pog","user1"]])
user3 = UserAccount("user3","user3@gmail.com",[["12/10/2022","nadie me sigue sadge","user1"]],[],[])


tweet1=["07/75/2022","Rabadins"]

user2.tweet(tweet1)


print("\n")
print(user1.followers)
print(user1.tweets)
print(user1.timeline)

print("\n")
print(user2.followers)
print(user2.tweets)
print(user2.timeline)

print("\n")
print(user3.followers)
print(user3.tweets)
print(user3.timeline)

















