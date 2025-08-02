def islands_count(grid:list):
    count = 0
    visited = []
    for _ in range(len(grid)):
        x = []
        for _ in range(len(grid[0])):
            x.append(False)
        
        visited.append(x)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j] is False:
                if grid[i][j] == "1":
                    stack = [(i, j)]
                    visited[i][j] = True
                    while len(stack) > 0:
                        row, col = stack.pop()
                        if row + 1 < len(grid):
                            if visited[row + 1][col] is False and grid[row + 1][col] == "1":
                                visited[row + 1][col] = True
                                stack.append((row + 1, col))

                        if row - 1 >= 0:
                            if visited[row - 1][col] is False and grid[row - 1][col] == "1":
                                visited[row - 1][col] = True
                                stack.append((row - 1, col))

                        if col + 1 < len(grid[0]):
                            if visited[row][col + 1] is False and grid[row][col + 1] == "1":
                                visited[row][col + 1] = True
                                stack.append((row, col + 1))

                        if col - 1 >= 0:
                            if visited[row][col - 1] is False and grid[row][col - 1] == "1":
                                visited[row][col - 1] = True
                                stack.append((row, col - 1))
        
                    count += 1

    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print("TEST 1:")
print(islands_count(grid), end="\n\n")

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","1","0"],
  ["0","0","0","1","1"]
]
print("TEST 2:")
print(islands_count(grid), end="\n\n")

grid = [
  ["1","1","0","0","0"],
  ["1","1","1","0","0"],
  ["0","1","1","1","0"],
  ["0","0","0","1","1"]
]
print("TEST 3:")
print(islands_count(grid), end="\n\n")

grid = [
  ["1","1","0","0","1"],
  ["1","1","1","0","1"],
  ["0","1","0","1","0"],
  ["0","0","0","1","1"]
]
print("TEST 4:")
print(islands_count(grid), end="\n\n")

grid = [
  ["1","1","0","0","1"],
  ["1","0","1","0","1"],
  ["0","1","0","1","0"],
  ["0","0","0","0","1"]
]
print("TEST 5:")
print(islands_count(grid), end="\n\n")

grid = [
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"]
]
print("TEST 6:")
print(islands_count(grid), end="\n\n")