from  Comment import Comment

class Post():
    def __init__(self , text , user):
        self.text = text
        self.user = user
        self.comments = []

    def addComment(self , commentText , user):
        newComment = Comment(commentText , user)
        self.comments.append(newComment)

if __name__ == "__main__":
    newPost = Post("new post" , "jijiji")
    newPost.addComment("commenting on the new post!" , "boris")
    newPost.addComment("why are you commenting?!" , "dikla")
    newPost.addComment("it's a great post!" , "boris")
    [print(comment.text) for comment in newPost.comments]
