from Post import Post
class User():
    def __init__(self , name):
        self.name = name
        self.friends = []
        self.posts = []
    
    def addPost(self , text):
        newPost = Post(text , self)
        self.posts.append(newPost)
    
    def addFriend(self , user):
        self.friends.append(user)


if __name__ == "__main__":
    dani = User("Dani")
    Beni = User("Beni")
    Shimon = User("Simon")
    hadas = User("hadas")
    hadas.addFriend(Shimon)
    hadas.addFriend(Beni)
    hadas.addFriend(dani)
    Beni.addFriend(dani) 
    Shimon.addFriend(dani) 

