
def missing_number_1(size_num, list_num):
    index = 1
    missing = None
    while( missing is None):
        if index in list_num:
            index += 1
        else:
            missing = index

    return missing

#get number to get size
while(True):
    size_num = int(input())
    if (size_num > 1):
        break



#get list of numbers to search in and make list
entry = input().split(' ')
list_num = [int(x) for x in list(entry)]
list_num.sort()
#get missing number
print(missing_number_1(size_num, list_num))







