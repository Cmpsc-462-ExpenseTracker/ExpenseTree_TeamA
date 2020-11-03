# Team A: Kavan Adeshara, Dillon Hector, Matthew Coutts, Himani Vommi
# Team B: ZeZheng, Mis Champa

# class node

'''
#Item Node
# lets get started
#this holds our item here
'''


class itemNode:

    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost
        self.category = "" #general category
        self.levelOfNeed = ""# level of need
        self.description = "none" #additional note or description of item (for example, under name "professional wear",
                              # allow a note for "new suit"

    # mutator methods
    def setCost(self, c):
        self.cost = c

    def setCategory(self, cat):
        self.category = cat

    def setLevelOfNeed(self, lon):
        self.levelOfNeed = lon

    def setName(self, n):
        self.name = n

    def setDescription(self, note):
        self.description = note

    # accessor methods:
    def getCost(self):
        return self.cost

    def getCategory(self):
        return self.category

    def getName(self):
        return self.name

    def getLevelOfNeed(self):
        return self.levelOfNeed

    def getDescription(self):
        return self.description

    def toString(self):
        print("name: " + self.name)
        print("cost: " + str(self.cost))
        print("category: " + self.category)
        print("level of need: " + self.levelOfNeed)
        print("description: " + self.description)
        print("\n")

'''
ListNode - this contains list of all listNodes
this gets passed to the expense tree

'''
def classifier(item):  # Himani: commenting outline
    # store off cost and name from item for classification use
    cost = item.cost
    name = item.name
    category = "" #type of category
    levelOfNeed = "necessity" #necessity (default) or luxury

    # create a list of keywords for each type of personal expense:
    #perhaps the GUI can have the user select one of these words when entering their expense
    housing = ["housing", "mortgage", "rent", "property tax", "repairs", "housing fees"]
    transportation = ["transportation", "car mortgage", "bus", "train", "gas", "tires", "repairs", "parking fees", "maintenance",
                      "warranty", "uber", "taxi"]
    food = ["food", "groceries", "restaurants", "pet food", "snacks"]
    utilities = ["utilities","electricity", "water", "garbage", "sewage", "heating", "cooling", "AC", "mobile network", "internet",
                 "cable", "laundry"]
    clothing = ["clothing","professional attire", "formal wear", "casual wear", "shoes", "accessories"]
    healthcare = ["healthcare", "medicine","primary care", "dental care", "specialty care", "urgent care", "medication", "medical devices",
                  "support", "nursing"]
    insurance = ["insurance","health insurance", "homeowner's insurance", "car insurance", "life insurance", "disability insurance"]
    householdItems = ["household items", "toiletries", "laundry detergent", "dishwasher detergent", "cleaning supplies", "tools"]
    personal = ["personal", "memberships", "haircut", "salon", "cosmetics", "babysitter", "birthday", "anniversary", "holiday",
                "wedding"]
    loans = ["personal loan", "student loan", "credit card"]
    education = ["education","textbooks", "student fees", "lab fees", "school supplies", "clubs", "conferences"]
    savings = ["savings", "emergency", "long-term savings"]
    entertainment = ["entertainment", "games", "movie", "concerts", "party", "vacations", "alcohol", "subscription", "sport",
                    "social events"]

#check if the item name fits in one of these categories
    if (name in housing):
        category = "housing"
    elif(name in transportation):
        category = "transportation"
    elif(name in food):
        category = "food"
    elif(name in utilities):
        category = "utilities"
    elif(name in clothing):
        category = "clothing"
    elif(name in healthcare):
        category = "healthcare"
    elif(name in insurance):
        category = "insurance"
    elif(name in householdItems):
        category = "household items"
    elif(name in personal):
        category = personal
    elif(name in loans):
        category = "loans"
    elif(name in education):
        category = "education"
    elif(name in savings):
        category = "savings"
    elif(name in entertainment):
        category = "entertainment"
    else:
        category = "miscellaneous" #if category isn't identified

#luxury if personal, entertainment (may need adjusting - perhaps add functions to tweak definition of "luxury" for each user using input)
    if (category == "personal" or category == "entertainment"):
        levelOfNeed = "luxury"

#returns an array of the category and sub category:
    return [category, levelOfNeed]


item = itemNode("movie", 20)
categoryList = classifier(item)
item.setCategory(categoryList[0])
item.setLevelOfNeed(categoryList[1])
item.toString()

item2 = itemNode("water", 70)
categoryList = classifier(item2)
item2.setCategory(categoryList[0])
item2.setLevelOfNeed(categoryList[1])
item2.toString()

item3 = itemNode("professional attire", 100)
categoryList = classifier(item3)
item3.setCategory(categoryList[0])
item3.setLevelOfNeed(categoryList[1])
item3.setDescription("new suit for interview")
item3.toString()
'''
**SAMPLE CLASSIFIER RUN: ***

name: movie
cost: 20
category: entertainment
level of need: luxury
description: none


name: water
cost: 70
category: utilities
level of need: necessity
description: none


name: professional attire
cost: 100
category: clothing
level of need: necessity
description: new suit for interview
'''

