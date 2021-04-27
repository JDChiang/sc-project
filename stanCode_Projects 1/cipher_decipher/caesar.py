"""
File: caesar.py
Name: Frank Chiang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program uses method of alphabet shifting to encrypt/decrypt the messages
    """
    first = type_secret_number()
    second = transfer_new_alphabet(first)
    third = type_ciphered_string()
    ans = transfer(first, second, third)
    print('The deciphered string is: ' + str(ans))


def type_secret_number():
    """
    This function is used to input the number
    :return: remainder of input number
    """
    number = int(input('Secret Number: '))
    number = number % 26
    return number


def transfer_new_alphabet(number):
    """
    :param number: int, remainder of input number.
    :return:Str,  New ordered alphabet table.
    """
    new_alphabet = ALPHABET[26-number:27] + ALPHABET[0:26-number]
    return new_alphabet


def type_ciphered_string():
    """
    This function is used to input the encrypted message.
    :return:Str, message turns to case insensitive.
    """
    input_ciphered_string = str(input('What\'s the ciphered string? '))
    new_ciphered_string = input_ciphered_string.upper()
    return new_ciphered_string


def transfer(number, new_ciphered_alphabet, new_ciphered_string):
    """
    Decrypt/Encrypt the message.
    :param number: int,
    :param new_ciphered_alphabet: str, New ordered alphabet table.
    :param new_ciphered_string: str, case insensitive message.
    :return: str, the decrypted/encrypted message.
    """
    ans = ''
    # find the length of new_ciphered_string
    for i in range(len(new_ciphered_string)):
        ch = new_ciphered_string[i]
        # Find the number in new order table
        num_ch = new_ciphered_alphabet.find(ch)
        # Search the word in the old alphabet table.
        new_ch = ALPHABET[num_ch]
        if num_ch > -1:
            ans += new_ch
        else:
            ans += ch
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
