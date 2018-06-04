def resultant(dic):
    for each in dic:
        print(str(each).replace("'", ''))

def looping(dic, li):
    for value in range(len(li)):
        dic[li[value][:len(li[value]) - 1], li[value][1:]] = 1

def func(var):
    complement_is = ""
    for each in var[::-1]:

        #global complement_is

        #find() string in "TACG
        complement_is += "ATGC"["TACG".find(each)]
    return complement_is

if __name__ == '__main__':

    infile = "rosalind_dbru.txt"

    text = [x.strip() for x in open(infile).readlines()]

 #   global complement_is
  #  global list
   # global dictionary


    list = [] #s
    dictionary = {} #c

    for each_val in text:

        list.append(each_val)

        list.append(func(each_val))



    looping(dictionary, list)

    resultant(dictionary)