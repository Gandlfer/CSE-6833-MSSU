from sort import *
import random as rand
import timeit
import matplotlib.pyplot as plt

length = 10
y1 = list()
y2 = list()
x = list()
while length <= 150:
    x.append(length)
    arr = [rand.randint(0, 5000) for x in range(length)]
    mergeSortList = arr.copy()
    selectionSortList = arr.copy()
    mergeSortResult = timeit.Timer(lambda: mergeSort(mergeSortList)).timeit(1)
    selectionSortResult = timeit.Timer(
        lambda: selectionSort(selectionSortList, length)
    ).timeit(1)
    y1.append(mergeSortResult)
    y2.append(selectionSortResult)
    length = length + 11

# Plotting Graph
plt.plot(x, y1, label="Merge Sort")
plt.plot(x, y2, label="Selection Sort")
plt.xlabel("Length of number")
plt.ylabel("Execution Time")
plt.legend()
plt.show()
