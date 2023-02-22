import time
import random


class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data

    def operation(self, cnode, rule):
        x = cnode.x
        y = cnode.y

        if rule == 1:

            if x < maxjug1:
                x = maxjug1

            else:
                return None

        elif rule == 2:

            if y < maxjug2:
                y = maxjug2

            else:
                return None
        elif rule == 3:

            if x > 0:
                x = 0
            else:
                return None
        elif rule == 4:
            if y > 0:
                y = 0
            else:
                return None
        elif rule == 5:
            if x + y >= maxjug1:
                y = y - (maxjug1 - x)
                x = maxjug1
            else:
                return None
        elif rule == 6:
            if x + y >= maxjug2:
                x = x - (maxjug2 - y)
                y = maxjug2
            else:
                return None
        elif rule == 7:
            if x + y < maxjug1:
                x = x + y
                y = 0
            else:
                return None
        elif rule == 8:
            if x + y < maxjug2:
                y = x + y
                x = 0
            else:
                return None
        if x == cnode.x and y == cnode.y:
            return None
        nextnode = node(cnode)
        nextnode.x = x
        nextnode.y = y
        nextnode.parent = cnode
        return nextnode


class searchBFS:
    def __init__(self, initialNode, goalNode):
        self.queue = []

    def printnode(self, i):
        print("(", i.x, ",", i.y, ")")

    def popnode(self):
        return self.queue.pop(0)

    def search(self):
        self.queue.append(initialNode)

        while len(self.queue) != 0:
            cnode = self.popnode()

            if cnode.x == goalNode.x and cnode.y == goalNode.y:
                return cnode
            l = self.generateAllSuccessors(cnode)
            self.queue.extend(l)
        return None

    def generateAllSuccessors(self, cnode):
        list1 = []
        for rule in range(1, 9):
            nextnode = cnode.operation(cnode, rule)
            if nextnode != None:
                list1.append(nextnode)

        return list1

    def printPath(self, cnode):
        temp = cnode
        list1 = []
        while temp != None:
            list1.append(temp)
            temp = temp.parent
            list1.reverse()
            for i in list1:
                self.printnode(i)
            print("Path cost:" + str(len(list1)))


class searchDFS:
    def __init__(self, initialNode, goalNode):
        self.dfsStack = []

    def generateRandomSuccessors(self, cnode, visitedNodes):
        l1 = []
        listRule = []
        while len(listRule) < 8:
            rule = random.randint(1, 8)
            if rule not in listRule:
                nextNode = cnode.operation(cnode, rule)
                listRule.append(rule)

                if nextNode != None and self.checkSameNodes(nextNode, visitedNodes):
                    l1.append(nextNode)
        return l1

    def checkSameNodes(self, nextNode, visitedNodes):

        for node in visitedNodes:
            if node.x == nextNode.x and node.y == nextNode.y:
                return False
        return True

    def search(self):
        self.dfsStack.append(initialNode)
        visitedNodes = []
        while len(self.dfsStack) != 0:
            cnode = self.dfsStack.pop()
            if cnode.x == goalNode.x and cnode.y == goalNode.y:
                return cnode
            visitedNodes.append(cnode)
            l = self.generateRandomSuccessors(cnode, visitedNodes)
            self.dfsStack.extend(l)

    def printnode(self, i):
        print("(", i.x, ",", i.y, ")")

    def printPath(self, cnode):
        temp = cnode
        list1 = []
        while temp != None:
            list1.append(temp)
            temp = temp.parent
        list1.reverse()
        for i in list1:
            self.printnode(i)
        print("Path cost:" + str(len(list1)))


maxjug1 = int(input("Enter value of maxjug1: "))
maxjug2 = int(input("Enter value of maxjug2: "))
initialNode = node(None)
initialNode.x = 0
initialNode.y = 0
initialNode.parent = None
goalNode = node(None)
goalNode.x = int(input("Enter value of goal in jug1: "))
goalNode.y = 0
goalNode.parent = None
print("Mihir Parmar - 20012021018")
print("\nBFS algorithm is running...")
start_time = time.time()
solution = searchBFS(initialNode, goalNode)
solutionNode = solution.search()
end_time = time.time()
if solutionNode != None:
    print("Solution can be found")
    solution.printPath(solutionNode)
else:
    print("Solution can't be found")
diff = end_time - start_time
print("Executed in time:", diff * 1000, "ns")
print("Mihir Parmar - 20012021018")
print("\n\nDFS algorithm is running...")
start_time1 = time.time()
solution1 = searchDFS(initialNode, goalNode)
solutionNode1 = solution1.search()
end_time1 = time.time()
if solutionNode1 != None:
    print("Solution can be found")
    solution1.printPath(solutionNode1)
else:
    print("Solution can't be found")
diff1 = end_time1 - start_time1
print("Executed in time:", diff1 * 1000, "ns")
print("Mihir Parmar - 20012021018")