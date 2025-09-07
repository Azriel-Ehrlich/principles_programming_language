from functools import reduce


# ------------------- part a ---------------------------
def power_function(exp):
    """returns a function f(x) = x**exp"""
    return lambda x: x ** exp

# ------------------- part b ---------------------------
def make_power_funcs(n: int):
    """returns a map object of functions f(x) = x**i for i in 0..n-1"""
    return map(power_function, range(n))

# # --- main script ---
# if __name__ == "__main__":
#     n = int(input("Enter number of powers:"))
#     result = make_power_funcs(n)
#     base = int(input("Enter base:"))
#     print(type(result))
#     # apply each function to 'base' using map 
#     output = tuple(map(lambda f: f(base), result))
#     print(output)

# ------------------- part c ---------------------------
# Taylor approximation of e^x up to degree n
def taylor_exp(x, n):
    """returns the Taylor series approximation of e^x up to degree n"""
    # generate power functions for degrees 0 to n-1
    power_funcs = make_power_funcs(n)
    
    # calculate factorials for degrees 0 to n-1
    factorials = list(map(lambda i: reduce(lambda a, b: a * b, range(1, i + 1), 1), range(n)))
    
    # calculate each term x^i / i! and sum them up
    terms = map(lambda f, fact: f(x) / fact, power_funcs, factorials)
    
    return reduce(lambda a, b: a + b, terms)
# Example usage
approx = taylor_exp(1, 10) 
print(f"Taylor approximation of e^1 up to degree 10: {approx}")