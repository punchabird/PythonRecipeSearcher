import random
from bs4 import BeautifulSoup
#remember not to name your program the same as your module
from googlesearch import search

#create an empty list to store our search resultsin
results = []

#ask what dish we're searching for recipes to
recipe_request = input("What\'s a dish you'd like to cook? >") + "recipe"
print(recipe_request)

#run a google search, get 10 results, store in list
def recipe_lookup(query): #I need to fix this part in order for things to work, I think 
	for j in search(query, tld=".com", num=10, stop=1, pause=2):
		results.append(j)

#pick out one recipe at random
selected_recipe = random.choice(results)

#run our google search
recipe_lookup(recipe_request)

#print our recipe
print(selected_recipe)
