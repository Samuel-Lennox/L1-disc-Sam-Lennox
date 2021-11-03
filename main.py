# random import for later use, kept up here for ease
import random
listoption = 0
# lists also kept up here for ease
food = ['pizza', 'chips', 'sandwich', 'salad', 'smoothie', 'meat', 'fruit', 'vegetables', 'popcorn', 'seafood', 'rice', 'tacos', 'toast', 'tofu', 'fish n chips', 'waffles/pancakes', 'sushi', 'wrap', 'lasagna', 'kebab', 'corn', 'hamburger', 'noodles', 'eggs']
candy = ['licorice', 'toffee', 'candyfloss', 'gummybears', 'chocolate', 'mints', 'gum', 'lollipop', 'hard boiled', 'candycorn', 'sour candy', 'candy canes', 'jawbreaker', 'marshmallow', 'sherbet', 'cookies', 'icecream']
activities = ['running', 'gaming', 'board game', 'card game', 'swimming', 'fitness', 'yoga', 'meditation', 'cooking', 'bike riding', 'music', 'reading', 'movie', 'shower/bath', 'clean the house/room', 'gardening', 'art', 'dance/drama', 'shopping', 'stargazing']
extremeactivities = ['skydiving', 'bungee', 'hang gliding', 'abseiling', 'canyoning', 'scuba diving', 'zipline', 'ice climbing']
crustaceans = ['barnacle', 'crab', 'crayfish' 'lobster', 'krill', 'hermit crab', 'prawn', 'Shrimp', 'woodlouse', 'yabby', 'mantis shrimp', 'scampi', 'rock lobster', 'rock lobster', 'slipper lobster', 'land crab', 'caridea', 'iraq lobster']
sandwich = ['lettuce', 'mayo', 'tomato sauce', 'mustard', 'cold meat', 'cheese', 'carrot', 'egg', 'tomato', 'avocado', 'spinach', 'onion', 'olives', 'cucumber', 'pickle', 'salt', 'honey', 'hot meat', 'sea meat', 'beans', 'beetroot', 'mushrooms', 'paprika', 'pineapple']
usercustom = []
# these values for while statement's, used for later variables
value = 0
value2 = 0
createvalue = 0
valuepremade = 0
variablename = ''
reroll = 0

# pre-made or create list, asks to determine which path the user goes down
while value != 1:
    listtype = input('Would you like to CREATE a custom list or use a PREMADE one instead?').lower()
    if listtype == 'create':
        print('create')  # confirms that user goes create path
        value = 1
    elif listtype == 'premade':
        print('premade')  # confirms that user goes premade lists path
        value = 1
    else:
        print("please enter 'CREATE' or 'PREMADE'")
# create section of code, takes in what user says and removes the last input of 'done'
if listtype == 'create':
    print("please enter something you'd like to add to your list and enter 'done' when you are done")
    while createvalue != 1:
        thing = input("enter thing and enter 'done' when complete:").lower()
        if thing == 'done':
            createvalue = 1
        usercustom.append(thing)
    usercustomsize = len(usercustom)
    last = list(range(1, usercustomsize))
    del last[-1]
    del usercustom[-1]
    print(usercustom)
# pre-made list options to choose which one theyd use
if listtype == 'premade':
    print('please enter one of the following words for the premade list options')
    while valuepremade == 0:
        if listoption != 'food' and listoption != 'candy' and listoption != 'activities' and listoption != 'extreme activities' and listoption != 'crustaceans' and listoption != 'sandwich':
            listoption = input('list options are:\n food \n candy \n activities \n extreme activities \n crustaceans \n sandwich').lower()
        elif listoption == 'food' or listoption or 'candy' or listoption == 'activities' or listoption == 'extreme activities' or listoption == 'crustaceans' or listoption == 'sandwich':
            valuepremade = 1
        elif listoption != 'food' and listoption != 'candy' and listoption != 'activities' and listoption != 'extreme activities' and listoption != 'crustaceans' and listoption != 'sandwich':
            listoption = input('list options are:\n food \n candy \n activities \n extreme activities \n crustaceans \n sandwich').lower()
# pulls, asks how many items the user would like to pull
pullamount = int(input('How many items would you like to pull from the list\nMust be in numerical form\nNo Decimals:'))
if listtype == 'premade':  #uses their selected list with the pull amount
    if listoption == 'food':
        variablename = len(food)
        for i in range(pullamount):
            f = random.randint(1, variablename)
            print(food[f])
        valuepremade = 0
    if listoption == 'candy':
        variablename = len(candy)
        for i in range(pullamount):
            f = random.randint(1, variablename)
            print(candy[f])
        valuepremade = 0
    elif listoption == 'activities':
        variablename = len(activities)
        for i in range(pullamount):
            f = random.randint(1, variablename)
            print(activities[f])
        valuepremade = 0
    elif listoption == 'extreme activities':
        variablename = len(extremeactivities)
        for i in range(pullamount):
            f = random.randint(1, variablename)
            print(extremeactivities[f])
        valuepremade = 0
    elif listoption == 'crustaceans':
        variablename = len(crustaceans)
        for i in range(pullamount):
            f = random.randint(1, variablename)
            print(crustaceans[f])
        valuepremade = 0
    elif listoption == 'sandwich':
        variablename = len(sandwich)
        for i in range(pullamount):
            f = random.randint(1, variablename)
            print(sandwich[f])
        valuepremade = 0
if listtype == 'create':
    variablename = len(usercustom)
    for i in range(pullamount):
        f = random.randint(1, variablename)
        print(usercustom[f])
