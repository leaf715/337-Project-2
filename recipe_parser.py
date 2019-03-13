import urllib.request
from itertools import chain
# pip3 install BeautifulSoup4
from bs4 import BeautifulSoup
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
import json
import copy
cfg_file = open("cooking_info.config", "r")
cfg_lines = cfg_file.read()
cooking_dict = json.loads(cfg_lines)

def main():
    #Open URL
    with urllib.request.urlopen('https://www.allrecipes.com/recipe/173906/cajun-roasted-pork-loin/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=8722%20referringContentType%3Drecipe') as response:
        page = response.read()
    recipe = BeautifulSoup(page, 'html.parser')

    title, ingredients, steps = getItems(recipe)
    print(title+"\n")
    parsedIngreds = parseIngred(ingredients)
    parsedIngreds = parseIngred(ingredients)
    print("Ingredient List (Quantity, Measurement, Description, Ingredient, Preperation):")
    for i in range(len(parsedIngreds[0])):
        print("Q: " + parsedIngreds[0][i] +" M: " + parsedIngreds[1][i] +" D: " + parsedIngreds[2][i] +" I: " + parsedIngreds[3][i] +" P: " + parsedIngreds[4][i])
    print("\nSteps:")
    parsedSteps = parseSteps(steps)
<<<<<<< HEAD
    for i in range(len(parsedSteps)):
        print("{}. {}".format(i+1,parsedSteps[i]))
    primary, otherMethods, tools = parseMethodsandTools(title,parsedIngreds[4],parsedSteps)
    print("\nPrimary method: "+primary)
    print("Other methods: {}".format(otherMethods))
    print("Tools needed: {}\n".format(tools))

    transform(title, parsedIngreds, parsedSteps)

def transform(title, parsedIngreds, parsedSteps):
    while(True):
        try:
            choice = int(input('\nChoose a Transformation (1 = Vegetarian, 2 = Healthy, 3 = Prescatarian, anything else to quit): '))
        except:
            return
        transfromedIngreds = copy.deepcopy(parsedIngreds)
        transformedSteps = copy.deepcopy(parsedSteps)
        if choice == 1:
            print("\nVegetarian")
            changes,newIngreds = translateVegetarian(parsedIngreds[3])
        elif choice == 2:
            print("\nHealthy")
            changes,newIngreds = translateHealthy(parsedIngreds[3])
        elif choice == 3:
            print("\nPescatarian")
            changes,newIngreds = translatePescatarian(parsedIngreds[3])
        else:
            return
        print(changes)
        print(newIngreds)
        # use changes dict to change and print ingredients list and steps

def parseMethodsandTools(title,prep,steps):
    tools = set()
    otherMethods = set()
    MainMethods = cooking_dict["main-methods"]
    primary = ""
    action_tool_dict = cooking_dict["action-tools"]
    tool_to_pot_dict = cooking_dict["tools-to-pot"]
    allMethods = action_tool_dict.keys()
    allTools = cooking_dict["tools"]
    recipe_words = " ".join(steps) + " " + " ".join(prep)
    recipe_words = recipe_words.lower()
    for m in allMethods:
        if m in recipe_words:
            otherMethods.add(m)
            tools.add(action_tool_dict[m])
    for t in allTools:
        if t in recipe_words:
            tools.add(t)
    for m in otherMethods:
        if m in title:
            primary = m
            otherMethods.discard(m)
=======
    parsedTools = parseTools(title,parsedIngreds[4],parsedSteps)
    primary, otherMethods = parseMethods(title,parsedSteps,parsedIngreds[4])
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
    for i in possPrim:
        if i in title.lower():
            primary = i
            primaryFound = True
>>>>>>> f910773a891193f40134936b52e0c80408dc1b8e
            break
    helperTools = set()
    for t in tools:
        if t in tool_to_pot_dict:
            helperTools.add(tool_to_pot_dict[t])
    tools = tools.union(helperTools)
    if "skillet" in tools:
        tools.discard("pan")
    if primary == "":
        for m in otherMethods:
            if m in MainMethods:
                primary = m
                otherMethods.discard(m)
                break

    return primary, otherMethods, tools

<<<<<<< HEAD
# def parseMethods(title,steps,prep):
#     possPrim = ["roast","boil","broil","bake","stew","braise","toast","poach","sear","fry","sauté","fried","smoke","grill","steam"]
#     possSec = ["chop","grate","stir","shake","mince","crush","squeeze","dice","mix","sprinkle","melt","stuff","rub","whisk","pour","strain","roast","boil","broil","bake","stew","braise","toast","poach","sear","fry","stir-fry","simmer","sauté","fried","stir-fried","smoke","grill","steam","barbaque"]
#     #Get primary
#     primary = ""
#     primaryFound = False
#     titleWords = title.lower().split()
#     for i in titleWords:
#         if i in possPrim:
#             primary = i
#             primaryFound = True
#             break
#
#     if not primaryFound:
#         for x in steps:
#             if "oven" in x:
#                 primary = "bake"
#                 primaryFound = True
#
#     primaryDict = dict()
#     if not primaryFound:
#         for step in steps:
#             for possibility in possPrim:
#                 if possibility in step.lower():
#                     primaryDict[possibility] = primaryDict.get(possibility, 0) + 1
#         primaryFound = True
#         primary = get_max_in_dict(primaryDict)
#
#     #Get Others
#     othersDict = dict()
#     for step in steps:
#         for possibility in possSec:
#             if possibility in step.lower():
#                 print(step + " " + possibility)
#                 othersDict[possibility] = othersDict.get(possibility, 0) + 1
#
#     if(not primaryFound):
#         primary = get_max_in_dict(othersDict)
#         del othersDict[primary]
#
#     for p in prep:
#         if p != "no prep":
#
#
#     print(primary)
#     print(othersDict)
#     return primary, othersDict
=======
    if not primaryFound:
        for x in steps:
            if "oven" in x:
                if "bake" in steps:
                    primary = "bake"
                    primaryFound = True
                elif "roast" in steps:
                    primary = "roast"
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
                othersDict[possibility] = othersDict.get(possibility, 0) + 1

    if(not primaryFound):
        primary = get_max_in_dict(othersDict)
        del othersDict[primary]

    for p in prep:
        if p != "no prep":
            for possibility in possSec:
                if possibility in p.lower():
                    othersDict[possibility] = othersDict.get(possibility, 0) + 1

    return primary, othersDict
>>>>>>> f910773a891193f40134936b52e0c80408dc1b8e

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

def translateVegetarian(og_ingredients):
    ingredients = copy.deepcopy(og_ingredients)
    veg_Replacements = {"butter":"coconut butter", "honey":"maple syrup","eggs":"bananas","milk":"soy milk","gelatin":"agar agar"}
    # meats = ["beef", "steak", "pork", "salmon", "tuna","halibut","tilapia","chicken","venisen","lamb","duck","sausage","eel","shrimp","lobster","crab","chorizo","scallops","clams","hotdog","pepperoni","goat","liver","caviar","calamari","goose","quail","anchovies","mussels"]
    meats = cooking_dict["meats"] + cooking_dict["seafood"]
    translated = []
    veg_options = cooking_dict["vegetarian"]
    substitution_dict = {}
    meat_count = 0
    for x in range(len(ingredients)):
        if "broth" in ingredients[x] or "stock" in ingredients[x]:
            substitution_dict[ingredients[x]] = "vegetable broth"
            ingredients[x] = "vegetable broth"
            continue
        y = ingredients[x].split(" ")
        for i in y:
            if(i in veg_Replacements.keys()):
                t = veg_Replacements.get(i)
                substitution_dict[i] = t
                ingredients[x] = t
            elif(i in meats):
                substitution_dict[i] = veg_options[meat_count]
                ingredients[x] = veg_options[meat_count]
                meat_count = (meat_count+1)%len(veg_options)
    return substitution_dict, ingredients

def translatePescatarian(og_ingredients):
    ingredients = copy.deepcopy(og_ingredients)
    meats = cooking_dict["meats"]
    translated = []
    fish_options = cooking_dict["seafood"]
    substitution_dict = {}
    meat_count = 0
    for x in range(len(ingredients)):
        if "broth" in ingredients[x] or "stock" in ingredients[x]:
            substitution_dict[ingredients[x]] = "fish broth"
            ingredients[x] = "fish broth"
            continue
        y = ingredients[x].split(" ")
        for i in y:
            if(i in meats):
                substitution_dict[i] = fish_options[meat_count]
                ingredients[x] = fish_options[meat_count]
                meat_count = (meat_count+1)%len(fish_options)
    return substitution_dict, ingredients

def translateHealthy(og_ingredients):
    ingredients = copy.deepcopy(og_ingredients)
    healthyReplacements = cooking_dict["make-healthy"]
    substitution_dict = {}
    # healthyReplacements = {"butter":"Coconut Oil", "honey":"Maple Syrup","eggs":"Bananas","milk":"Almond Milk","gelatin":"agar agar","rice":"quinoa", "oil":"Coconut Oil", "chips":"Popcorn", "croutons":"Almonds","flour":"Coconut Flower","sugar":"Stevia", "breadcrumbs":"Chia Seeds","iceberg":"Romaine Lettuce","ranch":"Olive Oil and Vinegar Mix","mayo":"Mustard","peanut":"Almond Butter","soda":"Tea","noodles":"Zoodles","pita":"Carrots"}
    for x in range(len(ingredients)):
        item = ingredients[x]
        if(item in healthyReplacements.keys()):
            t = healthyReplacements.get(item)
            substitution_dict[item] = t
            ingredients[x] = t
        else:
            y = ingredients[x].split(" ")
            for i in y:
                if(i in healthyReplacements.keys()):
                    t = healthyReplacements.get(i)
                    substitution_dict[i] = t
                    ingredients[x] = t
            #if(i in unhealthy):
            #    ingredients[x] = "tofu"
    # specificHealthyReplacements = {"sour cream":"Greek Yogurt","table salt":"Himalayan Salt","chocolate chips":"Cocoa Nibs","corn tortilla":"Flour Tortilla"}
    # for x in range(len(ingredients)):
    #     if(x in specificHealthyReplacements.keys()):
    #         t = specificHealthyReplacements.get(x)
    #         ingredients[x] = t
    return substitution_dict, ingredients

if __name__ == "__main__":
    main()
