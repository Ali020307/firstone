with open("movies.txt", 'w') as file:
    file.write("spiderman.\n")
    file.write("revengers.\n")
    file.write("flash.\n")
with open("movies.txt", 'r') as file:
    content = file.read()
    print(content)