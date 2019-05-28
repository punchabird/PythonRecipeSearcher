import random
from bs4 import BeautifulSoup
#remember not to name your program the same as your module
from googlesearch import search
import webbrowser

recipeList = []

def findRecipe():
    recipeRequest = input("What\'s a dish you'd like to cook? >" + " recipe")
    print("Searching for \'" + recipeRequest + "\'...")
    for url in search(recipeRequest, tld="com", num=10, start=1, stop=10, only_standard=True):
        recipeList.append(url)
        return printRecipe(recipeList)

def printRecipe(resultsList):
    if len(resultsList) > 0:
        
        #print a randomly selected list item, open in browser, then delete it from the list    
        i = random.randint(0, len(resultsList) - 1)
        print(resultsList[i])
        webbrowser.open(resultsList[i])
        del resultsList[i]

        #make this next part into a different function      
        doneSearching = input("Satisfied with this recipe (y/n)? >")
        if doneSearching == "y":
            print("Cool. Let's get cooking!")
        else:
            differentDish = input("Search for a different dish (y/n)? >")
            if differentDish == "y":
                return findRecipe()
            else:
                return printRecipe(recipeList)


    

    else:
        print("You're out of results! Search again.")
        return findRecipe()




    '''print(resultsList[i])
    webbrowser.open(resultsList[i])
    del resultsList[i]'''












'''
recipeList = []
doneSearching = False

while not doneSearching: #as long as I'm not done searching, keep me in a loop here
    recipe_request = input("What\'s a dish you'd like to cook? > ") + " recipe"
    print("Searching for \'" + recipe_request + "\'...")

    #get the first 10 results from google searching my recipe
    for url in search(recipe_request, tld="com", num=10, start=1, stop=10, only_standard = True):
        recipeList.append(url) #add each of the URLs to a list
        differentDish = False

        while not differentDish:
            i = random.randint(0, len(recipeList) - 1)
            print(recipeList[i])
            webbrowser.open(recipeList[i])
            del recipeList[i]
            
            chooseThisRecipe = input("Satisfied with this recipe (y/n)? > ")

            if chooseThisRecipe == "y":
                differentDish = True
                doneSearching = True
                print("Cool. Let's get cooking!")
            
            else: 
                searchSameDish = input("Would you like another recipe for the same dish (y/n)? >")
                if searchSameDish == "n":
                    differentDish = True

                    
            if differentDish == True:
                break

        if doneSearching == True:
            break'''





                    










#three scenarios 
#first - initial search 
#second - give me a different result from my list 
#third - initiate another search, this time with different input

'''search for recipe 
put into array
print the first result, then delete that item from the array 
ask if you want to get a different recipe or look for a new dish
if yes, ask which one to look for (recipe/dish)
if recipe, randomly pull from the array again
if dish, run the entire search over


'''

