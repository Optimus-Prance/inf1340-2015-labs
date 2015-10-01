#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowel_or_consonant():
    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should display
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """

    print("hello, please enter a letter from the Alphabet"
          " and I will tell you if it is a vowel or consonant. Please only input lowercase letters")
    letter_choice = raw_input()
    if letter_choice == "a":
        print("vowel")
    elif letter_choice == "e":
        print("vowel")
    elif letter_choice == "i":
        print("vowel")
    elif letter_choice == "o":
        print("vowel")
    elif letter_choice == "u":
        print("vowel")
    elif letter_choice =="y":
        print("sometimes a vowel, sometimes a consonant")
    else:
        print("consonant")

print(vowel_or_consonant())
