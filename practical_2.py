
class Node:
    def __init__(self, parent=None, value="", child_list=[], lvl=0):
        self.parent = parent
        self.value = value
        self.child_list = child_list
        self.level = lvl

    def add_child_node(self, child):
        self.child_list.append(child)

    def __repr__(self):
        indent = "\t" * self.level
        strChild = ""
        for child in self.child_list:
            strChild += child.__repr__()
        return f"{indent}-> {self.value}\n{strChild}"



class Tree:
    def __init__(self, rootnode):
        self.root = rootnode

    def insert_node(self, nodevalue, parentnode, lvl):
        temp_node = Node(parentnode, nodevalue, [], lvl)
        parentnode.add_child_node(temp_node)
        return temp_node

    def __repr__(self):
        return str(self.root)


# driver code

child0 = Node(parent=None, value="Electronics", child_list=[], lvl=0)
tree1 = Tree(child0)
child1 = tree1.insert_node("Freeze", tree1.root, 1)
child2 = tree1.insert_node("Mobile", tree1.root, 1)
child3 = tree1.insert_node("Smart Tv", tree1.root, 1)

child4 = tree1.insert_node("Godrez freeze", child1, 2)
child5 = tree1.insert_node("LG Freeze", child1, 2)
child6 = tree1.insert_node("Samsung freeze", child1, 2)

child7 = tree1.insert_node("Oppo Mobile", child2, 2)
child8 = tree1.insert_node("Samsung Mobile", child2, 2)
child9 = tree1.insert_node("Redmi Mobile", child2, 2)
child10 = tree1.insert_node("Realme Mobile", child2, 2)

child11 = tree1.insert_node("Lg smart tv", child3, 2)
child12 = tree1.insert_node("Samsung smart tv", child3, 2)
child13 = tree1.insert_node("Panasonic smart tv", child3, 2)
child14 = tree1.insert_node("Realme smart tv", child3, 2)
child15 = tree1.insert_node("Redmi smart tv", child3, 2)

child16 = tree1.insert_node("40 inch LG Smart TV", child11, 3)
child17 = tree1.insert_node("50 inch LG Smart TV", child11, 3)
print(tree1)


def bfs(searchString, rootNode):
    node = []
    f = 0

    node.append(rootNode)
    while node:
        tempNode = node.pop(0)
        if tempNode.value == searchString:
            f = 1
            return tempNode
        else:
            node.extend(tempNode.child_list)

    if f == 0:
        return None


def drawPath(solNode):
    list1 = []
    tempNode = solNode
    while (tempNode != None):
        list1.append(tempNode.value)
        tempNode = tempNode.parent
        if (tempNode == None):
            break

    list1.reverse()
    print("Path:")
    print(*list1, sep="->")
    print("Path Cost=" + str(len(list1) - 1))


searchSTR = input("\nSearch String : ")
breathF = bfs(searchSTR, tree1.root)
if breathF is None:
    print("Sorry!! We can't find the entered string")
else:
    res = drawPath(breathF)