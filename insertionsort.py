def sort(unsorted):
    l1 = unsorted
    s_l = []
    if len(l1) <= 1 :
        return l1

    s_l.append(l1[0])

    for i in range (1, len(l1) ):
        if(max(s_l) > l1[i]):
            if(len(s_l) == 1 ):
                temp1 = s_l[0]
                s_l[0] = l1[i]
                s_l.append(temp1)
                
            else:
                temp1 = []
                additem = 0
                for item in s_l:
                    if item < l1[i]:
                        temp1.append(item)
                    elif item == l1[i]:
                        temp1.append(item)
                    else:
                        if (additem == 0):
                            temp1.append(l1[i])
                            temp1.append(item)
                            additem += 1
                        else:
                            temp1.append(item)
                
                s_l = []
                s_l += temp1

        elif(max(s_l) <= l1[i]):
            temp1 = l1[i]
            s_l.append(temp1)
        else:
            pass 

    return s_l


