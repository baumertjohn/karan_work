# A program to find PI to the Nth digit
# Python PI limit is 15 digits after decimal
# 20210727 - Change PI to string to allow for 100 digits

PI = ('3.141592653589793238462643383279502884197169399375105820974944592307816'
      '4062862089986280348253421170679')


def main():
    while True:
        try:
            digits = int(input("How many digits of PI would you like to "
                               + "display? (100 max): "))
        except ValueError:
            print("Input must be an integer between 1 and 100.")
            continue

        if 0 < digits < 101:
            break
        else:
            print("Digits must be between 1 and 100.")

    print(PI[0:digits + 2])  # +2 for first digit and decimal point


if __name__ == '__main__':
    main()
