# function that generates the sums of the Taylor series for e^x
def exp_taylor_sums(x: float):
    term = 1.0
    total = 0.0
    k = 0
    while True:
        total += term
        yield total
        k += 1
        term *= x / k


def main():
    try:
        x = float(input("Enter x: ").strip())
        n = int(input("Enter n (non-negative integer): ").strip())
        if n < 0:
            raise ValueError
    except Exception:
        print("Invalid input.")
        return

    gen = exp_taylor_sums(x)
    s_n = None
    for _ in range(n + 1):      
        s_n = next(gen)
        print(s_n)



if __name__ == "__main__":
    main()
