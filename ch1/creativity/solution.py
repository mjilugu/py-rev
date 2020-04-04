

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

if __name__ == '__main__':
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
