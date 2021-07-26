# A program to find PI to the Nth digit
# Python PI limit is 15 digits after decimal
import math

# print(math.pi)

def main():
    while True:
        try:
            digits = int(input("How many digits of PI would you like to display? " 
                            + "(15 max): "))
        except ValueError:
            print("Input must be an integer between 1 and 15.")
            continue
        
        if 0 < digits < 15:
            break
        else:
            print("Digits must be between 1 and 15.")
            
    pi = str(math.pi)
    print(pi[0:digits + 2])


if __name__ == '__main__':
    main()
