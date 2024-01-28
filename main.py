import random
from english_words import get_english_words_set
from kjvbible import word as verses_list
web2lowerset = get_english_words_set(['web2'], lower=True)
web2upperset = []
for i, j in enumerate(web2lowerset):
    if len(j) == 5:
        web2upperset.append(j.upper())
with open('bible_words.txt', 'r') as f:
    file = f.read()
words_list = file.split("\n")



word_len = 5

# Define ANSI escape codes for text and background colors
class BackgroundColor:
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    GRAY = '\033[100m'
    RESET = '\033[0m'

def color_word(goal_word, player_word):
    return ["green" if player_word[i] == goal_word[i] else "yellow" if player_word[i] in goal_word else "gray" for i in range(word_len)]

# Rules
rules = """
All words will be in uppercase.
You will get six tries to guess a randomly picked word.
All words are from the Bible.
When you input a word, you will get your word colored.
If the background color of a letter in your word is gray, the letter is not in the word.
If the background color of a letter in your word is yellow, the letter is somewhere else in the word.
If the background color of a letter in your word is green, the letter is in the right place.
Every word is five letters long.
Every word must be an english word.
Enter q or quit to end the game.
Good luck!
"""
# Welcome player
print("Welcome to Bible Wordle!")
# Asks if the player knows the rules
knows_rules = input("Do you know the rules? (y/n): ")
# Checks if the player knows the rules
# If the player doesn't know the rules, print out the rules
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
if knows_rules.lower() == "n":
    print(rules)
while True:
    # goal_word = random.choice(words_list)
    goal_word = "ENOCH"
    tries = 0
    while True:
        tries += 1
        if tries == 7:
            print(f"Oh no, you lost! You have already used all six tries... :( The word was {goal_word}")
            break
        print("\nLet's play!")
        while True:
            word = input("Enter a word (uppercase): ")
            if word in {"Q", "QUIT"}:
                print("Okay, thanks for playing!")
                quit()

            if len(word) != word_len:
                print("Your word was not five letters long! Please enter a word five letters long.")
                continue
                
            if word != word.upper():
                print("Your word was not all uppercase. Please enter an ALL-UPPERCASE word.")
                continue
            
            contains = False
            for i in word:
                if not i in alphabet:
                    contains = True
            if contains:
                print("Your word contains symbols and/or numbers and/or spaces. Please enter word with five letters.")
                continue


            if not word in web2upperset:
                if word in words_list:
                    break
                else:
                    print("This is not a word in english.")
                continue

            break

        colors_list = color_word(goal_word, word)

        for i in range(word_len):
            if colors_list[i] == "green":
                print(f"{BackgroundColor.GREEN}{word[i]}{BackgroundColor.RESET} ", end="")
            elif colors_list[i] == "yellow":
                print(f"{BackgroundColor.YELLOW}{word[i]}{BackgroundColor.RESET} ", end="")
            else:
                print(f"{BackgroundColor.GRAY}{word[i]}{BackgroundColor.RESET} ", end="")

        if all(color == "green" for color in colors_list):
            if tries == 1:
                print(f"Yay! You guessed the word in {tries} try! You won!")
            else:
                print(f"Yay! You guessed the word in {tries} tries! You won!")
            verses = []
            for verse in verses_list:
                for item in verse:
                    if item.upper() == goal_word:
                        verses.append(verse)
            print()
            print(f"Here are two random verses that contain the word {goal_word}")
            print()
            rand_verses = []
            if len(verses) < 2:
                rand_verses.append(random.sample(verses, len(verses)))
            else:
                rand_verses.append(random.sample(verses, 2))
            for i in rand_verses:
                for j in i:
                    for k in j:
                        if k.upper() == goal_word:
                            print("\033[1m" + BackgroundColor.GREEN + k + BackgroundColor.RESET + "\033[0m ", end="")
                        else:
                            print(k + " ", end="")
                    print()
                print()

            break
    
    user_input = input("Do you want to play again (y/n)?\n")
    if user_input == "n":
        print("Ok! Bye!")
        break