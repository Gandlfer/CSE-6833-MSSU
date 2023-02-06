from sort import *
import random as rand
import timeit
import matplotlib.pyplot as plt

length = 10
y1 = list()
y2 = list()
x = list()
while length <= 3000:
    x.append(length)
    arr = [rand.randint(0, 5000) for x in range(length)]
    # print(arr)
    mergeSortList = arr.copy()
    selectionSortList = arr.copy()
    mergeSortResult = timeit.Timer(lambda: mergeSort(mergeSortList)).timeit(1)
    selectionSortResult = timeit.Timer(
        lambda: selectionSort(selectionSortList, length)
    ).timeit(1)
    y1.append(mergeSortResult)
    y2.append(selectionSortResult)
    length = length + 10

# print(y1)
# print(y2)
plt.plot(x, y1, label="line 1")
plt.plot(x, y2, label="line 2")
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
