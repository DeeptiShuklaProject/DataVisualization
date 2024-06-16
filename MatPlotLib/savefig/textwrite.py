import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[3,1,5,2,6]

plt.plot(x,y)
plt.title("Visualization",fontsize=15)
plt.xlabel("Days",fontsize=15)
plt.ylabel("Python",fontsize=15)

plt.text(2,5,"Matplotlib",fontsize=15,style="italic",bbox={"facecolor":"red"})
plt.annotate("python",xy=(3,2),xytext=(4,4),arrowprops=dict(facecolor="black",shrink=100))

plt.legend(["up"],loc=9,facecolor="Red",edgecolor="yellow",framealpha=0.5,shadow=True)
plt.show()