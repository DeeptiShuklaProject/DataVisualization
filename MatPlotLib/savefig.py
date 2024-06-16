import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,3,5,3]

plt.plot(x,y,color="r")
# plt.savefig("line")
# plt.savefig("line1",dpi=2000)
# plt.savefig("line2",dpi=2000,facecolor="g")
# plt.savefig("line3.pdf",dpi=2000,facecolor="g")
# plt.savefig("line4.jpg",dpi=2000,facecolor="g")
plt.savefig("line5.jpg",dpi=2000,facecolor="g",transparent=False,bbox_inches="tight")

plt.show()