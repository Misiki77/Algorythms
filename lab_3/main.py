class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):

    def find_left_leaf_sums(node, is_left_child):
        if node is None:
            return 0

        if node.left is None and node.right is None and is_left_child:
            return node.value

        left_sum = find_left_leaf_sums(node.left, True)
        right_sum = find_left_leaf_sums(node.right, False)

        return left_sum + right_sum

    return find_left_leaf_sums(root, False)


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

sum_of_left_leaves = branchSums(root)
print(sum_of_left_leaves)