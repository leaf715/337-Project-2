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
    parsedIngreds = parseIngred(ingredients)
    parsedSteps = parseSteps(steps)
    print(title)
    print(ingredients)
    print(steps)

def parseSteps(steps):
    print("my steps")
    return 0

def parseIngred(ingredients):
    descriptors = ['all-purpose','fresh','dried','extra-virgin','ground', 'boneless']
    ingreds = []
    quantity = []
    measurement = []
    descriptor = []
    preparation = []
    num = 0

    for i in ingredients:
        comma = i.split(', ',2)
        first = comma[0]
        words = first.split()
        print(words)
        for x in range(len(words)):
            if words[x] in descriptors:
                descriptor.append(words[x])
                del words[x]
                break


        if len(comma) > 1:
            preparation.append(comma[1])
        else:
            #check if word ends in 'ed'
            #if so, make prep that and remove from array
            preparation.append('no prep')
            for x in range(len(words)):
                if words[x].endswith('ed'):
                    preparation[num]=words[x]
                    del words[x]
                    break


        #if first word has number in first digit
        if words[0][0].isdigit():
            quantity.append(words[0])
            #if only 2 word probably just number and ingredient
            if(len(words) < 3):
                ingreds.append(words[1])
                measurement.append('')
            else:
                mynum = 1
                if('(' in words[1] and ')' not in words[1]):
                    mymeas = ''
                    while(')' not in words[mynum]):
                        mymeas = mymeas + words[mynum] + " "
                        mynum = mynum + 1
                    mymeas = mymeas + words[mynum]
                    measurement.append(mymeas)
                else:
                    measurement.append(words[1])


                myIngred = words[mynum+1]
                for w in range(mynum+2, len(words)):
                    myIngred = myIngred + " " + words[w]
                ingreds.append(myIngred)
        else:
            quantity.append("to taste")
            measurement.append('')
            myIngred = words[0]
            for w in range(1, len(words)):
                myIngred = myIngred + " " + words[w]
            ingreds.append(myIngred)

        print(first)
        print(quantity[num])
        print(measurement[num])
        print(ingreds[num])
        print(preparation[num])
        print()
        num = num +1

    return 0

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
