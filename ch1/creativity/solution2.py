import operator

# C-1.21
def readlines(lines):
    try:
        while True:
            lines.append(input())
    except EOFError:
        print("Done")

# C-1.22
def dot_product(a,b):
    if len(a) != len(b):
        raise ValueError("The arrays a,b must be of equal length.")

    c=list()
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

# C-1.23
def f_append(data, item, index):
    try:
        data[index]=item
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

# C-1.24
def count_vowels(str):
    l_vowels={'a','e','i','o','u'}
    count=0

    for char in str:
        if char in l_vowels:
            count += 1

    return count

# C-1.25
def remove_punctuation(str):
    regular_chars = [chr(i) for i in range(97,123)]
    regular_chars.append(' ')
    regular_chars += [chr(i) for i in range(65,91)]
    new_str = ''
    print(regular_chars)

    for char in str:
        if char in regular_chars:
            new_str+=char

    return new_str

# C-1.26
def get_formula(a,b,c):
    operations = [
        {"op":operator.add,"symbol":"+"},
        {"op":operator.sub,"symbol":"-"},
        {"op":operator.mul,"symbol":"*"},
        {"op":operator.truediv,"symbol":"/"},
        {"op":operator.mod,"symbol":"%"},
        {"op":operator.pow,"symbol":"^"},
        {"op":operator.floordiv,"symbol":"//"}
    ]

    for op in operations:
        if a == op['op'](b,c):
            print(f">>>{a} = {b} {op['symbol']} {c}")
        elif op['op'](a,b) == c:
            print(f">>>{a} {op['symbol']} {b} = {c}")

# C-1.27
# TODO: My solution is to wrap function call with a set. Need to check if
# other solutions exist.
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

# C-1.28
def norm(v, p=2):
    p_sum = sum([ i**p for i in v ])
    print ("Sum:",p_sum)
    p_norm = p_sum ** (1/p)

    return p_norm

if __name__ == '__main__':
    # C-1.21
    print("=========C-1.21============")
    print("Uncomment to test")
    # lines=list()
    # readlines(lines)
    # print(lines[::-1])

    # C-1.22
    print("=========C-1.22============")
    a = [i for i in range(10)]
    b = [i*i for i in range(10)]
    c = dot_product(a,b)
    print("a: ",a)
    print("b: ",b)
    print("c: ",c)

    # C-1.23
    print("=========C-1.23============")
    data=[i for i in range(10)]
    f_append(data,22,21)

    # C-1.24
    print("=========C-1.24============")
    str = "The quick brown dog jumped onto the lazy fox"
    print(str)
    print(f"There are {count_vowels(str)} vowels in the string")

    # C-1.25
    print("=========C-1.25============")
    str = "Let's try, Mike."
    print(str)
    print(f"String without punctuation: {remove_punctuation(str)}")

    # C-1.26
    print("=========C-1.26============")
    a,b,c = 5,3,2
    print(f"Trying {a},{b},{c}")
    get_formula(a,b,c)
    a,b,c = 5,3,7
    print(f"Trying {a},{b},{c}")
    get_formula(a,b,c)
    a,b,c = 5,3,8
    print(f"Trying {a},{b},{c}")
    get_formula(a,b,c)

    # C-1.27
    print("=========C-1.27============")
    print({ i for i in factors(20) })

    # C-1.28
    print("=========C-1.28============")
    a = { 4, 3 }
    print(f"Euclidean norm of {a} is {norm(a)}")
    print(f"p-norm of {a} for p=3 is {norm(a,3)}")
