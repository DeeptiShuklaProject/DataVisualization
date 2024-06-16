import matplotlib.pyplot as plt

x=[10,20,30,40]
y=["c","c++","java","python"]
ex=[0.4,0.0,0.0,0.0]
# c=["r","b","g","y"]
# plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.2f%%")
plt.pie(x,labels=y,explode=ex,autopct="%0.1f%%",shadow=True,radius=1.3,labeldistance=1.1,startangle=0,textprops={"fontsize":15},counterclock=False,wedgeprops={"linewidth":5,"edgecolor":"m"})
plt.title("PiePlot")
plt.legend(loc=2)
plt.show()