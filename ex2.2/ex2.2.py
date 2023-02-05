import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    with open('ex2.json', 'r') as file:
        content = json.load(file)
    
    times = []
    for i in range(len(content) - 1):
        time = timeit.timeit(lambda: func1(content[i], 0, len(content[i])-1), number = 1)
        times.append(time)
    
    plt.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],times)
    plt.xlabel('N items')
    plt.ylabel('Time(s)')
    plt.show()

if __name__ == "__main__":
    main()