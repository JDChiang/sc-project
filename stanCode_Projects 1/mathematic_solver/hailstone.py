"""
File: hailstone.py
Name: Frank Chiang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program will demonstrate how Hailstone sequence works.
    """
    greeting()
    print('')
    n = int(input('Type your number: '))
    total = -1
    while True:
        # To count how many steps.
        total += 1
        if n == 1:
            break
        # If the number is even.
        elif n % 2 == 0:
            print(str(int(n)) + ' is even, so I take half: ' + str(int(n / 2)))
            n = n / 2
        # If the number is odd.
        elif n % 2 == 1:
            print(str(int(n)) + ' is odd, so I make 3n+1: ' + str(int(3 * n + 1)))
            n = 3 * n + 1
    print('It took ' + str(int(total)) + ' steps to reach 1.')


def greeting():
    """
    This function is for greeting!
    """
    print('This program computes Hailstone sequences.')

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
