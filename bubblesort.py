def bubblesort(unsorted):
    l1 = unsorted
    
    for i in range(len(l1)):
        for j in range(len(l1)): 
            if j+1 >= len(l1):
                continue
            elif l1[j] > l1[j+1]:
                temp1 = l1[j]
                temp2 = l1[j+1]
                l1[j] = temp2
                l1[j+1] = temp1

    return l1