import pandas as pd
import numpy as np

# question66: how to replace both the diagonals of data frame with 0?
dataset = pd.DataFrame(np.random.randint(1, 100, 100).reshape(10, -1))
print(dataset)
for i in range(len(dataset)):
    for j in range(len(dataset)):
        if i == j:
            dataset.iloc[i, j] = 0
print(dataset)
del dataset

# question67: how to get the particular group of groupby data frame by key?
dataset = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                        'rating': np.random.rand(9),
                        'price': np.random.randint(0, 15, 9)})
df_group = dataset.groupby(['fruit'])
print(df_group.groups["apple"])
del dataset

# question68: how to get the nth largest value of a column when grouped by another column?
dataset = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                        'rating': np.random.rand(9),
                        'price': np.random.randint(0, 15, 9)})
df_group = dataset['rating'].groupby(dataset["fruit"])
print(df_group.get_group('banana'))
print(df_group.get_group('banana').sort_values().iloc[-2])
del dataset

# question69: how to computer grouped mean on pandas data frame and keep the grouped column
# as another column(not index)
dataset = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                        'rating': np.random.rand(9),
                        'price': np.random.randint(0, 15, 9)})
# solution1
print(dataset['price'].groupby(dataset['fruit']).mean())
# solution2
print(dataset.groupby('fruit', as_index=False)['price'].mean())
del dataset

# question70: how to join two data frames by 2 columns so they have only the common rows?
dataset1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                         'weight': ['high', 'medium', 'low'] * 3,
                         'price': np.random.randint(0, 15, 9)})
dataset2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                         'kilo': ['high', 'low'] * 3,
                         'price': np.random.randint(0, 15, 6)})
merge_data = pd.merge(dataset1, dataset2, left_on=["fruit", "weight"], right_on=["pazham", "kilo"],
                      suffixes=["_left", "_right"])
print(merge_data)
