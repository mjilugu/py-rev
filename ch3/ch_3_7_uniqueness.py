from random import randrange

# cf-3.7
def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    n = len(S)
    for i in range(n):
        for j in range(i+1,n):
            if S[i] == S[j]:
                return False
    return True

# cf-3.8
def unique2(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S)
    for i in range(1, len(temp)):
        if S[i - 1] == S[i]:
            return False
    return True

if __name__ == "__main__":
    A = [ 1,2,3 ]
    B = [ 4,5,5 ]

    print(A)
    print(f"is unique1? {unique1(A)}")
    print(f"is unique2? {unique2(A)}")
    print(B)
    print(f"is unique1? {unique1(B)}")
    print(f"is unique2? {unique2(B)}")
