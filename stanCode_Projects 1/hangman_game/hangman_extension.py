"""
File: hangman.py
Name: Frank Chiang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is the extension of hangman game(with pic).
    """
    ans = choose_the_answer()
    blocking = block_the_answer(ans)
    guessing(ans, blocking)
    print('The word was: ' + ans)


def choose_the_answer():
    """
    Random choose the word.
    :return: str, the answer.
    """
    ans = random_word()
    return ans


def block_the_answer(ans):
    """
    This function is to block the answer to '---'
    :param ans: str, the answer.
    :return: the blocked answer.
    """
    block = ''
    for i in range(len(ans)):
        ch = ans[i]
        if ch.isalpha():
            block += '-'
    return block


def guessing(ans, block):
    """
    This function is for player to guess the word.
    :param ans: str, the answer.
    :param block: str, the blocked answer.
    """
    # The remaining guessing times.
    remain = N_TURNS
    while True:
        # The shown pic will depend on how many remaining times.
        picture(remain)
        # Showing the blocked answer, giving player hint how many characters in the word.
        print('The word looks like: ' + block)
        temp_block = ''
        # Break the loop, point to win the game.
        if block == ans:
            print('You are correct!')
            break
        # Break the loop, point to lose the game.
        if remain == 0:
            print('You are completely hung!:(')
            break
        else:
            print('You have ' + str(remain) + ' guesses left.')
        # Input the word.
        guess = str(input('Your guess: '))
        # Make the guess case insensitive.
        new_guess = guess.upper()
        # If input multiple characters, it will show the wrong message.
        if len(new_guess) > 1:
            print('illegal format.')
        # If input one character
        elif new_guess.isalpha():
            # Wrong guess.
            if ans.find(new_guess) == -1:
                print('Their is no ' + str(new_guess) + ' in the word.')
                remain -= 1
            # Right guess
            else:
                for i in range(len(block)):
                    if new_guess == ans[i]:
                        temp_block += new_guess
                    else:
                        temp_block += block[i]
                block = temp_block
        else:
            print('illegal format.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def pic_1():
    print("|／　　　|")
    print("|　　　　")
    print("|　　　　 ")
    print("|　　　 ")


def pic_2():
    print("|／　　　|")
    print("|　　　　Ｏ")
    print("|　　　　 ")
    print("|　　　 ")


def pic_3():
    print("|／　　　|")
    print("|　　　　Ｏ")
    print("|　　　　｜")
    print("|　　　 ")


def pic_4():
    print("|／　　　|")
    print("|　　　　Ｏ")
    print("|　　　／｜")
    print("|　　　 ")


def pic_5():
    print("|／　　　|")
    print("|　　　　Ｏ")
    print("|　　　／｜＼")
    print("|　　　 ")



def pic_6():
    print("|／　　　|")
    print("|　　　　Ｏ")
    print("|　　　／｜＼")
    print("|　　　 ／")



def pic_7():
    print("|／　　　|")
    print("|　　　　Ｏ")
    print("|　　　／｜＼")
    print("|　　　 ／＼")


def picture(i):
    head()
    if i == 0:
        pic_7()
    elif i == 1:
        pic_6()
    elif i == 2:
        pic_5()
    elif i == 3:
        pic_4()
    elif i == 4:
        pic_3()
    elif i == 5:
        pic_2()
    elif i == 6:
        pic_1()
    else:
        pic_0()
    bottom()


def head():
    for i in range(6):
        print('－', end='')
    print('')


def bottom():
    for i in range(3):
        print("|")


def pic_0():
    print("|／　　　")
    print("|　　　　")
    print("|　　　　")
    print("|　　　 ")

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
