import requests as r
import random as rd
import pyfiglet as pf

url = "https://icanhazdadjoke.com/search"
ascii_text = pf.figlet_format("DAD JOKE MACHINE")
user_input = input("Search Term: ")

res = r.get(url,
headers={"Accept": "application/json"},
params={"term": user_input}).json()

num_jokes = res["total_jokes"]
random_joke = rd.randint(0,num_jokes-1)

if num_jokes > 1:
    print(f"There are {num_jokes} jokes for '{user_input}'")
    print(res["results"][random_joke].get('joke'))
elif num_jokes == 1:
    print("There is one joke")
    print(res["results"][0].get('joke'))
else:
    print("There are no Jokes")





