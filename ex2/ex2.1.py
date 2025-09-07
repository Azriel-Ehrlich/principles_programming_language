from functools import reduce
import time

lin = lambda x: x/2 + 2

# ----------------- part 1 -----------------
l = list(range(0,10001))

# list of modified values 
modified = list(map(lin,l))

# ----------------- part 2 -----------------
# sum the modified values in high order way
result = reduce(lambda x,y: x+y, modified)

# ----------------- part 3 -----------------
# compare times with imperative way
def imperative_sum(l):
    ''' sum the values in a list in an imperative way '''
    total = 0
    for x in l:
        total += x
    return total

# measure time for the imperative way
start1 = time.perf_counter()
sum1 = imperative_sum(modified)
end1 = time.perf_counter()

# measure time for the high order way
start2 = time.perf_counter()
sum2 = reduce(lambda x,y: x+y, modified)
end2 = time.perf_counter()

# print the results
print(f"Imperative sum: {sum1}, Time: {end1 - start1}")
print(f"High order sum: {sum2}, Time: {end2 - start2}")

# ----------------- part 4 -----------------
# do everything in one high order function 
result_all = reduce(lambda x,y: x+y, map(lin, l))
