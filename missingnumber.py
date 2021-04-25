
def missing_number_1(size_num, list_num):
    index = 1
    missing = None
    while( missing is None):
        if index in list_num:
            index += 1
        else:
            missing = index

    return missing

def missing_number_2(size_num, list_num):
    missing = None
    set_size = set(range(1, size_num+1))
    set_num = set(list_num)
    found = set_size ^ set_num
    missing = found.pop()

    return missing

#get number to get size
while(True):
    size_num = int(input())
    if (size_num > 1 and size_num <= (2*10**5)):
        break

#get list of numbers to search in and make list
entry = input().split(' ')
#covert to int with comprehesion
#list_num = [int(x) for x in list(entry)]
#convert to int with map
list_num = list(map(int, entry))
#list_num.sort()
#get missing number wuth method 1 - linear operation
#print(missing_number_1(size_num, list_num))
#get missing number with method 2 sets
print(missing_number_2(size_num, list_num))







