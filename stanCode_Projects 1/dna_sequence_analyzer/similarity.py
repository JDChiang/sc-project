"""
File: similarity.py
Name: Frank Chiang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will help users to do the sequence alignment.
    We input both long sequence and short sequence, the program will tell us the most similar region.
    """

    long_seq = input_long_sequence()
    short_seq = input_short_sequence()
    ans = matching(long_seq, short_seq)
    print('The best match sequence is: ' + ans)


def input_long_sequence():
    """
    This function will need the users to input the long DNA sequence.
    :return: The case insensitive sequence will return as new_ls.
    """
    ls = str(input('Please give me a DNA sequence to search: '))
    new_ls = ls.upper()
    return new_ls


def input_short_sequence():
    """
    This function will need the users to input the DNA sequence they want to match.
    :return: The case insensitive sequence will return as new_ss.
    """
    ss = str(input('What DNA sequence would you like to match? '))
    new_ss = ss.upper()
    return new_ss


def matching(new_ls, new_ss):
    """
    This function will start matching both sequence and find the most similar part.
    :param new_ls: str, the long sequence.
    :param new_ss: str, the short sequence.
    :return: str, the most similar region of sequence.
    """
    ans = ''
    temp_data = 0
    # The matching will stop at the last nucleotide.
    for i in range(len(new_ls) - len(new_ss) + 1):
        # To find the maximum number of match.
        count = 0
        # The size of the sequence want to match. eq: TGC to GTA or TGACC to GATCA
        l_seq = new_ls[i:i + len(new_ss)]
        for j in range(len(new_ss)):
            num_l_seq = l_seq[j]
            s_seq = new_ss[j]
            # If nucleotide is the same, make it count.
            if num_l_seq == s_seq:
                count += 1
        # To replace the maximum match
        if count > temp_data:
            temp_data = count
            ans = l_seq
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
