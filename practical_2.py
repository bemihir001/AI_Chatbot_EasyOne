class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return self.data


class Tree:
    def __init__(self, root=None): 
        self.root = root

    def __repr__(self):
        return self.root.__repr__() if self.root else None

    def add_node(self, data, parent_data):
        parent_node = self._find_node(parent_data, self.root)
        if parent_node:
            parent_node.add_child(Node(data))
        else:
            print(f"Parent node with data {parent_data} not found.")

    def _find_node(self, data, node):
        if node.data == data:
            return node

        for child in node.children:
            child_node = self._find_node(data, child)
            if child_node:
                return child_node
        return None


tree = Tree("Root")
tree.add_node("Child 1", "Root")
tree.add_node("Child 2", "Root")
tree.add_node("Grandchild", "Child 1")
print(tree)
