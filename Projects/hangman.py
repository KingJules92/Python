import random

# Function to split a String into single Characters
def split_word(word):
    return [char for char in word]

# Open the file in read mode

word  = random.choice(open("F:\GitHub\Python\Projects\sources\hangman.txt", "r").read().split())
print(word)
# Splitting the Word
secret_word = split_word(word)

guessed_word = ["_ " for char in word]


for x in range(11):

    print(guessed_word)
    print(" # "*10)
    user_input = input("Buchstaben eingeben: ")

    if user_input in word:
        for i in range(len(word)):
            if secret_word[i] == user_input:
                guessed_word[i] = user_input
        print(guessed_word)
        print(" # "*10)