import time
import sys
# -------------------------- part a --------------------------

# function that generates a list that contains the numbers 1 -1000
def generate_numbers(n =1000):
    numbers = [i for i in range(1, n+1)]
    return numbers

# function that generates a list that contains the squares of the numbers 1 -1000
# with lazy evaluation
def generate_numbers_lazy(n =1000):
    numbers = (i for i in range(1, n+1))
    return numbers

#mesuring the exectution time and memory size of the two functions
def measure_performance():
    # Measure the non-lazy function
    start_time = time.perf_counter()
    numbers = generate_numbers()
    end_time = time.perf_counter()
    print(f"Execution time (generate_numbers): {end_time - start_time:.6f} seconds")
    print(f"Object size (generate_numbers): {sys.getsizeof(numbers)} bytes")

    # Measure the lazy function
    start_time = time.perf_counter()
    numbers_lazy = generate_numbers_lazy()
    end_time = time.perf_counter()
    print(f"Execution time (generate_numbers_lazy): {end_time - start_time:.6f} seconds")
    print(f"Object size (generate_numbers_lazy): {sys.getsizeof(numbers_lazy)} bytes")

    # -------------------------- part b --------------------------

# function that gets a list of numbers and returns a list of the n first elements
def first_n(numbers, n=5000):
    return numbers[:n]
# function that gets a generator of numbers and returns a generator of the n first elements
def first_n_generator(numbers, n=5000):
    return (next(numbers) for _ in range(n))

def measure_first_n():
    numbers = generate_numbers(10000)
    numbers_lazy = generate_numbers_lazy(10000)

    # Measure the non-lazy function
    first_numbers = first_n(numbers, 5000)
    print("the types of the lists are " + ("the same" if type(first_numbers) == type(numbers) else "different"))
    # Measure the lazy function
    first_numbers_lazy = first_n_generator(numbers_lazy, 5000)
    print("the types of the generators are " + ("the same" if type(first_numbers_lazy) == type(numbers_lazy) else "different"))
if __name__ == "__main__":
    measure_performance()
    measure_first_n()