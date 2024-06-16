import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
number=[2,3,1,4,5,3,6]
plt.scatter(day,number)
plt.title("Scatter Plot", fontsize=15)
plt.xlabel("Day",fontsize=15)
plt.ylabel("Number", fontsize=15)
plt.show()