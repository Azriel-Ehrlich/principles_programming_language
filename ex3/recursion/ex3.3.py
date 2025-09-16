from tail_recursive import tail_recursive

# find LCM of two numbers recursion without tail
def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)*1
    return abs(a * b) // gcd(a, b)

# find LCM of two numbers recursion with tail
def lcm_tail(a, b, acc=1):
    @tail_recursive
    def gcd(x, y):
        if y == 0:
            return x
        return gcd.tail_call(y, x % y)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def main():
    print ("LCM of 12 and 15 is:", lcm(12, 15))
    print ("LCM of 12 and 15 using tail recursion is:", lcm_tail(12, 15))

if __name__ == "__main__":
    main()