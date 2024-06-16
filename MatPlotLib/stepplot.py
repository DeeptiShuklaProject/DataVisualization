import matplotlib.pyplot as plt
x=[1,2,3,4,5]
# y=[1,2,3,4,5]
y=[2,2,3,5,4]

plt.step(x,y,color="r",marker="o",ms=10,mfc="g",label="python")
plt.title("python")
plt.xlabel(" x - axis ")
plt.ylabel(" y - axis ")
plt.legend(loc=2)

plt.grid()


plt.show()