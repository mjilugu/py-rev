from random import randrange

# cf-3.5
def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a==b==c:
                    return False
    return True

# cf-3.6
def disjoint2(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            if a==b:
                for c in C:
                    if a==c:
                        return False
    return True

if __name__ == "__main__":
    A = [ 1,2,3 ]
    B = [ 4,5,6 ]
    C = [ 7,8,9 ]

    print(A)
    print(B)
    print(C)

    print(f"3 way disjoint1? {disjoint1(A,B,C)}")
    print(f"3 way disjoint2? {disjoint2(A,B,C)}")

    A = [ 1,4,3 ]
    B = [ 4,5,6 ]
    C = [ 7,8,4 ]

    print(A)
    print(B)
    print(C)

    print(f"3 way disjoint1? {disjoint1(A,B,C)}")
    print(f"3 way disjoint2? {disjoint2(A,B,C)}")
