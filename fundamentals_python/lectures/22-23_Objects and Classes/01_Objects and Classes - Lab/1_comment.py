class Comment:
    def __init__(self, username,content,likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

comment1 = Comment("user1", "I like this book")
print(comment1.username)
print(comment1.content)
print(comment1.likes)

comment2 = Comment(username="user2", content=" I like this", likes= 6)
comment3 = Comment( "user3", 'I dont like this', 3)

print(f" I'm a {comment3.username}! {comment3.content} book!  I giv him {comment3.likes} points")



