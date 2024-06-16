import matplotlib.pyplot as plt

x=["python","c","c++","java"]
y=[85,70,60,82]
z=[20,30,40,50]

plt.xlabel("language",fontsize=15)
plt.ylabel("number",fontsize=15)
plt.title("BarPlot",fontsize=15)

plt.barh(x,y,color='r',label="Popularity")
plt.barh(x,z,color='y',label="Popularity1")

plt.legend()
plt.show()