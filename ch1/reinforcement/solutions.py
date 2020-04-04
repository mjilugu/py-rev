
import random

# R-1.1
def is_multiple(n, m):
    return n % m == 0

# R-1.2
def is_even(k):
    return k % 2 == 0

# R-1.3
def maxmin(data):
    max_n = data[0]
    min_n = data[0]

    for num in data:
        if num > max_n:
            max_n = num
        if num < min_n:
            min_n = num

    return (min_n,max_n)

# R-1.4
def sum_squares_all(n):
    sum = 0

    if n <= 0:
        raise ValueError("Value entered is not positive integer")

    for num in range(n):
        sum += num*num

    return sum

# R-1.5
# sum([ r*r for r in range(5) ])

# R-1.6
def sum_squares_odd(n):
    sum = 0

    if n <= 0:
        raise ValueError("Value entered is not positive integer")

    for num in range(n):
        if num % 2 != 0:
            sum += num*num

    return sum

# R-1.7
# sum([ r*r for r in range(5) if r % 2 != 0 ])

# R-1.8
# j = n + k for -n <= k < 0.

# R-1.9
# [50,60,70,80]
# range(50,90,10)

# R-1.10
# [8, 6, 4, 2, 0, -2, -4, -6, -8]
# range(8,-10,-2)

# R-1.11
# [1, 2, 4, 8, 16, 32, 64, 128, 256]
# [2**i for i in range(0,9)]

# R-1.12
def choice(data):
    random_index = random.randrange(len(data))
    return data[random_index]

if __name__ == '__main__':
    # R-1.1
    print('20 is multiple of 5.', is_multiple(20,5))
    print('23 is multiple of 5.', is_multiple(23,5))

    # R-1.2
    print()
    print('10 is even.', is_even(10))
    print('15 is even.', is_even(15))

    # R-1.3
    print()
    list1 = [ 1, 2, 7, 4, 3, -1 ]
    min_n,max_n = maxmin(list1)
    print(f"min of {list1} is {min_n}")
    print(f"max of {list1} is {max_n}")

    # R-1.4
    print()
    try:
        print(f"Sum of squares of odds upto {5} is {sum_squares_all(5)}")
        print(f"Sum of squares of odds upto {6} is {sum_squares_all(6)}")
        print(f"Sum of squares of odds upto {-9} is {sum_squares_all(-9)}")
    except ValueError as v_err:
        print(v_err)

    # R-1.5
    print()
    sum_1 = sum([ r*r for r in range(5) ])
    print(f"Sum of squares upto 5 with list comprehension {sum_1}")

    # R-1.6
    print()
    try:
        print(f"Sum of squares of odds upto {5} is {sum_squares_odd(5)}")
        print(f"Sum of squares of odds upto {6} is {sum_squares_odd(6)}")
        print(f"Sum of squares of odds upto {-9} is {sum_squares_odd(-9)}")
    except ValueError as v_err:
        print(v_err)

    # R-1.7
    print()
    sum_1 = sum([ r*r for r in range(5) if r % 2 != 0 ])
    print(f"Sum of squares of odds upto 5 with list comprehension {sum_1}")

    # R-1.12
    print()
    data = [ 4, -4, 5, 3, 99, 21, -3 ]
    print(f"Random choice from {data}: {choice(data)}")
    print(f"Random choice from {data}: {choice(data)}")
    print(f"Random choice from {data}: {choice(data)}")
