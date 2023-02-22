import time


class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.data = data


def operation(cnode, rule):
    x = cnode.x
    y = cnode.y
    if rule == 1:
        if x < max_jug1:
            x = max_jug1
    elif rule == 2:
        if y < max_jug2:
            y = max_jug2
    elif rule == 3:
        if x > 0:
            x = 0
    elif rule == 4:
        if y > 0:
            y = 0
    elif rule == 5:
        if x + y >= max_jug1:
            y = y - (max_jug1 - x)
            x = max_jug1
    elif rule == 6:
        if x + y >= max_jug2:
            x = x - (max_jug2 - y)
            y = max_jug2
    elif rule == 7:
        if x + y <= max_jug1:
            x = x + y
            y = 0
    elif rule == 8:
        if x + y <= max_jug2:
            x = 0
            y = x + y

    temp_node = node(cnode, x, y)
    return temp_node


def DFS(maxJugCap1, maxJugCap2, target1, target2):
    stack = []
    root = node(0, 0, 0, None)
    stack.append(root)
    visited = set()
    visited.add((0,0))
    max_stack_length = 0
    start_time = time.time()

    while stack:
        currNode = stack.pop()
        if currNode.m == target1 and currNode.n == target2:
            print("Path: ")
            printPath(currNode)
            print(f"Path cost: {currNode.cost}")
            print("Time complexity: ", (time.time() - start_time) * 1000, "milliseconds")
            print("Space complexity: ", max_stack_length)
            return currNode

        for rule in range(1, 9):
            child = waterJugOperation(currNode, rule, maxJugCap1, maxJugCap2)
            if child is not None and (child.m, child.n) not in visited:
                stack.append(child)
                visited.add((child.m, child.n))
                child.cost = currNode.cost + 1
                max_stack_length = max(max_stack_length, len(stack))

    return None


class bFsAlgo:
    def __int__(self):
        self.queue_bfs = []
        self.temp = 123

    def is_empty(self):
        return len(self.queue_bfs) == 0

    def generateAllNode(self, cnode):
        list = []
        for rule in range(0, 9):
            temp_node = operation(cnode, rule)
            list.append(temp_node)
        return list

    def bfsmain(self, i, g):
        print(self.temp)
        self.queue_bfs.append(i)

        while not self.is_empty():
            visitedNode = self.queue_bfs.pop(0)
            if visitedNode.x == goalNode.x and visitedNode.y == goalNode.y:
                return visitedNode
            else:
                successor_node = self.generateAllNode(visitedNode)
            self.queue_bfs.extend(successor_node)
            # print(g)
        return None


max_jug1 = int(input("Enter max jug1 value: "))
max_jug2 = int(input("Enter max jug2 value: "))

initialNode = node(None)

goalNode = node(None)
goalNode.x = int(input("Enter GoalX value: "))

print("BFS starts!")
start_time = time.time()
p = bFsAlgo()
p.bfsmain(initialNode, goalNode)
end_time = time.time()
diff = end_time - start_time
print(f"algo took: {diff} ms")

maxJugCap1 = int(input("Enter the capacity of jug 1: "))
maxJugCap2 = int(input("Enter the capacity of jug 2: "))
target1 = int(input("Enter the target value for jug 1: "))
target2 = int(input("Enter the target value for jug 2: "))


print("\nDFS traversal: ")
dfsResultNode = DFS(maxJugCap1, maxJugCap2, target1, target2)
print("DFS is complete in finding the solution if it exists.")
print("DFS, on the other hand, is not an optimal algorithm because it does not necessarily find the solution with the minimum number of steps.")
if dfsResultNode is None:
  print("Node not found in DFS")


'''
create the queue
import queue
q1 = queue
init parent=none, x=, y=
print node method which prints the nodes
generate the successor of each state
create operation method where you have to define the rules 
create pushList method (list)
create popNode() - gettheNode() , setTheNode()
create isgoalNode() method
create method bfs (initialNode, goalNode)

'''
