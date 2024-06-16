import matplotlib.pyplot as plt
import numpy as np
import random
x=np.random.randint(10,60,(50))
# print(x)


no=[30,26,10,45,51,56,39,23,25,17,13,39,59,34,48,17,55,55,32,51,59,14,22,56,30,53,30,44,49,12,50,15,29,27,30,12,50,53,56,45,16,52,38,46,20,55,43,47,19,13]
l=[10,20,30,40,50,60]

# plt.hist(no,color="b",bins=l,edgecolor="r")
# plt.hist(no,color="b",edgecolor="r",cumulative=-1)
# plt.hist(no,color="b",edgecolor="r",bottom=10)
# plt.hist(no,color="b",edgecolor="r",align="mid")
# plt.hist(no,color="b",bins=l,edgecolor="r",histtype="step")
# plt.hist(no,color="b",bins=l,edgecolor="r",orientation="horizontal")
# plt.hist(no,color="b",bins=l,edgecolor="r",rwidth=0.8)
# plt.hist(no,color="b",bins=l,edgecolor="r",log=True)
plt.hist(no,color="b",bins=l,edgecolor="r",label="python")


plt.title("HistoGram Graph")
plt.xlabel("python")
plt.ylabel("no")
plt.axvline(45,color="g",label="line")

plt.legend()
plt.grid()

plt.show()
