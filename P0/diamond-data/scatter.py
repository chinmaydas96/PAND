import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('new-diamonds.csv',delimiter=',')
a = [row[1] for row in data]
carat = a[1:] 
b = [row[7] for row in data]
price = b[1:]

plt.scatter(carat,price)
plt.title('scatter plot between Diamond carat and predicted price')
plt.xlabel('carat')
plt.ylabel('predicted price')
plt.show()
