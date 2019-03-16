EECS 337 Project 2

Git Repo: https://github.com/leaf715/337-Project-2

Team Number: 14

Students:
Brennan Adler
Joe Chookaszian
Shu Han
Daniel McGrory

Language: Python 3.7

Standard modules: copy, itertools, json, random, re, sys, urllib
Nonstandard modules:
 - BeautifulSoup: Can be installed via "pip install beautifulsoup4"

Instructions to run:

Run the file recipe_parser.py using python as follows:
"python recipe_parser.py URL"
where URL is the url of the desired recipe to be analyzed. recipe_parser.py can only handle one recipe at a time.

If you do not include a recipe, the program will resort to using a default recipe instead.
That default recipe can be found here: https://www.allrecipes.com/recipe/234534/beef-and-guinness-stew/

Once you run recipe_parser.py, you will be presented with a print out of the regular recipe parsed into:

The recipe title
An ingredient list containing each ingredient decomposed into its quantity, measurement, description, ingredient, preparation
The recipe steps
The primary and secondary methods used to prepare and cook the recipe
The tools required to cook the recipe

Below this print out, you will be prompted by a menu asking you to provide an input in the form of a number/letter to
select the type of transformation you wish to perform. The numbers and letters and their corresponding transformation
are listed in this prompt but will be listed again below:
1 Vegetarian
2 Healthy
3 Pescatarian
4 Cajun
q Quit Program

Upon selecting a choice, you will be provided with a print out of the transformed recipe parsed into:
The transformed recipe title
The transformed ingredient list
The transformed recipe steps

You will also be prompted with the same menu as before below the transformed recipe printout. Follow the instructions as
before in order to transform the original recipe to any of the options or to quit the program.