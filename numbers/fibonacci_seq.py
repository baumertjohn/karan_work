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
        fib_x, fib_y = 0, 1
        print(f"{fib_x}\n{fib_y}")
        for i in range(2, num):
            fib_z = fib_x + fib_y
            print(fib_z)
            fib_x, fib_y = fib_y, fib_z
            i += 1


if __name__ == '__main__':
    main()
