import pandas as pd
import numpy as np

# question36: how to import only specified columns from a csv?
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataset = pd.read_csv(r'inputs\housing.csv', delimiter=r'\s+', names=column_names)
dataset.to_csv(r"inputs\housing_preprocessed.csv")
del dataset
dataset = pd.read_csv(r"inputs\housing_preprocessed.csv", usecols=["CRIM", "ZN", "CHAS"], index_col=False)
print(dataset.head())

# question37: how to get the nrows, ncolumns, datatype, summary, stats of each column
# of a data frame? Also get the array and list equivalent
del dataset
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataset = pd.read_csv(r'inputs\housing.csv', delimiter=r'\s+', names=column_names)
print(dataset.info())
print(dataset.describe())
print(dataset.dtypes.value_counts())

# question38: how to extract the row and column number of a particular cell with given criterion?
del dataset
dataset = pd.read_csv(r'inputs\housing.csv', delimiter=r'\s+', names=column_names)
max_tax = dataset["TAX"].max()
print("max_tax:", max_tax)
# find the cell whose tax is the max
# solution1
max_tax_cell = dataset[dataset["TAX"] == max_tax]
print(max_tax_cell)
# solution2
max_tax_cell = dataset.loc[dataset["TAX"] == max_tax, ["CRIM", "ZN", "TAX"]]
print(max_tax_cell)

# question39: how to rename a specific columns in a data frame
cars93 = pd.read_csv(r'inputs\cars93.csv', index_col=False)
print(cars93.head())
cols = cars93.columns
cols = list(map(lambda x: x.replace(".", "_"), cols))
cols[cols.index("Type")] = "CarType"
cars93.columns = cols
print(cars93.head())
del cars93

# question40: how to check if a data frame has any missing values?
cars93 = pd.read_csv(r"inputs\cars93.csv", index_col=False)
print(cars93.isnull().sum())
