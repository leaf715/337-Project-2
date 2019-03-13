import urllib.request
from itertools import chain
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
    parsedIngreds = parseIngred(ingredients)
    parsedIngreds = parseIngred(ingredients)
    print("ingredient list:")
    for i in range(len(parsedIngreds[0])):
        print("Q: " + parsedIngreds[0][i] +" M: " + parsedIngreds[1][i] +" D: " + parsedIngreds[2][i] +" I: " + parsedIngreds[3][i] +" P: " + parsedIngreds[4][i])
    parsedIngreds[3] = translateVegetarian(parsedIngreds[3])

    parsedSteps = parseSteps(steps)
    parsedTools = parseTools(title,parsedIngreds[4],parsedSteps)
    primary, otherMethods = parseMethods(title,parsedSteps)
    # print(steps)

def parseTools(title,prep,steps):
    possTools = ["","","","","","","","","","","","","","","","","","","","","","","","",""]
    return 0

def parseMethods(title,steps,prep):
    possPrim = ["roast","boil","broil","bake","stew","braise","toast","poach","sear","fry","sauté","fried","smoke","grill","steam"]
    possSec = ["chop","grate","stir","shake","mince","crush","squeeze","dice","mix","sprinkle","melt","stuff","rub","whisk","pour","strain","roast","boil","broil","bake","stew","braise","toast","poach","sear","fry","stir-fry","simmer","sauté","fried","stir-fried","smoke","grill","steam","barbaque"]
    #Get primary
    primary = ""
    primaryFound = False
    titleWords = title.lower().split()
    for i in titleWords:
        if i in possPrim:
            primary = i
            primaryFound = True
            break

    if not primaryFound:
        for x in steps:
            if "oven" in x:
                primary = "bake"
                primaryFound = True

    primaryDict = dict()
    if not primaryFound:
        for step in steps:
            for possibility in possPrim:
                if possibility in step.lower():
                    primaryDict[possibility] = primaryDict.get(possibility, 0) + 1
        primaryFound = True
        primary = get_max_in_dict(primaryDict)

    #Get Others
    othersDict = dict()
    for step in steps:
        for possibility in possSec:
            if possibility in step.lower():
                print(step + " " + possibility)
                othersDict[possibility] = othersDict.get(possibility, 0) + 1

    if(not primaryFound):
        primary = get_max_in_dict(othersDict)
        del othersDict[primary]

    for p in prep:
        if p != "no prep":


    print(primary)
    print(othersDict)
    return primary, othersDict

def parseSteps(steps):
    parsedSteps = []
    for i in steps:
        sentences = i.split('. ')
        if type(sentences) is list:
            for s in sentences:
                parsedSteps.append(s)
        else:
            parsedSteps.append(i)
    #for s in parsedSteps:
        #print(s)
    return parsedSteps

def parseIngred(ingredients):
    descriptors = ['all-purpose','fresh','dried','extra-virgin','ground', 'boneless','organic']
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

        hasD = False
        for x in range(len(words)):
            if words[x] in descriptors:
                descriptor.append(words[x])
                hasD = True
                del words[x]
                break
        if(not hasD):
            descriptor.append('')

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

        num = num +1

    return [quantity,measurement,descriptor,ingreds,preparation]

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

def translateVegetarian(ingredients):
    healthyReplacements = {"butter":"Coconut Butter", "honey":"Maple Syrup","eggs":"Bananas","milk":"Soy Milk","gelatin":"agar agar"}
    meats = ["beef", "steak", "pork", "salmon", "tuna","halibut","tilapia","chicken","venisen","lamb","duck","sausage","eel","shrimp","lobster","crab","chorizo","scallops","clams","hotdog","pepperoni","goat","liver","caviar","calamari","goose","quail","anchovies","mussels"]
    translated = []
    for x in range(len(ingredients)):
        y = ingredients[x].split(" ")
        for i in y:
            if(i in healthyReplacements.keys()):
                t = healthyReplacements.get(i)
                ingredients[x] = t
            if(i in meats):
                ingredients[x] = "tofu"
    return ingredients

def translateHealthy(ingredients):
    healthyReplacements = {"butter":"Coconut Oil", "honey":"Maple Syrup","eggs":"Bananas","milk":"Almond Milk","gelatin":"agar agar","rice":"quinoa", "oil":"Coconut Oil", "chips":"Popcorn", "croutons":"Almonds","flour":"Coconut Flower","sugar":"Stevia", "breadcrumbs":"Chia Seeds","iceberg":"Romaine Lettuce","ranch":"Olive Oil and Vinegar Mix","mayo":"Mustard","peanut":"Almond Butter","soda":"Tea","noodles":"Zoodles","pita":"Carrots"}
    for x in range(len(ingredients)):
        y = ingredients[x].split(" ")
        for i in y:
            if(i in healthyReplacements.keys()):
                t = healthyReplacements.get(i)
                ingredients[x] = t
            #if(i in unhealthy):
            #    ingredients[x] = "tofu"
    specificHealthyReplacements = {"sour cream":"Greek Yogurt","table salt":"Himalayan Salt","chocolate chips":"Cocoa Nibs","corn tortilla":"Flour Tortilla"}
    for x in range(len(ingredients)):
        if(x in specificHealthyReplacements.keys()):
            t = specificHealthyReplacements.get(x)
            ingredients[x] = t
    return ingredients

if __name__ == "__main__":
    main()
