import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.plot(x,y,color="r")

plt.fill_between(x,y,color="g",where=(x>=2) & (x<=4),alpha=0.3)
# plt.fill_between(x=[2,4],y1=2,y2=4)

plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()