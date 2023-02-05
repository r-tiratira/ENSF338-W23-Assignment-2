def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def fib2(n, cache = {}):
    if n == 0 or n == 1:
        return n
    if n in cache.keys():
        return cache[n]
    else:
        cache[n] = fib2(n-1, cache) + fib2(n-2, cache)
        return cache[n]
    
def main():
    import timeit
    import matplotlib.pyplot as plt

    fib_list = []
    fib2_list = []
    for i in range(36):
        fib_time = timeit.timeit(lambda: fib(i), number = 1)
        fib2_time = timeit.timeit(lambda: fib2(i), number = 1)
        fib_list.append(fib_time)
        fib2_list.append(fib2_time)

    x = [i for i in range(36)]
    plt.plot(x, fib_list, label = 'Unoptimized')
    plt.plot(x, fib2_list, label = 'Memoization')
    plt.xlabel('nth index')
    plt.ylabel('Time(s)')
    plt.legend()
    plt.show()

    plt.plot(x, fib_list, label = 'Unoptimized')
    plt.xlabel('nth index')
    plt.ylabel('Time(s)')
    plt.legend()
    plt.show()

    plt.plot(x, fib2_list, label = 'Memoization')
    plt.xlabel('nth index')
    plt.ylabel('Time(s)')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()