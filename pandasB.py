import pandas as pd
import numpy as np

# question51: how to get the row number of the nth largest value in a column?
dataset = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10, -1), columns=["a", "b", "c"])

arg_sort = dataset["a"].argsort()
dataset_2 = dataset.iloc[arg_sort]
dataset_2.insert(3, "arg_sort", arg_sort)
print(dataset_2)

# question52: how to find the position of the nth largest value greater than a given value?
ser_input = pd.Series(np.random.randint(1, 100, 15))
# sort the series
sorted_ser = ser_input[ser_input.argsort()[::-1]]
count = sorted_ser[sorted_ser > sorted_ser.mean()].index[1]  # it represents the second largest element
print("the index of the second largest element is:", count, "value is:", ser_input[count])

# question53: how to get the last n rows of a data frame with row sum greater than 100?
dataset = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
dataset.insert(4, "sum", dataset.sum(axis=1))
count = dataset[dataset["sum"] > 100].index.to_list()[-2:]
dataset_output = dataset.iloc[count]
print(dataset_output)

# question54: how to find and cap outlier from a series or data frame column?
ser = pd.Series(np.logspace(-2, 2, 30))
quantiles = np.quantile(ser, [0.05, 0.95])
ser.iloc[np.where(ser < quantiles[0])] = quantiles[0]
ser.iloc[np.where(ser > quantiles[1])] = quantiles[1]
print(ser)

# question55: how to reshape a data frame to the largest possible square after removing the negative values?
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10, -1))
array_1 = np.array([df.values]).reshape(-1, 1)
array_2 = array_1[array_1 > 0]
square_num = int(np.floor(np.sqrt(array_2.shape[0])))
arg_sort = np.argsort(array_2)[::-1][0:square_num ** 2]
frame_output = np.take(array_2, arg_sort).reshape(square_num, square_num)
print(frame_output)
