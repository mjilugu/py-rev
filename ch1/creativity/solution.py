import random

# C-1.13
def reverse(data):
    d_length=len(data)

    for i in range(-1, -(d_length//2 + 1), -1):
        print(i, abs(i) - 1)
        data[i],data[ abs(i) - 1 ] = data[ abs(i) - 1 ],data[i]

# C-1.14
def odd_products(data):
    d_length = len(data)
    odd_p = []

    for i in range(0,d_length - 1):
        for j in range(i+1,d_length):
            if data[i]*data[j] % 2 != 0:
                odd_p.append((data[i],data[j]))

    return odd_p

# C-1.15
# This works because the value data[i] points to is replaced
# by the multiple
def is_uniq(data):
    d_length=len(data)
    for i in range(d_length - 1):
        for j in range(i+1,d_length):
            if data[i] == data[j]:
                return False
    return True

# C-1.16
def scale1(data,factor):
    for i in range(len(data)):
        data[i] *= factor

# C-1.17
# This will not work because a value pointed by data[i] is
# copied to new instance pointed by variable val and modified. The original
# item pointed by data[i] is unchanged.
def scale2(data,factor):
    for val in data:
        val *= factor

# C-1.18
# data = [ i * (i+1) for i in range(10)]

# C-1.19
# [chr(i) for i in range(97,123)]

# C-1.20
def shuffle(data):
    new_indicies=set()
    new_data=list()
    d_length=len(data)
    counter=0

    while len(new_indicies) != d_length:
        counter+=1
        i = random.randint(0,d_length - 1)
        if i not in new_indicies:
            new_indicies.add(i)
            new_data.append(data[i])

    for i in range(d_length):
        data[i] = new_data[i]

    print(f"INFO: shuffled in {counter} steps")

if __name__ == '__main__':
    # C-1.13
    print("=========C-1.13============")
    data = [i for i in range(10)]
    print(f"Data before reverse: {data}")
    reverse(data)
    print(f"Data after reverse:  {data}")
    data = [i for i in range(10,60,10)]
    print(f"Data before reverse: {data}")
    reverse(data)
    print(f"Data after reverse:  {data}")

    # C-1.14
    print("=========C-1.14============")
    data = [i for i in range(10)]
    print(f"Odd pairs for data {data} are:")
    print(odd_products(data))

    # C-1.15
    print("=========C-1.15============")
    data = [i for i in range(10)]
    print(f"{data} is distinct array: {is_uniq(data)}")
    data = [2,3,3,5,4]
    print(f"{data} is distinct array: {is_uniq(data)}")
    data = [2,3,0,5,4,3]
    print(f"{data} is distinct array: {is_uniq(data)}")

    # C-1.16,C-1.17
    print("=========C-1.16,C-1.17============")
    data = [i for i in range(10)]
    print(data)
    scale1(data, 5)
    print(f"After scale1: {data}")
    data = [i for i in range(10)]
    print(data)
    scale2(data, 5)
    print(f"After scale2: {data}")

    # C-1.18
    print("=========C-1.18============")
    data = [ i * (i+1) for i in range(10)]
    print(data)

    # C-1.20
    print("=========C-1.20============")
    data = [i for i in range(10)]
    print("Shuffling ", data)
    shuffle(data)
    print("Shuffled  ", data)
