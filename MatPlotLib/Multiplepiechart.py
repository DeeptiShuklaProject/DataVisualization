import matplotlib.pyplot as plt

x=[10,20,30,40]
x1=[40,30,20,10]

y=["c","c++","java","python"]
c=["r","b","y","g"]


plt.pie(x,labels=y,radius=1.5)
plt.pie([1],colors="w")

plt.show()