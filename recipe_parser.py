import urllib.request
# pip3 install BeautifulSoup4
from bs4 import BeautifulSoup
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

def main():
    #Open URL
    with urllib.request.urlopen('https://www.allrecipes.com/recipe/173906/cajun-roasted-pork-loin/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=8722%20referringContentType%3Drecipe') as response:
        page = response.read()
    recipe = BeautifulSoup(page, 'html.parser')

    title, ingredients, steps = getItems(recipe)

    print(title)
    print(ingredients)
    print(steps)

# Get HTML elements we need
def getItems(recipe):
    title = recipe.find('h1', attrs={'class': 'recipe-summary__h1'}).text.strip()

    ingredients = []
    ingred = recipe.find_all('li', attrs={'class': 'checkList__line'})
    for i in ingred:
        if i:
            if i.text.strip() != 'Add all ingredients to list' and i.text.strip() !='':
                ingredients.append(i.text.strip())
    steps =[]
    prep = recipe.find_all('span', attrs={'class': 'recipe-directions__list--item'})
    for i in prep:
        if i:
            if i.text.strip() != '':
                steps.append(i.text.strip())
    return title, ingredients, steps

if __name__ == "__main__":
    main()
