# A program to generate 'e' to a given number of decimal places
# Will probably use some code from the previous PI to the nth program.
# Note: There are also 15 digits after the decimal when Python calculates 'e'.

import math


def main():
    while True:
        try:
            digits = int(input("How many digits of 'e' would you like to "
                               + "display? (15 max): "))
        except ValueError:
            print("Input must be an integer between 1 and 15.")
            continue

        if 0 < digits < 16:
            break
        else:
            print("Digits must be between 1 and 15.")

    e_const = str(math.exp(1))
    print(e_const[0:digits + 2])


if __name__ == '__main__':
    main()
