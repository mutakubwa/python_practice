def sort(unsorted):
    '''
    merge sort function to recursively sort using merge sort
    '''
    l1 = unsorted
    a = 0
    b = len(l1)-1
    k = (a + b) // 2 #middle index
    sorted = []

    if (a == b):
        sorted.append(l1[0])

    elif ( len(l1) == 2 ):
        array1 = l1[:a+1]
        array2 = l1[b:]
        
        if (array1[0] > array2[0]):
            sorted.append( array2[0] )
            sorted.append( array1[0] )
        else:
            sorted.append( array1[0] )
            sorted.append( array2[0] )

    else:
        array1 = l1[:k]
        array2 = l1[k:]

        q1 = sort(array1)
        q2 = sort(array2)

        q3 = merge(q1, q2)

        sorted += q3
    
    return sorted

def merge(left, right):
    '''
    merge two arrays while sorting them
    '''
    result=[]
    in_left = in_right = 0
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        while len(result) <= ( len(left) + len(right) ):
            if left[in_left] <= right[in_right]:
                result.append( left[in_left] )
                in_left += 1
            else:
                result.append( right[in_right] )
                in_right += 1
            
            #if at the ned just add either array
            if in_right == len(right):
                result += left[in_left:]
                break

            if in_left == len(left):
                result += right[in_right:]
                break
        
    
    return result

