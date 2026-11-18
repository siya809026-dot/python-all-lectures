import pandas as pd

s = pd.Series([1,2,3,4,5,6,7],index=['k','i','y','a','s','i','n'])
print(s)

dh = pd.DataFrame({"names":["harry","rohan","subham"],"marks":[100,45,78]})
print(dh)

df = pd.read_csv("iris.csv")
print(df)
# print(df.head)
# print(df.tail)
# print(df.describe)
# print(df.info)
print(df.columns)
# print(df["ID"])
# print(type(df["sepal_length"].astype(str)))
