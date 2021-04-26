#imports
import re


#define function to reutrn number of characters
def get_num_chars_1(char_str, seed_list):
    '''
    Linearly get through all the characters and return longest repetition
    '''
    longest = 1
    temp = 0
    temp_found_c = ''
    found_c = ''

    for cha in char_str:
        if (cha != temp_found_c ):
            temp_found_c = cha
            temp = 0
        temp += 1
        if temp > longest:
            found_c = temp_found_c
            longest = temp   
    return (longest)

def get_num_chars_2(char_str, seed_list):
    '''
    use regular epxression but by going through l=ist of characters to search
    '''
    longest = 1
    found_c = ''
    #index = 0
    found = ''
    for x in range(len(char_str)):
        pattern = '([' + char_str[x] +']{2,})'
        reg = re.compile(pattern)
        result = reg.search(char_str)
        if result is None:
            continue
        found_p = result[1]
        if (len(found_p) > longest) and char_str[x] in seed_list:
            longest = len(found_p)
            found_c = char_str[x]
        index = x + len(found_p)
        x = index
    return longest

def get_num_chars_3(char_str, seed_list):
    '''
    use regular epxression but by going through seed list of characters
    '''
    longest = 1
    found_c = ''
    found = ''
    for x in seed_list:
        pattern = '([' + x +'^ ]{2,})'
        #print(pattern)
        reg = re.compile(pattern)
        result = reg.findall(char_str)
        if result is None:
            continue
        for item in result:
            if (len(item) > longest):
                longest = len(item)
                found_c = x

    return longest

def get_num_chars_4(char_str, seed_list):
    '''
    use regular epxression but by going through seed list of characters
    '''
    s_c = set(char_str)
    c_c = s_c & set(seed_list)
    #print(c_c)
    longest = 1
    found_c = ''
    found = ''
    for x in c_c:
        pattern = '([' + x +'^ ]{2,})'
        #print(pattern)
        reg = re.compile(pattern)
        result = reg.findall(char_str)
        #print(result)
        if result is None:
            continue
        for item in result:
            if (len(item) > longest):
                longest = len(item)
                found_c = x

    return longest



#get Characters
seed_list = ['A','C','G','T']
try:
    while(True):
        entry = input()
        if (len(entry) <= 0 ) or (len(entry) >= 1000000 ):
            continue
        break
except:
    pass

#go through each of the characters - method 1
print(get_num_chars_1(entry, seed_list))

#go through each of the characters - method 2
#print(get_num_chars_2(entry, seed_list))

#go through each of the characters - method 2
#print(get_num_chars_3(entry, seed_list))
#go through each of the characters - method 2
#print(get_num_chars_4(entry, seed_list))