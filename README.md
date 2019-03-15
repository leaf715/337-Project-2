EECS 337 Project 2

Students:
Brennan Adler
Joe Chookaszian
Shu Han
Daniel McGrory

Language: Python 3.7

Standard modules: copy, itertools, json, random, re, sys, urllib
Nonstandard modules:
 - BeautifulSoup: Can be installed via "pip bs4"

Instructions to run:

Run the file recipe_parser.py using python as follows:
"python recipe_parser.py URL"
where URL is the url of the desired recipe to be analyzed. recipe_parser.py can only handle one recipe at a time.

Once you run recipe_parser.py, you will be presented with a print out of the regular recipe parsed into:
A ingredient list containing the quantity, measurement, description, ingredient, preparation

If you do not include a recipe, the program will resort to using a default recipe instead.
That default recipe can be found here: DEFAULT_RECIPE_URL