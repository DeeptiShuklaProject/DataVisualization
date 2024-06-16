import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,3,5,6,4,3]

# plt.stem(x,y,linefmt=":",markerfmt="r+")
# plt.stem(x,y,markerfmt="ro",bottom=9)
plt.stem(x,y,linefmt=":",markerfmt="ro",bottom=0,basefmt="g",label="python")

plt.legend()

plt.show()