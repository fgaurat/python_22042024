# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def main():
    print(50*'-')
    print("fibo",__name__)
    fib(50)
    print(fib2(50))
    print(50*'-')

if __name__ == "__main__":
    main()


