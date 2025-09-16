from functools import reduce

# ------------- part a -----------
# Build list 1..1000 and split to evens/odds using filter
nums = list(range(1, 1001))
evens = list(filter(lambda x: x % 2 == 0, nums))
odds  = list(filter(lambda x: x % 2 == 1, nums))
# lambda for list of cummulative product for list
cum_prod = lambda ls,size: list(map(
    lambda x: reduce (lambda a, b: a * b, ls[:x+1]), range(size)
    ))

# lambda for list of x/2+2+next element for list where x is
# the sum until the current element
transform_sum = lambda ls: list(map(
    lambda x: x/2 + 2 + (ls[x+1] if x+1 < len(ls) else 0), range(len(ls))
    ))

# ------------- part b -----------
# for the even list compute the cummulative product of part of it
even_cumprod = cum_prod(evens,30)
# for the odd list compute the transform_sum of part of it
odd_transformed = transform_sum(odds[:10])

print(f"Even cummulative product: {even_cumprod}")
print(f"Odd transformed: {odd_transformed}")

# ------------- part c -----------
# sum every list and print the results
sum_evens = reduce(lambda x, y: x + y, even_cumprod)
sum_odds  = reduce(lambda x, y: x + y, odd_transformed)

print(f"Sum of even cummulative product: {sum_evens}")
print(f"Sum of odd transformed: {sum_odds}")