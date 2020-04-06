import pandas as pd
import numpy as np

# question46: how to set the number of rows and columns displayed in the output?
cars93 = pd.read_csv(r"inputs\cars93.csv", index_col=False)
pd.set_option("display.max_columns", 10)
pd.set_option("display.max_rows", 10)
print(cars93)

# question47: how to format or suppress scientific notations in a pandas data frame?
df = pd.DataFrame(np.random.random(5) ** 10, columns=["random"])
# solution1
df2 = df.round(4)
print(df2)
pd.reset_option('^display.', silent=True)
# solution2
pd.set_option('display.float_format', lambda x: '%.4f' % x)
print(df)
pd.reset_option('^display.', silent=True)
# solution3
df2 = df.apply(lambda x: '%.4f' % x, axis=1).to_frame()
print(df2)
pd.reset_option('^display.', silent=True)

# question48: how to format all the  values in a data frame as percentages?
df = pd.DataFrame(np.random.random(4), columns=["random"])
pd.options.display.float_format = '{:,.2f}%'.format
df2 = df * 100
print(df2)
pd.reset_option('^display.', silent=True)

# question49: how to filter every nth row in a data frame?
cars93 = pd.read_csv(r"inputs\cars93.csv", index_col=False, usecols=["Manufacturer", "Model", "Type"])
cars_out = cars93[::20]
print(cars_out)
del cars93

# question50: how to create a primary key index by combining relevant columns?
cars93 = pd.read_csv(r"inputs\cars93.csv", index_col=False, usecols=["Manufacturer", "Model", "Type", "Min.Price"])
cars93["new_index"] = cars93["Manufacturer"] + cars93["Model"] + cars93["Type"]
print(cars93)
print(cars93["new_index"])
cars93.set_index("new_index", inplace=True)
print(cars93)
