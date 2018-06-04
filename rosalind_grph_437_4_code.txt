def overlap(a, b):
    if b[0:3] == a[len(a) - 3: len(a)]:
        print(a, " ", b)


#check_str = {'Rosalind_0498': 'AAATAAA', 'Rosalind_2391': 'AAATTTT', 'Rosalind_2323': 'TTTTCCC', 'Rosalind_0442': 'AAATCCC', 'Rosalind_5013': 'GGGTGGG'}

file_obj = open("rosalind_grph.txt", 'r')

list_key = []
list_val = []

for index, str_line in enumerate(file_obj.readlines()):
    if (index) % 3 == 0:
        list_key.append(str_line.strip("\n"))
    else:
        list_val.append(str_line.strip("\n"))

list_val = [list_val[i] + list_val[i + 1] for i in range(0, len(list_val), 2)]


#print(list_key)
#print(list_val)
check_str = dict(zip(list_key, list_val))

for i in check_str:
    for j in check_str:
        if i is not j:

            if check_str.get(j)[0:3] == check_str.get(i)[len(check_str.get(i)) - 3: len(check_str.get(i))]:

                print(i.strip(">"),j.strip(">"))