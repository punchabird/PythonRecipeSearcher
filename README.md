# Generating Random Recipes in Python
I wrote a thing with a bit of help from my girlfriend that takes
user input from the terminal and searches google for food recipes
using that input. 

It uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
and [googlesearch](https://python-googlesearch.readthedocs.io/en/latest/)
to make google searches from Python, and 
[webbrowser](https://docs.python.org/3.7/library/webbrowser.html) to open results
in the browser. 

The first version used a while loop to do everything and only got you one
result. I rewrote it using functions (recipeSearch2.py) calling each other so that it'd be
easier to implement the specific logic I wanted (searching for different
recipes of the same dish vs different dishes) and provide more results per search. 

I'm sure if this coding thing goes far enough, I'll look back at the last
commit for this one and chuckle. So embarrassing....
