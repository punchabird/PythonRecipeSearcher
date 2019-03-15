# RandomRecipeGenerator
Random recipe generator

## Project Requirements
1. Take some input specifying a kind of food
2. Append the string "recipe" to input
3. Run a Google search on (input + "recipe")
4. Generate a random number 'i' between 1-10
5. Select i'th Google search result
6. Output the text of the recipe

## Tools we might be able to use

**BeautifulSoup**

[Website](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Python library for pulling data out of HTML files. We can use this
to extract recipe text after selecting a webpage from our recipe
search. 

**Google**

[Website](https://python-googlesearch.readthedocs.io/en/latest/)

Allows you to make Google searches from Python. BeautifulSoup is
a dependency. 

**urllib3**

[Website](https://urllib3.readthedocs.io/en/latest/)

[HTTP client for for Python. Looks like you can get the HTML page
of the URL, then use BeautifulSoup to parse.](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe)

[Also here](https://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup)

**Instructions on how to format output in terminal with Python**

[GeeksforGeeks showing how to do this on Linux](https://www.geeksforgeeks.org/formatted-text-linux-terminal-using-python/)


_Note_: Let's uh, let's just stick to Python for this because it's
a language we both know (you more than me, but w/e). 

## Key project milestones and deadlines

**Week of March 4**
* Finish initial project planning and tools research
* Assign tasks to Urnfish
   - Fish: design interface for obtaining user input, retrieve Google search results based on input from user
   - Urn: process Google search results, return appropriate information to user

**Week of March 11**
* Phase 1: basic implementation - take input, retrieve search results, return link (print to console)

**Week of March 18** 
* Phase 2: return link and open page in browser

**Week of March 25** 
* Phase 3: print recipe to console
* Project should be completed
