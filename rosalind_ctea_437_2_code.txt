# EDIT DISTANCE ALIGNMENT
fileobj = open('rosalind_ctea.txt', 'r')
filecontent = fileobj.readlines()
for a, val in enumerate(filecontent):
    if val.startswith(">Rosa"):
        filecontent[a] = "\n"
    else:
        filecontent[a] = val.rstrip()
filelines = ''.join(filecontent)
filelinewise = filelines.split()

s = filelinewise[0]
t = filelinewise[1]

matrix = [[0 for val2 in range(len(t) + 1)] for val1 in range(len(s) + 1)]

count = [[0 for val2 in range(len(t) + 1)] for val1 in range(len(s) + 1)]
for c1 in range(0, len(s) + 1):
    count[c1][0] = 1
for c2 in range(0, len(t) + 1):
    count[0][c2] = 1

for val1 in range(1, len(s) + 1):
    matrix[val1][0] = val1

for val1 in range(1, len(t) + 1):
    matrix[0][val1] = val1

for val1 in range(1, len(s) + 1):
    for val2 in range(1, len(t) + 1):
        if s[val1 - 1] == t[val2 - 1]:
            weight = 0
        else:
            weight = 1
        matrix[val1][val2] = min(matrix[val1 - 1][val2] + 1, matrix[val1][val2 - 1] + 1, matrix[val1 - 1][val2 - 1] + weight)
        if(matrix[val1][val2] == (matrix[val1-1][val2] + 1)):
            count[val1][val2] += count[val1-1][val2]
        if((matrix[val1][val2] ) == (matrix[val1 - 1][val2-1] + weight)):
            count[val1][val2] += count[val1 - 1][val2-1]
        if((matrix[val1][val2]) == (matrix[val1][val2-1] + 1)):
            count[val1][val2] += count[val1][val2-1]

print(count[len(s)][len(t)]% 134217727)