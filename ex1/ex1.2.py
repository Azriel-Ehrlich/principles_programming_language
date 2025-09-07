# Azriel Ehrlich 213662539
# principles of programming languages - ex1.2

def sum_digit(n):
    """Return the sum of the digits of n."""
    try:
        n = int(n)
    except (ValueError, TypeError):
        return "invalid input"
    # Handle negative numbers by taking absolute value
    return sum(map(int, str(abs(n))))

def main():
   s = input("enter number: ")
   print(sum_digit(s))

if __name__ == "__main__":
   main()
