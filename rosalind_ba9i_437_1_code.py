s = "CAAGAGACCGCTTGCATAGTGCACGGGACGATACATTGAGATAAAGGCACGACGACGCCATCGGCGTATGCTGTGGTTTCATCATTTTGCTTATCTACGTTATCGACTATTATTAGGTTGAATTCGGATCTAAACTGTTGTCGAATGACGGACGCAGCACCTCTGCGCACGCTGTTGCACGACGGATCCCTTGCTATTTTTAAGCCACTACTTGAGTACATGTTTCAACGATGTGTTATTCAATTTTCCTATGATGCAGGCTCAATCTTTCCACCAACGACGGGGTCACAACAGGTGCTGTCTTCATTTAACGGCCACCTTGCGGTTAACTTAGATATGCCGCATGGGTGCTGTCCCTTGCGTACAATAGACCTCGGCTCCCTAGATGGTCCCCTCTTCACGGAAATAGCGACCAATCAGAAGGCGTGCTTTTGCACCGGCTCTGGGTACGACCGCTGATAGACTCTGAGTTTCGCGTAGGAAAGCACGACCCGAGTATATACATCCCGATGACACCCTATGGAACAGGCCGGCGTTAGGAACCAGCGAGACGTAGGTTTATGCTAGCTGGGCTCAAACATAGTAGGCGAAAGGCTAAGAAGTCACGTTCCCATGAGGCCTTAATTAACGTTCTATGGAGACACATCGTGGTACATCCATTCTGTTGTCTGGAGTCCATCAGCTGCTTGTTACCTGCTGCGGCGGACCGCACCATGTTGCACGACAGTCGTGTTAGCCCGTATAATGCGGCCCGAATACGCCGGATGATCGCTTCTCACACGACTGGGCACATACCCTGATGTCCAGTGACGCTCCGCGTGGCCACGCTGTTATCCATAC$"

matrix = [""] * len(s)

for i in range(len(matrix)):
    matrix[i] = s[i:len(s)] + s[0:i]

matrix.sort()

str = ""

for j in range(len(matrix)):
    val = matrix[j]
    str = str + val[len(s)-1]


print(str)