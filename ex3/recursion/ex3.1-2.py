from tail_recursive import tail_recursive
# ----------------- ex 1 -----------------
# make tuple of n, n-1, ..., 1 with regular recursion
def make_tuple(n):
    if n <=0:
        return ()
    return (n,) + make_tuple(n-1)

# make tuple of n, n-1, ..., 1 with tail recursion
@tail_recursive
def make_tuple_tail(n, acc=()):
    if n <=0:
        return acc
    return make_tuple_tail.tail_call(n-1, acc + (n,))

# usage 
# print(make_tuple(10000)) # should hit recursion limit and crash
# print(make_tuple_tail(10000)) # should work fine
# ---------------- ex 2 -----------------
# recursive function to sum elements of a list 
def sum_elements(seq):
    if not seq:
        return 0
    return seq[0] + sum_elements(seq[1:])

# tail recursive function to sum elements of a list
@tail_recursive
def sum_elements_tail(seq, acc=0):
    if not seq:
        return acc
    return sum_elements_tail.tail_call(seq[1:], acc + seq[0])

#run on the list of first 10000 integers from ex 1 without tail
print(sum_elements(make_tuple_tail(1000)))  # should hit recursion limit and crash
#run on the list of first 10000 integers from ex 1 with tail
print(sum_elements_tail(make_tuple_tail(10000)))
