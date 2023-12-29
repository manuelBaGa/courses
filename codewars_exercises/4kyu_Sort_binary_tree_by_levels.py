'''
INSTRUCTIONS
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]

TEST EXAMPLES:
test.assert_equals(tree_by_levels(None), [])
test.assert_equals(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])
'''
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node != None:
        pre_sorted_tree = [node]
        for element in pre_sorted_tree:
            if type(element).__name__ == 'Node':
                pre_sorted_tree.append(element.value)
                if element.left != None:
                    pre_sorted_tree.append(element.left)
                if element.right != None:
                    pre_sorted_tree.append(element.right)
        sorted_tree = [object for object in pre_sorted_tree if type(object).__name__ == 'int']

    else:
        return []

    print(sorted_tree)

node=Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)

test_node=Node(R=2,L=Node(4,5,3),n=1)
test_node1=Node(2,3,1)
tree_by_levels(node)