with open("kjvbiblewords.txt", "r") as file:
    text = file.read()

verses = text.split("\n")
word = []
for verse in verses:
    word.append(verse.split(" "))