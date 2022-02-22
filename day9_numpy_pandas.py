"""
Numpy
Pandas
"""
# imports
import numpy as np
import pandas as pd

#
df1 = pd.DataFrame(
    np.random.rand(4, 6),
    index=["index1", "index2", "index3", "index4"],
    columns=list("ABCDEF"),
)
# print()
print(df1)
#
print(df1.describe())  # it needs parenthesis to give stats!
print()
#
# access sort_values
# with loc
# print(df1.loc["Test1", "C"])
# with iloc
# print(df1.iloc[0][1])
# # asign values
# df1.loc["Test1", "C"] = "Hello"
# # with iloc too
# # print(df1.A[])
# print(df1.C["Test1"])
#
#
df_2 = df1.sort_values("A")
print("sort by A", df_2)
print()
df_3 = df1.sort_values("B")
print("sort by B", df_3)
print()
#
# Iterate over columns
# method1 iteritems
for (columnName, columnData) in df1.iteritems():
    print("Column Name : ", columnName)
    print("Column Contents : ", columnData.values)
print()
# method2
# Select column contents by column
# name using [] operator
for column in df1:
    columnSeriesObj = df1[column]
    print("Column Name : ", column)
    print("Column Contents : ", columnSeriesObj.values)
