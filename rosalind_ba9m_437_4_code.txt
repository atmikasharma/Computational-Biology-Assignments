alphabet = ['$', 'A', 'T', 'C', 'G']

def BetterBWMatching(foccurence, lcol, patt, count_dic):
    top = 0
    bottom = len(lcol) - 1
    while top <= bottom:
        if patt:
            char = patt[-1]
            patt = patt[:-1]
            columnex = lcol[top:(bottom + 1)]
            if char in columnex:
                top = foccurence[char] + count_dic[char][top]
                bottom = foccurence[char] + count_dic[char][bottom+1] - 1
            else:
                return 0
        else:
            return bottom - top + 1

if __name__=="__main__" :
    fileobj   = "rosalind_ba9m.txt"
    bwt, patterns = [x.strip() for x in open(fileobj).readlines()]
    patterns = patterns.split()
    print(bwt)
    print(patterns)
    #bwt1= 'GGCGCCGC$TAGTCACACACGCCGTA'
    #print(bwt1)
    #firstcol2= sorted(bwt1)
    #patterns = ['ACC','CCG', 'CAG']
    firstcol = sorted(bwt)
    print(firstcol)
    print(patterns)
    #print(firstcol2)
    foccur = dict()
    for val1 in alphabet:
        foccur[val1] = firstcol.index(val1)
    foccurence = foccur
    dictionary = dict()
    for val2 in alphabet:
        dictionary[val2] = [0]*(len(bwt) + 1)
    for val3 in range(len(bwt)):
        found = bwt[val3]
        for val2 in alphabet:
            if val2 == found:
                dictionary[val2][val3+1] = dictionary[val2][val3] + 1
            else:
                dictionary[val2][val3+1] = dictionary[val2][val3]
    count_dic = dictionary
    match_num = []
    for patt in patterns:
        tata = BetterBWMatching(foccurence, bwt, patt, count_dic)
        match_num.append(tata)

    print(' '.join(map(str, match_num)))