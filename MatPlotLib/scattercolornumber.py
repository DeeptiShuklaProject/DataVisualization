import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
number=[2,3,1,4,5,3,6]
number2=[3,2,4,5,1,6,2]
colors=[10,29,30,30,40,50,56]
size=[50,100,500,300,700,400,200]

plt.scatter(day,number,c=colors,s=size,cmap="viridis")

plt.scatter(day,number2,color="r",s=size)
t=plt.colorbar()
t.set_label("colorBar",fontsize=15)
plt.title("Scatter Plot",fontsize=15)
plt.xlabel("Day",fontsize=15)
plt.ylabel("Number", fontsize=15)
plt.show()