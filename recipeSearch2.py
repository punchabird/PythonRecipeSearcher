import random
from bs4 import BeautifulSoup
#remember not to name your program the same as your module
from googlesearch import search
import webbrowser

recipeList = []

def findRecipe():
    recipeRequest = input("What\'s a dish you'd like to cook? > ") + " recipe"
    print("Searching for \'" + recipeRequest + "\'...")
    for url in search(recipeRequest, tld="com", num=10, stop=10, only_standard=True):
        recipeList.append(url)
        return printRecipe(recipeList)

def printRecipe(resultsList):
    if len(resultsList) > 0: #only spit out a result if the list has stuff
        #print a randomly selected list item, open in browser, then delete it from the list    
        i = random.randint(0, len(resultsList) - 1)
        print(resultsList[i])
        webbrowser.open(resultsList[i])
        del resultsList[i]

        return checkIfDone()

    else: #start a new search if the list is empty
        print("You're out of results! Search again.")
        return findRecipe()

def checkIfDone():        
        #ask if the user is happy with their recipe      
        doneSearching = input("Satisfied with this recipe (y/n)? >")
        if doneSearching == "y":
            print("Cool. Let's get cooking!")

        else: #if not, ask if they want to search for a different dish
            differentDish = input("Search for a different dish (y/n)? >")
            if differentDish == "y":
                return findRecipe()
            else:
                return printRecipe(recipeList)

#call findRecipe to start it
findRecipe()
