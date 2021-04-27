"""
File: anagram.py
Name: Jo-Di(Frank), Chiang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


# Global variable
dict_lst = []   # List, used to store the dictionary
anagrams = []   # List, saved all the found anagrams


def main():
    """
    TO DO: This program will find all the anagrams based on the word we input.
    """
    global anagrams
    print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        ans = input(str('Find anagrams for: '))
        new_ans = ans.lower()
        if new_ans == EXIT:
            break
        find_anagrams(new_ans)
        print(anagrams)


def read_dictionary():
    """
    Open the FILE and loop over the txt, saving into global dict_lst
    """
    with open(FILE, 'r') as f:
        for word in f:
            dict_word = word.strip()
            dict_lst.append(dict_word)


def find_anagrams(s):
    """
    :param s: str, new_answer
    """
    global anagrams
    start_time = time.time()
    get_help(s, '', len(s), anagrams, [])
    end_time = time.time()
    print(end_time-start_time)


def has_prefix(sub_s):
    """
    :param sub_s: find prefix
    :return: bool
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


def get_help(s, current_word, word_length, word_list, index):
    """
    :param s: str, new_answer in main()
    :param current_word: str, storing current str
    :param word_length: int, length of new_answer
    :param word_list: lst, storing anagrams
    :param index: lst, storing word index
    """
    if len(current_word) == word_length:    # base case
        if current_word in dict_lst:
            if current_word not in word_list:
                word_list.append(current_word)
                print('searching......')
                print('Found: ' + current_word)
    else:
        for i in range(len(s)):     # recursive case
            if i not in index:
                # Choose
                index.append(i)
                current_word += s[i]
                # Explore
                if has_prefix(current_word):
                    get_help(s, current_word, word_length, word_list, index)
                # Un-choose
                current_word = current_word[:-1]
                index.pop()


if __name__ == '__main__':
    main()
