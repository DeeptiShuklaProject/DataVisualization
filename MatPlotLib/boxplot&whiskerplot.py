import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70]
x1=[10,20,40,50,30,60,90]

y=[x,x1]

# plt.boxplot(x,notch=True)
# plt.boxplot(x,vert=False)
# plt.boxplot(x,label=["python"],patch_artist=True,showmeans=True)
# plt.boxplot(x,label=["python"],patch_artist=True,showmeans=True,whis=2)
# plt.boxplot(x,label=["python"],showmeans=True,sym="g+",boxprops=dict(color="r"),capprops=dict(color="r"),whiskerprops=dict(color="r"),flierprops=dict(markeredgecolor="y"))
plt.boxplot(y,labels=["python","c++"],showmeans=True,sym="g+",boxprops=dict(color="r"),capprops=dict(color="r"),whiskerprops=dict(color="r"))

plt.show()