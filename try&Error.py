import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression

# matrix = np.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])

# df = pd.DataFrame(matrix)

# print(df)

df = pd.read_csv("linear-data.csv")

x = df.iloc[:,[0]].to_numpy()
y = df.iloc[:,[1]].to_numpy()

model = LinearRegression()
model.fit(x, y)
value = 80
print(model.predict([[value]]))