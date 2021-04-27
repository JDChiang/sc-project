"""
File: complement.py
Name: Frank Chiang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program will convert the DNA sequence to complementary sequence.
    """
    dna = input('Pleas give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    print(build_complement(dna))


def build_complement(dna):
    """
    :param dna: str, nucleotide
    :return: str, complement ans
    """
    ans = ''
    for base in dna:
        if base == 'T':
            ans += 'A'
        elif base == 'A':
            ans += 'T'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
