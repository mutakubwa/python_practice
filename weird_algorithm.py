
def weird_algo(num):
    i = num
    final = []
    final.append(i)
    while i != 1:
        #check if even
        if i % 2 == 0:
            i //= 2
            final.append(i)
        else:
            #check oddd
            i *= 3
            i += 1 
            final.append(i)
    return final

#num = input()
#[print(x) for x in weird_algo(int(num))]

print(3<<4)

