def add_numbers(list):
    sum = 0
    for i in list:
        sum += i
    return sum

numlist = [1,2,3]
listsum = add_numbers(numlist)
print(listsum)