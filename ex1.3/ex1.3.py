def fib2(n, cache = {}):
    if n == 0 or n == 1:
        return n
    if n in cache.keys():
        return cache[n]
    else:
        cache[n] = fib2(n-1, cache) + fib2(n-2, cache)
        return cache[n]
    
def main():
    cache = {}
    list_of_fib2 = [fib2(i, cache) for i in range(1,36)]
    print(list_of_fib2)
    
if __name__ == "__main__":
    main()