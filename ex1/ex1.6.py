# ------------------- part a -------------------------------
def times2(x):
    """ return double the input """
    return 2 * x

def square(x):
    """ return the square of the input """
    return x * x

def reciprocal(x):
    """ return the reciprocal of the input """
    return None if x == 0 else 1 / x

FUNCS = [times2, square, reciprocal]

# -------------------- part b --------------------------
def apply_funcs(nums,funcs):
    """ return a dictionary where the key is the name of the function
        and the value is the list of results of applying the function
        to each number in nums"""
    # create a list of (function_name, results) pairs, filtering out None values
    pairs = map(lambda f: (f.__name__, list(filter(lambda x: x is not None, map(f, nums)))), funcs)
    return dict(pairs)

# example
result = apply_funcs([1, 2, 0], FUNCS)
print(result)