import pandas as pd
import numpy as np

# question71: how to remove rows from a data frame that are present in another data frame?
dataset1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                         'weight': ['high', 'medium', 'low'] * 3,
                         'price': np.random.randint(0, 15, 9)})
dataset2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                         'kilo': ['high', 'low'] * 3,
                         'price': np.random.randint(0, 15, 6)})
columns_1 = pd.Series(dataset1.columns.to_list())
columns_2 = pd.Series(dataset2.columns.to_list())
unit = list(np.intersect1d(columns_1, columns_2))
dataset1.drop(unit, axis=1, inplace=True)
dataset2.drop(unit, axis=1, inplace=True)
print(dataset1)
print(dataset2)
del dataset1
del dataset2

# question72: how to get the positions where values of two columns match?
dataset = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                        'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})
print(dataset)
print(np.where(dataset["fruit1"] == dataset["fruit2"])[0])
del dataset

# question73: how to create lags and leads of a columns in a data frame?
dataset = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns=list('abcd'))
dataset.insert(len(dataset.columns), "lag1", dataset['a'].shift(1))
dataset.insert(len(dataset.columns), "lag2", dataset['b'].shift(-1))
print(dataset)
del dataset

# question74: how to get the frequency of unique values in the entire data frame?
dataset = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns=list('abcd'))
print(pd.value_counts(dataset.values.ravel()))
del dataset

# question75: how to split a text column into two separate columns?
dataset = pd.DataFrame(["STD, City State", "33, Kolkata West Bengal",
                        "44, Chennai Tamil Nadu", "40, Hyderabad Telengana",
                        "80, Bangalore Karnataka"], columns=['row'])
new = dataset['row'].apply(lambda x: " ".join(x.split(',')).split(None, 2, ))
new_head = new[0]
values =new[1:]
new_dataset = pd.DataFrame(values.array, columns=new_head)
print(new_dataset)
