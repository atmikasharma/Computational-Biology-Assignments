def BWMatching(fcol, lcol, patt, ltofmap):
    top = 0
    bottom = len(lcol) - 1
    while top <= bottom:
        if patt:
            char = patt[-1]
            patt = patt[:-1]
            columnex = lcol[top:(bottom + 1)]
            if char in columnex:
                top_index = columnex.index(char) + top
                last_index = len(columnex) - columnex[::-1].index(char) + top -1
                top = ltofmap[top_index]
                bottom = ltofmap[last_index]
            else:
                return 0
        else:
            return bottom - top + 1

if __name__=="__main__" :
    fileobj   = "rosalind_ba9l.txt"
    bwt, patterns = [x.strip() for x in open(fileobj).readlines()]
    patterns = patterns.split()
    firstcol = sorted(bwt)
    index_list = []
    for i in bwt:
        index = firstcol.index(i)
        index_list.append(index)
        firstcol[index] = "#"

    firstcol = sorted(bwt)
    ltofmap = index_list
    match_num = []

    for patt in patterns:
        match_num.append(BWMatching(firstcol, bwt, patt, ltofmap))
    print(' '.join(map(str, match_num)))