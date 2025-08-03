digit_map = {
    '2': "abc", '3': "def", '4': "ghi",
    '5': "jkl", '6': "mno", '7': "pqrs",
    '8': "tuv", '9': "wxyz"
}

def Letter_Combinations_of_a_Phone_Number(index:int, path:str):
    if index == len(path):
        return 
    
    results = list()
    current_digit = path[index]
    for char in list(digit_map[current_digit]):
        current_string = char 
        words = Letter_Combinations_of_a_Phone_Number(index+1, path)
        if words != None:
            for word in words:
                results.append(current_string + word)
        else:
            results.append(current_string)

    return results 


path = "23"
print("TEST 1:")
print(Letter_Combinations_of_a_Phone_Number(0, path))

path = "2"
print("TEST 2:")
print(Letter_Combinations_of_a_Phone_Number(0, path))

path = "256"
print("TEST 3:")
print(Letter_Combinations_of_a_Phone_Number(0, path))

path = "79"
print("TEST 4:")
print(Letter_Combinations_of_a_Phone_Number(0, path))