import matplotlib.pyplot as plt
import numpy as np

x=["python","c","c++","java"]
y=[85,70,60,82]
z=[20,30,40,50]

width=0.2
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("language",fontsize=15)
plt.ylabel("number",fontsize=15)
plt.title("BarPlot",fontsize=15)


plt.bar(p,y,width,color='r',label="Popularity")
plt.bar(p1,z,width,color='y',label="Popularity")

plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()