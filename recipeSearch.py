import random
from bs4 import BeautifulSoup
#remember not to name your program the same as your module
from googlesearch import search

#ask what dish we're searching for recipes to
recipe_request = raw_input("What\'s a dish you'd like to cook? >") + "recipe"
print(recipe_request)

#generate random number to choose which search result to return
i = random.randint(0,9)

# googlesearch lets you specify number of hits per page, which page to start searching from, and which page to stop
# since we can only specify start and stop PAGES and not HITS, we do the following:
# to return the i'th result out of the first 10 hits: get 1 result per page, start at page i, and stop after that 1 hit
for url in search(recipe_request, tld=".com", num=1, start=i, stop=1):
    print(url) # even though it's just 1 url, I'm putting it in a for loop because search() returns an iterator

# need to come back to this code it's not working, errors using search()
