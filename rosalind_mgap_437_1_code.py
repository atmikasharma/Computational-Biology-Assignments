#EDIT DISTANCE ALIGNMENT
fileobj=open('blah.txt', 'r')
filecontent=fileobj.readlines()
for a, val in enumerate(filecontent):
    if val.startswith(">Rosa"):
        filecontent[a]="\n"
    else:
        filecontent[a]=val.rstrip()
filelines=''.join(filecontent)
filelinewise=filelines.split()

s=filelinewise[0]
t=filelinewise[1]

matrix=[[0 for val2 in range(len(t)+1)] for val1 in range(len(s)+1)]

for val1 in range(1,len(s)+1):
    matrix[val1][0]=val1

for val1 in range(1,len(t)+1):
    matrix[0][val1]=val1

for val1 in range(1,len(s)+1):
    for val2 in range(1,len(t)+1):
        if s[val1-1]==t[val2-1]:
            weight=0
        else:
            weight=10
        matrix[val1][val2]=min(matrix[val1 - 1][val2] + 1,matrix[val1][val2-1]+1, matrix[val1-1][val2-1] + weight)

print(matrix[len(s)][len(t)])