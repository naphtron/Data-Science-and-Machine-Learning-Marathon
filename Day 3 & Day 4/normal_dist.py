# simulating normal distribution
# data science marathon
 
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5,1,1000) # mean = 5, var = 1, data points = 1000
y = numpy.random.normal(10,2,1000) # mean = 10, var = 2, data points = 1000

plt.scatter(x,y)
plt.show()

#I may or may have not been a statistician in a past life ;)