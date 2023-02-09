import dataclasses
from typing import Optional, Any

"""
# Test task (kth biggest)

Container that supports two operations:

1. Get Kth biggest value from container;
2. Push new value to container.

Example: for a container with numbers 10, 2, 5, 0 the 1st biggest will be 10 and the 3rd biggest will be 2.
"""

@dataclasses.dataclass
class Node:
    left: Any = None
    right: Any = None
    value: Any = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value: Any):
        if self.root is None:
            self.root = Node(left=None, right=None, value=value)
            return True
        root = self.root
        while True:
            if root.value > value:
                if root.left is None:
                    root.left = Node(left=None, right=None, value=value)
                    break
                root = root.left
            elif root.value < value:
                if root.right is None:
                    root.right = Node(left=None, right=None, value=value)
                    break
                root = root.right
            else:
                return False

        return True

    def in_order(self):
        def traverse(root: Node):
            if root is None:
                return
            traverse(root.right)
            print(root.value)
            traverse(root.left)
        traverse(self.root)


    def get_max(self, k):
        if k < 0:
            return
        @dataclasses.dataclass
        class State:
            k: int = 0

        def traverse(root: Node, state: State):
            if root is None:
                return None
            v = traverse(root.right, state)
            if v is not None:
                return v

            if state.k == 0:
                return root.value
            state.k -= 1

            v = traverse(root.left, state)
            if v is not None:
                return v


        return traverse(self.root, State(k=k))

values = [10, 5, 7, 3, 2, 11, 18]
tree = Tree()
for v in values:
    assert(tree.add(v))

tree.in_order()

assert tree.get_max(2) == 10
assert tree.get_max(-1) is None
assert tree.get_max(0) == 18
assert tree.get_max(6) == 2
