
# cf-3.2
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ...,S[j]."""
    n = len(S)
    A = [0]*n

    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

# cf-3.3
def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ...,S[j]."""
    n = len(S)
    A = [0]*n

    for i in range(n):
        A[i] = sum(S[0:i+1]) / (i+1)
    return A

# cf-3.4
def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0],....,S[j]"""
    n = len(S)
    A = [0]*n
    total = 0
    for i  in range(n):
        total += S[i]
        A[i] = total / (i+1)
    return A


if __name__ == "__main__":
    data = [i for i in range(10)]
    print(data)
    print(f"prefix_average1:")
    print(prefix_average1(data))
    print(f"prefix_average2:")
    print(prefix_average2(data))
    print(f"prefix_average3:")
    print(prefix_average3(data))
