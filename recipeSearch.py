import random
from bs4 import BeautifulSoup
#remember not to name your program the same as your module
from googlesearch import search
import webbrowser

#ask what dish we're searching for recipes to
recipe_request = input("What\'s a dish you'd like to cook? > ") + " recipe"
print("Searching for \'" + recipe_request + "\'...")


# generate 10 results per page, return i'th result, stop after that
doneSearching = False
while not doneSearching: 
	#generate a random number to choose which result to return
	i = random.randint(0,9) 
	for url in search(recipe_request, tld="com", num=10, start=i, stop=1):
		print(url) # search() returns an iterator
		webbrowser.open(url)
		searchAgain = input("Search for a different recipe (y/n)? > ")
		if searchAgain == "n":
			doneSearching = True
			break
		
			



