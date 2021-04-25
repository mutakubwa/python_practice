

def get_subarray_sum_1(s_array): #O(n**2)
    '''
    Return max subarray and max subarray sum
    '''

    #initialise variables
    max_sum = 0
    max_sub_array = []
    #get all items in array and go through them
    for item in range(len(s_array)):
        #get all possible sub arrays while maintaining their max sum and max subarray
        #for  every tiem go to items after it and record max sum and max sub array if greater than current max sum 
        index1 = item
        index2 = item
        while index2 < len(s_array):
            index2 += 1
            if ( sum(s_array[index1:index2+1]) > (max_sum) ):
                max_sum =  sum(s_array[index1:index2+1])
                max_sub_array = s_array[index1:index2+1]


    return (max_sub_array,max_sum)

def get_subarray_sum_2(s_array): #O(n**2)
    '''
    Return max subarray and max subarray sum
    '''

    #initialise variables
    max_sum = 0
    max_sub_array = []
    #get all items in array and go through them
    for item in range(len(s_array)):
        #get all possible sub arrays while maintaining their max sum and max subarray
        #for  every tiem go to items after it and record max sum and max sub array if greater than current max sum 
        if item == 0:
            continue
        if( sum( s_array[:item+1] ) > max_sum):
            max_sum = sum( s_array[:item+1] )
            max_sub_array = s_array[:item+1]

    return (max_sub_array,max_sum)

#get subarray
s_array = [2, 4, -3, 5, -9 ,6, 2, 1 ,-5]

#get subarray and subarray sum
print(get_subarray_sum_1(s_array))