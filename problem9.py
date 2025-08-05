def Daily_Temperatures(temperatures:list):
    stack = [0]
    results = [0 for _ in range(len(temperatures))]
    for i in range(1, len(temperatures)):
        while len(stack) != 0:
            temp = stack.pop()
            if temperatures[temp] < temperatures[i]:
                results[temp] = i - temp
            else:
                stack.append(temp)
                break

        stack.append(i)

    return results

temperatures = [73,74,75,71,69,72,76,73]
print("TEST 1:")
print(Daily_Temperatures(temperatures), end="\n\n")

temperatures = [81,73,72,71]
print("TEST 2:")
print(Daily_Temperatures(temperatures), end="\n\n")

temperatures = [73,74,75,76,77,78,79,79]
print("TEST 3:")
print(Daily_Temperatures(temperatures), end="\n\n")

temperatures = [73,72,71,70,77]
print("TEST 4:")
print(Daily_Temperatures(temperatures), end="\n\n")

temperatures = [73,73,73,73,73,83,83,83,83,93]
print("TEST 5:")
print(Daily_Temperatures(temperatures), end="\n\n")