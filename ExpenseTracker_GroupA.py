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
        self.category = None  # level of need
        #self.node = {self.name, self.cost, self.category}

#mutator methods

    def setCost(self, c):
        self.cost = c


    def setCategory(self, cat):
        self.category = cat

    def setName(self, name):
        self.name = name

#accessor methods:
    def getCost(self):
       return self.cost

    def getCategory(self):
        return self.category

    def getName(self):
        return self.name
'''
ListNode - this contains list of all listNodes
this gets passed to the expense tree

'''


class listNode: #contains the total expenses of a single month

    # initialize
    def __init__(self):

        self.l = []  # list of items held in a NODE (itemNode) | f(g(x))
        self.right = None
        self.left = None
        self.parent = None

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
        self.root = listNode

    # insert func to insert the data according to it's amount
    def addNode(self, newListNode):

        # if the data inserted is less than cur value itll
        # go into the left node
        if newListNode.getTotal() < self.root.getTotal():
            if self.data:
                self.left.addNode(self.data)
            else:
                self.left = self.addNode(self.data)


        # if the data is greater than the value
        # of the current node then it goes right
        else:
            if self.right:
                self.right.addNode(self.data)
            else:
                self.right = self.addNode(self.data)

    # this will first visit left node
    # then the root node and finally
    # the right node and display them in
    # specific order

        #Matt: This will traverse through the expense Tree in order.
    def inOrderTrav(self):
        elements = []
        if self.left:  ###left
            elements += self.left.inOrderTrav()  # left
        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTrav()
        return elements

        #Matt, this inserts a node into the expense tree
    def insert(self, val):
        if self.root == None:
            self.root = self(val)
        else:
            self.__insert(val, self.root)

    # need to adjust the insert function to fit in with the expense tree
    def __insert(self, val, currNode):
        if val < currNode.val:
            if currNode.leftChild == None:
                currNode.leftChild = Node(val, parent=currNode)
                self.updateBalanceFactor(currNode)
                self.checkForBalanace(currNode)
            else:
                self.__insert(val, currNode.leftChild)
        elif val > currNode.val:
            if currNode.rightChild == None:
                currNode.rightChild = Node(val, parent=currNode)
                self.updateBalanceFactor(currNode)
                self.checkForBalanace(currNode)
            else:
                self.__insert(val, currNode.rightChild)
        else:
            return "value already exist"

    # getItem from itemNode
    # parameters: name of the item
    #def getItem(self, name):
        #for each in self: #fix this
            #if name == item.name:
             #   return item
        # need a function to search for a specific item in the list node
        # need a helper function to traverse all the list nodes

    #  Matt: this obtains the max cost within the expense
    #        tree.
    def getMaxCost(self, max=0):
            current = listNode.getItem(self)
            if current is None:
                return None
            if current > max:
                max = current
            return max

        # this find the minimum cost node
        #Matt: this is the minimum cost finder.
    def getMinCost(self, minimum=0):
        current = self # current is self.root node
        if self is None:
            return None
        if current < self.root and current < self.right: #checking the root/right node
            if current < self.left: #then we check the left node
                minimum = current
        return minimum
    # insert func to insert the data according to it's amount



'''
class Classifier: #TODO Himani: commenting outline
    def __init__(self,listnode)
        self.neccesity
        self.luxury

    # luxury
    #
    pass'''



#TODO Matt: add code to test itemNode and listNode

 #This creates a node to hold our list of items
list1 = list()
test = itemNode(list1) #storing a list in itemNode
test.setName("Rice") #name of product
test.setCost(24) #price of produt
test.setCategory("Food") #category of product

listTest = listNode() #assigning listTest to listNode()
listTest.append(test) #this adds test.ItemNode object to the listTest.listNode object
listTest.getItem("Rice") # do we need to add a print function for clarity in getItem?
print(listTest.getTotal()) # prints total cost in text itemNode

expenseTest = expenseTree(listTest) #in order to initialize the tree we needed a listNode input.
                                    #instead lets remove that and put a addListNode function for clarity
 # we need a build tree function here
# expenseTest.buildTree(listNode)

expenseTest.getMaxCost(itemNode.getName()) # i was stuck here, think we need to go over it on Tuesday


#extra
sampleList = listNode()
sampleList.append(3)

print(sampleList.getTotal)
