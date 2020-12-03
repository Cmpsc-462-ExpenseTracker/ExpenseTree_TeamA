class item:

    def __init__(self, name=None, cost=None, necessity=False):
        self.name = name
        self.necessity = necessity
        self.cost = cost

class monthly_expenses:

    def __init__(self, l):
        self.l = l
        self.parent = None
        self.right_child = None
        self.left_child = None
        self.balance_factor = 0
        self.height = 1

    def total_cost(self):
        total = 0
        for each_expense in self.l:
            total += each_expense.cost
        return total


class expense_tree:

    def __init__(self):
        self.root = None

    # function to add individual monthly expenses
    def add_monthly_expense(self, l):
        if not self.root:
            self.root = l
        else:
            self.__add_monthly_expense(self.root, l)

    # IGNORE
    # private function to recursively check for the new monthly expense node to be placed
    def __add_monthly_expense(self, current_node, l):

        if l.total_cost() < current_node.total_cost():
            if current_node.left_child == None:
                current_node.left_child = l
                current_node.left_child.parent = current_node
                self.update_balance(current_node)
                self.check_balance(current_node)
            else:
                self.__add_monthly_expense(current_node.left_child, l)
        elif l.total_cost() > current_node.total_cost():
            if current_node.right_child == None:
                current_node.right_child = l
                current_node.right_child.parent = current_node
                self.update_balance(current_node)
                self.check_balance(current_node)
            else:
                self.__add_monthly_expense(current_node.right_child, l)

    # function to check balance of the expense tree
    def check_balance(self, current_node):
        if current_node == None:
            return
        bF = current_node.balance_factor
        if abs(bF) > 1:
            self.rebalance(current_node)
            return
        self.check_balance(current_node.parent)

    # function to update the balance factor
    def update_balance(self, current_node):
        if current_node == None:
            return
        current_node.height = 1 + max(self.get_height(current_node.left_child), self.get_height(current_node.right_child))
        current_node.balance_factor = self.get_height(current_node.left_child) - self.get_height(current_node.right_child)
        self.update_balance(current_node.parent)

    # function to access the height of a node
    def get_height(self, node):
        if node == None:
            return 0
        return node.height

    # function to rebalance the expense tree
    def rebalance(self, current_node):
        if current_node.balance_factor < 0:
            if current_node.right_child.balance_factor > 0:
                self.right_rotation(current_node.right_child)
                self.left_rotation(current_node)
            else:
                self.left_rotation(current_node)
        elif current_node.balance_factor > 0:
            if current_node.left_child.balance_factor < 0:
                self.left_rotation(current_node.left_child)
                self.right_rotation(current_node)
            else:
                self.right_rotation(current_node)

    def right_rotation(self, node):

        A = node
        B = node.left_child
        BL = B.right_child
        C = B.left_child

        newParent = B
        A.left_child = BL

        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        else:
            if A.parent.left_child == A:
                A.parent.left_child = B
            else:
                A.parent.right_child = B

        B.right_child = A
        A.parent = B

        self.update_balance(B)
        self.update_balance(A)

    def left_rotation(self, node):

        A = node
        B = node.right_child
        BL = B.left_child
        C = B.right_child

        newParent = B
        A.right_child = BL

        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        else:
            if A.parent.left_child == A:
                A.parent.left_child = B
            else:
                A.parent.right_child = B

        B.left_child = A
        A.parent = B

        self.update_balance(B)
        self.update_balance(A)

# graphs necessity
def graph_necessity()


sample_list = monthly_expenses([item('toothpaste', 1.25, necessity=True),
                                item('keyboard', 60, necessity=False),
                                item('book', 15.24, necessity=True)
                                ])

sample_list1 = monthly_expenses([item('dijkstra algorithm', 100, necessity=True),
                                 item('random bullshit', 1000000, necessity=True),
                                 item('some more bullshit', 2.5, necessity=False)
                                 ])

test_tree = expense_tree()
test_tree.add_monthly_expense(sample_list)
test_tree.add_monthly_expense(sample_list1)

print(test_tree.root.total_cost())
print(test_tree.root.right_child.total_cost())
