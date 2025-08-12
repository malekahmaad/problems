class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Binary_Tree_Level_Order_Traversal(root:TreeNode):
    queue = [root]
    result = list()
    while len(queue) > 0:
        level = list()
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)
        
        result.append(level)

    return result

right = TreeNode(20, TreeNode(15), TreeNode(17))
left = TreeNode(9)
root =  TreeNode(3, left, right)
print("TEST 1:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")

right = TreeNode(20, TreeNode(15), TreeNode(17))
left = TreeNode(9, TreeNode(19), TreeNode(12))
root =  TreeNode(3, left, right)
print("TEST 2:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")

right = TreeNode(20, TreeNode(15, TreeNode(5)), TreeNode(17))
left = TreeNode(9, TreeNode(19, TreeNode(7)), TreeNode(12))
root =  TreeNode(3, left, right)
print("TEST 3:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")

right = TreeNode(20, TreeNode(15))
left = TreeNode(9)
root =  TreeNode(3, left, right)
print("TEST 4:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")
