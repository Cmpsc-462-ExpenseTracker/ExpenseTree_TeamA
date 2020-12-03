# class to create individual item nodes
class itemNode:

    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost
        self.category = None  # level of need
        #self.node = {self.name, self.cost, self.category}

# mutator methods

    def setCost(self, c):
        self.cost = c

    def setCategory(self, cat):
        self.category = cat

    def setName(self, name):
        self.name = name

# accessor methods used to access different parts of the item:
    def getCost(self):
       return self.cost

    def getCategory(self):
        return self.category

    def getName(self):
        return self.name
'''
monthlyExpenses - this contains list of all listNodes
this gets passed to the expense tree
'''

# contains the total expenses of a single month
class monthlyExpenses:

    # initialize
    def __init__(self):

        self.l = []  # list of items held in a NODE (itemNode) |
        self.right = None
        self.left = None
        self.parent = None

    # checks if the node is the leaf node
    def is_leaf_node(self):
        return (self.right == None) and (self.left == None)

    # checks if the node has both nodes
    def has_both_nodes(self):
        return (self.right != None) and (self.left != None)

    # check if the node has right node
    def has_right_node(self):
        return (self.right != None)

    # check if the node has left node
    def has_left_node(self):
        return (self.left != None)

    # function to append listNode
    def append(self, itemNode):
        self.l.append(itemNode)

    # function to get the total cost of the list
    def getTotal(self, total=0):
        for each in self.l:
            total += each.cost
        return total

    # function to acquire a specific item from the list: input by name
    def getItem(self, name):
        for item in self.l:
            if name == item.name:
                return item



'''
expense Tree sorts out the elements within the list
 left = cheap
  right = expensive
  BST oriented
'''


class expenseTree:

    # initializes the tree
    def __init__(self, listNode):
        self.root = monthlyExpenses

    # insert function to insert the data according to its amount
    def addNode(self, monthlyExpenses, currNode):
        # if the data inserted is less than cur value it'll
        # go into the left node
        if monthlyExpenses.getTotal() < self.root.getTotal(): #compares the new expense tree with old expense tree
            if self.root.left == None:                         #if left of old expense tree is none
                self.root.left = monthlyExpenses #then the left of old is added to monthly expenses
                monthlyExpenses.parent = self.root
            else:
                self.addNode(self, monthlyExpenses, currNode.left)

        # if the data is greater than the root the value gets added to the right side
        #
        #   if self.root.right:
        #         self.right.addNode(self.data)
        # else:
        #     self.right = self.addNode(self.data)

    # this will first visit left node
    # then the root node and finally
    # the right node and display them in
    # specific order

        #Matt: This will traverse through the expense Tree in order.
    def inOrderTrav(self):
        elements = []
        parent = monthlyExpenses.self.parent
        left = monthlyExpenses.self.left
        right= monthlyExpenses.self.right
        if parent:          #visit root node first
            elements += parent
        if left:            #visit the left node
            elements+= left
        if right:           #visit the right node
            elements += right
        return elements #return the list of elements inOrder

       #Matt, this inserts a node into the expense tree
    def insert(self, val):
        if monthlyExpenses.self.root == None:
            self.root = self(val)
        else:
            self.__insert(val, self.root)


# Function to get the max cost of the tree
    def getMaxCost(self, max=0):
# Current is set to the root of the tree
            current = itemNode.getName(self)
# If there aren't any nodes in the tree return None
            if current is None:
                return None
# If the current is greater than the max set that value to the max
            if current > max:
                max = current
            return max

        # this find the minimum cost node
        #Matt: this is the minimum cost finder.
    def getMinCost(self, minimum=0):
# current is self.root node
        monthlyExpenses.current = self
        if self is None:
            return None
        if monthlyExpenses.current < monthlyExpenses.self.root and monthlyExpenses.current < monthlyExpenses.self.right: #checking the root/right node
            if monthlyExpenses.current < monthlyExpenses.self.left: #then we check the left node
                minimum = monthlyExpenses.current
        return minimum

    # insert func to insert the data according to it's amount

    # rebalances the entire tree
    def rebalance(self, currNode):
        if currNode.balanceFactor < 0:
            if currNode.rightChild.balanceFactor > 0:
                self.rightRotation(currNode.rightChild)
                self.leftRotation(currNode)
            else:
                self.leftRotation(currNode)
        elif currNode.balanceFactor > 0:
            if currNode.leftChild.balanceFactor < 0:
                self.leftRotation(currNode.leftChild)
                self.rightRotation(currNode)
            else:
                self.rightRotation(currNode)
        else:
            return "Error"

    # function to perform right rotation
    def rightRotation(self, node):

        A = node
        B = node.leftChild
        BL = B.rightChild
        C = B.leftChild

        newParent = B
        A.leftChild = BL

        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        else:
            if A.parent.leftChild == A:
                A.parent.leftChild = B
            else:
                A.parent.rightChild = B

        B.rightChild = A
        A.parent = B

        self.updateBalanceFactor(B)
        self.updateBalanceFactor(A)

    # function to perform left rotation
    def leftRotation(self, node):

        A = node
        B = node.rightChild
        BL = B.leftChild
        C = B.rightChild

        newParent = B
        A.rightChild = BL

        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        else:
            if A.parent.leftChild == A:
                A.parent.leftChild = B
            else:
                A.parent.rightChild = B

        B.leftChild = A
        A.parent = B

        self.updateBalanceFactor(B)
        self.updateBalanceFactor(A)

    # function to update the balance factor
    def updateBalanceFactor(self, currNode):

        if currNode == None:
            return
        currNode.height = 1 + max(self.getHeight(currNode.leftChild), self.getHeight(currNode.rightChild))
        currNode.balanceFactor = self.getHeight(currNode.leftChild) - self.getHeight(currNode.rightChild)
        self.updateBalanceFactor(currNode.parent)

    # function to check balance factor of each node in the tree
    def checkForBalanace(self, currNode):
        if currNode == None:
            return
        bF = currNode.balanceFactor
        if abs(bF) > 1:
            self.rebalance(currNode)
            return
        self.checkForBalanace(currNode.parent)

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


'''item = itemNode("movie", 20)
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
item3.toString()'''
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

