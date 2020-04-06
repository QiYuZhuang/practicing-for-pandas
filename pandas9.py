import pandas as pd
import numpy as np

# question41: how to count the number of missing values in each column?
cars93 = pd.read_csv(r"inputs\cars93.csv", index_col=False)
cars_null = pd.DataFrame(cars93.isnull().sum())
print(cars_null[cars_null[0] > 0][0].argmax())
del cars93

# question42: how to replace missing values of multiple numeric columns with the mean?
cars93 = pd.read_csv(r'inputs\cars93.csv', index_col=False)
cars93[["Luggage.room"]] = cars93[["Luggage.room"]].apply(lambda x: x.fillna(x.mean()))
cars93[["Rear.seat.room"]] = cars93[["Rear.seat.room"]].apply(lambda x: x.fillna(x.mean()))
print(cars93.isnull().sum().sum())
del cars93

# question43: how to use apply function on existing columns with global variables
# as additional arguments?
cars93 = pd.read_csv(r'inputs\cars93.csv', index_col=False)
d = {'Rear.seat.room': np.nanmean, 'Luggage.room': np.nanmedian}  # global variable
cars93[['Rear.seat.room', 'Luggage.room']] \
    = cars93[['Rear.seat.room', 'Luggage.room']].apply(lambda x, d: x.fillna(d[x.name](x)), args=(d,))
print(cars93.isnull().sum().sum())

# question44: how to select a specific column from a data frame as a data frame instead of a series?
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df2 = df["a"].to_frame()
print(type(df2))
df2 = pd.DataFrame(df["a"])
print(type(df2))

# question45: how to change the order of columns of a data frame?
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
# solution1
df2 = df[['c', 'b', 'a', 'd', 'e']]
print(df2)


# solution2
def change_column(data, col1, col2):
    df_columns = df.columns.to_list()
    index1 = df_columns.index(col1)
    index2 = df_columns.index(col2)
    df_columns[index1], df_columns[index2] = col2, col1
    return data[df_columns]


df2 = change_column(df, "a", "b")
print(df2)
