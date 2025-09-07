# Azriel Ehrlich 213662539
# principles of programming languages - ex1.1
# --------------------- part a --------------------------
def get_penta_num(n):
    """Return the n-th pentagonal number."""
    return n * (3 * n - 1) // 2

# --------------------- part b --------------------------
def pentaNumRange (n1,n2):
    """Return list of all of the pentagonial numbers between n1 and n2"""
    return list(map(get_penta_num, range(n1, n2)))

# example 
print(pentaNumRange(1, 11))

