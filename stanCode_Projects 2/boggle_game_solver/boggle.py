"""
File: boggle.py
Name: Jo-Di(Frank), Chiang
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dict_lst = {}  # dict, used to store the dictionary
input_word = []

count = 1
word_count = 0


def main():
    """
    TODO: Player input 16 alphabet in a 4 by 4 square, and this program will find any possible vocab in this square
    """
    read_dictionary()
    enter_alphabet()
    print(f"found {word_count} words in total")


def enter_alphabet():
    """
    This function will need us to input 16 letters in a 4 by 4 boggle form,
    each row of letter will split by space.
    """
    global count
    for i in range(4):
        letter = input(f"{count} row of letters: ").lower()
        row_info = []
        if len(letter) != 7 or letter[1] != ' ' or letter[3] != ' ' or letter[5] != ' ' \
                or not letter[2].isalpha() \
                or not letter[4].isalpha() \
                or not letter[6].isalpha():
            print('Illegal format')
            break
        else:
            count += 1
            row_info.append(letter[0])
            row_info.append(letter[2])
            row_info.append(letter[4])
            row_info.append(letter[6])
            input_word.append(row_info)
    if len(input_word) == 4:
        print("Searching......")
        find_word(input_word)


def find_word(input_lst):
    """
    :param input_lst: lst, storing the user-input alphabet
    """
    ans = []
    for x in range(4):
        for y in range(4):
            letter_coordinate = [(x, y)]  # The letter coordinates store in a list as tuple
            get_help(x, y, input_lst, input_word[x][y], letter_coordinate, ans)


def get_help(row, col, input_lst, current_ans, letter_coordinate, ans):
    """
    :param row: int, current x coordinate.
    :param col: int, current y coordinate.
    :param input_lst: lst, storing the user-input alphabet
    :param current_ans: str, current answer used to check if it's in the dic
    :param letter_coordinate: lst, the used coordinate of the letter, stored as tuple form
    :param ans: lst, found vocab in the dictionary
    """
    global word_count
    if len(current_ans) >= 4 and current_ans in dict_lst and current_ans not in ans:   # base case
        ans.append(current_ans)
        print(f"found \"{current_ans}\"")
        word_count += 1
    if has_prefix(current_ans):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    pass
                else:
                    x_cor = row + i
                    y_cor = col + j
                    if 0 <= x_cor < 4 and 0 <= y_cor < 4:
                        if (x_cor, y_cor) not in letter_coordinate:
                            # Choose
                            letter_coordinate.append((x_cor, y_cor))
                            current_ans += input_lst[x_cor][y_cor]
                            # Explore
                            get_help(x_cor, y_cor, input_lst, current_ans, letter_coordinate, ans)
                            # Un-choose
                            current_ans = current_ans[:-1]
                            letter_coordinate.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for word in f:
            dict_word = word.strip()
            dict_lst[dict_word] = 0


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
