import random

def split_word(word):
    return [char for char in word]

word_list = ["bird"]
word  = random.choice(word_list)

attempt = 0

split = split_word(word)

guessed_word = ["_ " for char in word]


for x in range(5):

    user_input = input("Buchstaben eingeben: ")

    if user_input in word:
        print("Correct")
        for i in range(len(word)):
            if split[i] == user_input:
                guessed_word[i] = user_input
        print(guessed_word)
