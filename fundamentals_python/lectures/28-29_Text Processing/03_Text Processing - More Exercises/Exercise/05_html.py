article_title = input()
content_of_article = input()
print(f"<h1>\n{4 * ' '}{article_title}\n</h1>")
print(f"<article>\n{4 * ' '}{content_of_article}\n</article>")
comment = input()
while comment != "end of comments":
    print(f"<div>\n{4 * ' '}{comment}\n</div>")
    comment = input()


"""CEO  """


title_first_line = input()
content_second_line = input()

comments_enter = input()
print(f"<h1>\n     {title_first_line}\n</h1>")
print(f"<article>\n    {content_second_line}\n</article>")

while comments_enter != "end of comments":
    print(f"<div>\n    {comments_enter}\n</div>")
    comments_enter = input()
