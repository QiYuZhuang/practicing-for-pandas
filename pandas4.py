import numpy as np
import pandas as pd

# question16: how to get the positiona of items of series A in another series B?
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
# gets the index, but it sorts the index(not recommend)
list_output = list(ser1[ser1.isin(ser2)].index)
print(list_output)
# via numpy where, np.where returns a tuple, we need the first element in every tuple,  so it comes the first [0]
list_output = [np.where(i == ser1)[0].tolist()[0] for i in ser2]
print(list_output)
# via pandas Index and get_loc()
list_output = [pd.Index(ser1).get_loc(i) for i in ser2]
print(list_output)

# question17: how to compute the mean squared error on a truth and predicted series? (useful !!!)
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
# using numpy
result = np.mean((truth - pred) ** 2)
print(result)
# using sklearn metrics(convention but you learn nothing)
from sklearn.metrics import mean_squared_error
result = mean_squared_error(truth, pred)
print(result)

# question18: how to convert the first character of each element in a series to uppercase?
ser = pd.Series(['just', 'a', 'random', 'list'])
# using python string title
output = pd.Series([i.title() for i in ser])
print(output)
# via lambda
output = ser.map(lambda x: x.title())
print(output)
# other solution
output = ser.map(lambda x: x[0].upper() + x[1:])
print(output)

# question19: how to calculate the number of characters in each word in series?
ser = pd.Series(['just', 'a', 'random', 'list'])
# using list function
output = pd.Series([len(i) for i in ser])
print(output)
# using series map
output = ser.map(len)
print(output)
# using series apply
output = ser.apply(len)
print(output)

# question20: how to compute difference of differences between consecutive numbers of a series?
ser = pd.Series([1, 3, 6, 10, 13, 15, 20])
output = ser.diff(periods=1)
print(output)
output = ser.diff(periods=2)
print(output)
output = ser.diff(periods=1).diff(periods=1)
print(output)
