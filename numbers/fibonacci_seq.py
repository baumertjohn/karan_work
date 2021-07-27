# Enter a number and have the program generate the Fibonacci sequence to that
# number or to the Nth number.


def main():
    fib_num = get_user_input()
    create_fib_sequence(fib_num)


def get_user_input():
    while True:
        try:
            user_input = int(input("Please enter integer to calculate "
                                   + "Fibonacci Sequence: "))
        except ValueError:
            print("Please enter an integer.\n")
            continue

        if user_input < 0:
            print("Please enter positive integer.\n")
            continue

        return user_input


def create_fib_sequence(num):
    if num in (0, 1):
        print(num)
        return
    else:
        pass


if __name__ == '__main__':
    main()
