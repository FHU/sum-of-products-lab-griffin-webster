#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks

import operator 

def sum_of_products(list1, list2):
    result = list(map(operator.mul, list1, list2))
    return sum(result)

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    int1 = int(input("Give a list of numbers:"))
    int2 = int(input("Give a second list of numbers (the same length as the first):"))
    str1 = str(int1)
    str2 = str(int2)
    if len(str1) < len(str2) or len(str1) > len(str2):
        print("Error")
    else:
        pass
    list1 = list(map(int, str(int1)) )
    list2 = list(map(int, str(int2)) )
    sum_of_products(list1, list2)

print(sum_of_products(list1, list2))