def recr_func(str1, str2 = ''):
    if len(str1) is 0:
        return str2
    elif len(str2) is 0:
        str2 = str1.pop(0)
        return recr_func(str1, str2)
    else:
        for elements in range(len(str1)):
                list_val = str1[elements]
                t = len(list_val)
                half_len = t/2
                for iter1 in range(int(t/2)):
                    full_len = t - iter1
                    if str2.startswith(list_val[iter1:]):
                        str1.pop(elements)
                        return recr_func(str1, list_val[:iter1]+str2)
                    elif str2.endswith(list_val[:full_len]):
                        str1.pop(elements)
                        return recr_func(str1, str2+list_val[full_len:])

file_obj = open("rosalind_long.txt", 'r')
new_listt = ''
listt = file_obj.readlines()
strr = []
for a, val in enumerate(listt):
    if val.startswith(">Rosa"):
        listt[a] = "\n"
    else:
        listt[a] = val.rstrip()

new_listt = ''.join(listt)
finalString = new_listt.split()
print (recr_func(finalString))