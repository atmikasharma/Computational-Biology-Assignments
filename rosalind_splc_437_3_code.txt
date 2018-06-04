CODONS = {'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
          'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
          'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
          'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
          'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
          'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
          'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
          'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
          'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
          'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
          'UAA': '',       'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
          'UAG': '',       'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
          'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
          'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
          'UGA': '',       'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
          'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}

in_str = ''

file_obj = open("rosalind_splc.txt", 'r')

str_list = []
intron = []

for index, str_line in enumerate(file_obj.readlines()):
    if index != 0 and index <= 16:
        str_list.append(str_line.strip("\n"))
    elif index > 17 and (index%2 == 0):
        intron.append(str_line.strip("\n"))

in_str = ''.join(str_list)

for i in intron:
    in_str = in_str.replace(i, "")

new_str = in_str.replace('T', 'U')

strr = ''

for i in range(0, len(new_str)-2, 3):
    strr += CODONS.get(new_str[i:i+3])
    if CODONS.get(new_str[i:i+3]) is '':
        print(strr)
        exit()


print(strr)