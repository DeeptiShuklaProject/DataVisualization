import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
number=[2,3,1,4,5,3,6]
colors=["r","y","b","g","r","b","g"]
size=[50,100,500,300,700,400,200]

plt.scatter(day,number,c=colors,s=size,alpha=0.5,marker="*",edgecolor="g",linewidth=2)
plt.title("Scatter Plot",fontsize=15)
plt.xlabel("Day",fontsize=15)
plt.ylabel("Number", fontsize=15)
plt.show()