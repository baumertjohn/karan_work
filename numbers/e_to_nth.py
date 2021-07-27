# A program to generate 'e' to a given number of decimal places
# Will use code from the previous PI to the nth program.
# Note: There are also 15 digits after the decimal when Python calculates 'e'.
# 20210727 - Change e_const to string to allow for 100 digits

E_CONST = ('2.7182818284590452353602874713526624977572470936999595749669676277'
           '240766303535475945713821785251664274')


def main():
    while True:
        try:
            digits = int(input("How many digits of 'e' would you like to "
                               + "display? (100 max): "))
        except ValueError:
            print("Input must be an integer between 1 and 100.")
            continue

        if 0 < digits < 101:
            break
        else:
            print("Digits must be between 1 and 100.")

    print(E_CONST[0:digits + 2])  # +2 for first digit and decimal point


if __name__ == '__main__':
    main()
