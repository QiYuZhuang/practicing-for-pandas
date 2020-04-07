import pandas as pd
import numpy as np

# question56: how to swap two rows of a data frame?
# solution1
dataset = pd.DataFrame(np.arange(25).reshape(5, -1))
temp_row = dataset.iloc[1].copy(deep=True)
dataset.iloc[1], dataset.iloc[2] = dataset.iloc[2], temp_row
print(dataset)
# solution2
dataset = pd.DataFrame(np.arange(25).reshape(5, -1))
dataset_2 = dataset.iloc[[0, 2, 1, 3, 4]]
dataset_2.index = np.arange(5)
print(dataset_2)

# question57: how to reverse teh rows of a data frame?
dataset = pd.DataFrame(np.arange(25).reshape(5, -1))
dataset_2 = dataset.iloc[dataset.index.to_list()[::-1]]
print(dataset_2)
# if we need to reset the index with original sequence
dataset_2.index = np.arange(5)
print(dataset_2)

# question58: how to create one-hot encodings of a categorical variable(dummy variables)?
dataset = pd.DataFrame(np.arange(25).reshape(5, -1), columns=list('abcde'))
dummies = pd.get_dummies(dataset["a"])
dataset_2 = pd.concat([dummies, dataset], axis=1)
print(dataset_2)

# question59: which column contains the highest number of row-wise maximum values?
dataset = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1))
dataset_2 = pd.concat([dataset, dataset.apply(np.argmax, axis=1).rename("arg_max")], axis=1)
print(dataset_2)

# question60: how to create a new column that contains the row number of nearest column by euclidean distance?
dataset = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1),
                       columns=list('pqrs'), index=list('abcdefghij'))

corr_list = []
index_list = []

# temporary variable
max_corr = 0
current_index = ""
for i in range(len(dataset)):
    for j in range(len(dataset)):
        if i == j:
            pass
        else:
            current = sum((dataset.iloc[i] - dataset.iloc[j]) ** 2) ** .5
            if current >= max_corr:
                max_corr = current
                current_index = list(dataset.index)[j]
    corr_list.append(max_corr)
    index_list.append(current_index)

    max_corr = 0
    current_index = ""

dataset.insert(4, "nearest_row", corr_list)
dataset.insert(5, "distance", index_list)
print(dataset)
