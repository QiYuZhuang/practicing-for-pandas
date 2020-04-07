import pandas as pd
import numpy as np

# question61: how to know the maximum possible correlation value of each column against other columns?
dataset = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1),
                       columns=list('pqrstuvwxy'), index=list('abcdefgh'))
data_corr = np.abs(dataset.corr())  # return a matrix
max_corr = data_corr.apply(lambda x: sorted(x)[-2], axis=1)
print(max_corr)
del dataset

# question62: how to create a column containing the minimum by maximum of each row?
dataset = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
dataset.insert(10, "min_by_max", dataset.apply(min, axis=1) / dataset.apply(max, axis=1))
print(dataset)
del dataset

# question63: how to create a column that contains the penultimate value in each row?
# solution1
dataset = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
dataset.insert(10, "penultimate", dataset.apply(lambda x: sorted(x)[-2], axis=1))
print(dataset)
dataset.drop("penultimate", inplace=True, axis=1)
# solution2
dataset.insert(10, "penultimate", dataset.apply(lambda x: np.partition(x, -2)[-2], axis=1))
print(dataset)
del dataset

# question64: how to normalize all columns in a data frame?
dataset = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
dataset_2 = dataset.apply(lambda x: ((x - np.mean(x)) / np.std(x)), axis=0)
print(dataset_2)
del dataset
del dataset_2

# question65: how to compute the correlation of each row with the succeeding row?
dataset = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
corr = []
for i in range(len(dataset) - 1):
    temp1 = dataset.iloc[i, :-1].astype('float64')
    temp2 = dataset.iloc[i + 1, :-1].astype('float64')
    current_corr = temp1.corr(temp2)
    corr.append(current_corr)
corr.append(0)
dataset.insert(10, "corr", corr)
print(dataset)
