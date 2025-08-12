def Binary_Tree_Level_Order_Traversal(root:list):
    queue = list()
    current_level = 0
    queue_size = 0
    result = list()
    for node in root:
        queue.append(node)
        queue_size += 1
        if queue_size == 2 ** current_level:
            level = list()
            while queue_size > 0:
                n = queue.pop(0)
                level.append(n)
                queue_size -= 1

            result.append(level)            
            current_level += 1

    level = list()
    if queue_size > 0:
        while queue_size > 0:
            n = queue.pop(0)
            level.append(n)
            queue_size -= 1
                
        result.append(level) 
    return result


root = [3,9,20,15,7]
print("TEST 1:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")

root = [3,9,20,15,7,13,12,10,2]
print("TEST 2:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")

root = [3,9,20,5,8,15,7]
print("TEST 3:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")

root = [3,9,20,5]
print("TEST 4:")
print(Binary_Tree_Level_Order_Traversal(root), end="\n\n")
