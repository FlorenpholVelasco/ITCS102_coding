
movie_genre = ["scifi","romcom", "action", "drama"]
movie_title =[]

while True:
    ans = input("do you any movie (yes/no)")

    if ans.lower() == 'yes':
        print("what is its genre -- select from the list")
        for x in movie_genre:
            print(x)
        a_type = input("type ->")

        title = input("what is the title of the movie?")
        movie_title.append(title)
        continue
    
    else:
        print("thank you")
        break