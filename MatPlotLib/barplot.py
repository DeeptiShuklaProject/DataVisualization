import matplotlib.pyplot as plt

x=["python","c","c++","java"]
y=[85,70,60,82]
z=[20,30,40,50]

plt.xlabel("language",fontsize=15)
plt.ylabel("number",fontsize=15)
plt.title("BarPlot",fontsize=15)

c=["y","b","m","g"]
# plt.bar(x,y,width=0.4,color=c,align='center',edgecolor="r",linewidth=5,linestyle=":",alpha=0.5)

plt.bar(x,y,width=0.4,color='r',label="Popularity")
plt.bar(x,z,width=0.4,color='y',label="Popularity1")

plt.legend()
plt.show()