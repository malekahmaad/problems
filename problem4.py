def min_coins(coins:list, amount:int):
    amounts_table = [float('inf') for _ in range(amount+1)]
    amounts_table[0] = 0
    for i in range(len(amounts_table)):
        for coin in coins:
            if i - coin >= 0:
                if amounts_table[i - coin] + 1 < amounts_table[i]:
                    amounts_table[i] = amounts_table[i - coin] + 1

    if amounts_table[-1] == float('inf'):
        return -1
    
    return amounts_table[-1]


coins = [1, 2, 5] 
amount = 12
print("TEST 1")
print(min_coins(coins, amount), end="\n\n")

coins = [3, 5] 
amount = 4
print("TEST 2")
print(min_coins(coins, amount), end="\n\n")

coins = [1, 2, 5] 
amount = 18
print("TEST 3")
print(min_coins(coins, amount), end="\n\n")

coins = [1, 2, 4] 
amount = 5
print("TEST 4")
print(min_coins(coins, amount), end="\n\n")

coins = [2] 
amount = 1
print("TEST 5")
print(min_coins(coins, amount), end="\n\n")