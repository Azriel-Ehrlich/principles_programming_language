from tail_recursive import tail_recursive

# non tail recursive function to check if a number is palindrome
def isPalindrome(n):
    if n < 0:
        return False
    def reverse_num(n):
        if n == 0:
            return 0
        return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_num(n // 10)
    return n == reverse_num(n)

# tail recursive function to check if a number is palindrome
def isPalindromeTail(n, acc=None):
    if n < 0:
        return False
    @tail_recursive
    def reverse_num(n,acc=0):
        if n == 0:
            return acc
        return reverse_num.tail_call(n // 10, acc * 10 + n % 10)
    return n == reverse_num(n)

# usage 
print(isPalindrome(1234321))  # True
print(isPalindromeTail(1234321)) # True
print(isPalindrome(123456))  # False
print(isPalindromeTail(123456)) # False