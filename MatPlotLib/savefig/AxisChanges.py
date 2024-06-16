import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[3,1,5,2,4]

plt.plot(x,y)

# plt.xticks(x,labels=["python","c","c++","java"])
# plt.yticks(x)

# plt.xlim(0,10)
# plt.ylim(0,10)

plt.axis([0,10,0,7])

plt.show()