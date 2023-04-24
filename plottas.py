#create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(loc=5, scale=2, size=1000)
plt.hist(data,edgecolor='white')
#now we will create a plot of the function  h(x)=x3 in the range [0, 10],
xpoint=np.random.normal(range(0,10))
ypoint= xpoint ** 3
plt.title("My Chart") 
plt.plot(xpoint,ypoint,color='red', label='plotfunction')
plt.legend()
plt.show()