from itertools import product
def Bridge_Repair(file) -> list:
    file = open(file, "r")
    print("\rWorking...", end="")
    found_array = []

    counter = 0
    for line in file:
        found = False
        counter += 1

        operators = ['*', '+']
        
        #usable STRING numerical test values
        test_values = line[line.index(":")+2:].split()
        all_operands = list(product(operators, repeat= (len(test_values) - 1)))
        total = line[:line.index(":")]
        #usable STRING total values (checker)
        for b in range(len(all_operands)):
            equation = ''
            index = 0
            for x in test_values:
                equation += x
                if (((index+1) < (len(test_values)))):
                    equation += all_operands[b][index]
                index += 1
            if (eval(equation) == int(total)):
                found = True
                break
        if(found):
            found_array.append(counter)
    file.close()
    print("\r", end="")
    return found_array

# Below is displayed example usage
# print(Bridge_Repair("example.txt"))