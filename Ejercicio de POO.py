


class UserAccount:

    def __init__(self, alias, email, tweets, followers, timeline):
        self.alias = alias #string {es un nombre}
        self.email = email #string {es un email}
        self.tweets = tweets #List of strings [time(string)/message(string)/sender(string)]  {cada tweet tiene 3 componentes, por lo que un tweet estará compuesto por 3 string independientes, lo único que en este caso el sender es el mismo}   
        self.followers = followers #List of strings [lista de alias]  {lista de nombres de los seguidores}
        self.timeline = timeline #List of strings [time(string)/message(string)/sender(string)]   {lo mismo que en los tweets, pero esta vez si hay diferentes senders}













