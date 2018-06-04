import math

strr = 'ATATTACTGGGAAGATCACGAAGCTCAAGCCAGCGCCAGCGCTATATGTAGCTCTAGACGTACACTGGCTCGGATTGGCATGTTATAA'

list1 = [0.056, 0.115, 0.186, 0.234, 0.318, 0.336, 0.419, 0.473, 0.555, 0.558, 0.642, 0.702, 0.749, 0.805, 0.862, 0.906]

temp = 1.000

new_list = []

for gc in list1:
    g = c = gc/2
    a = t = (1-gc)/2
    for val in strr:
        if val is 'A':
            temp = temp * a
        if val is 'C':
            temp = temp * c
        if val is 'G':
            temp = temp * g
        if val is 'T':
            temp = temp * t

    new_list.append(math.log10(temp))
    temp = 1.000
for vals in new_list:
    print("{0:.3f}".format(vals))