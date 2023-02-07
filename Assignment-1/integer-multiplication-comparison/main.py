from multiplication import *
import random as rand
import timeit
import matplotlib.pyplot as plt

power = 1
y1 = list()
y2 = list()
x = list()

while power <= 100:
    x.append(power)
    num = lambda: rand.randint(pow(10, power - 1), pow(10, power) - 1)
    karatsuba = timeit.Timer(lambda: karatsubaMultiplication(num(), num())).timeit(1)
    gradeSchool = timeit.Timer(lambda: gradeSchoolMultiplication(num(), num())).timeit(
        1
    )
    y1.append(karatsuba)
    y2.append(gradeSchool)
    power = power + 1

# Plotting Graph
plt.plot(x, y1, label="Karatsuba")
plt.plot(x, y2, label="Grade School")
plt.xlabel("Length of number")
plt.ylabel("Execution Time")
plt.legend()
plt.show()
