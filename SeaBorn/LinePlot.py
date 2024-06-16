import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

y_1=sns.load_dataset("penguins")
var = [1,2,3,4,5,6,7]
var_1 = [2,3,4,3,5,6,7]

x_1= pd.DataFrame({"var":var, "var_1":var_1})

sns.lineplot(x="var",y="var_1",data=x_1)


plt.show()
