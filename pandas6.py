import pandas as pd
import numpy as np

# question26: how to get the mean of a series grouped by another series?
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
# use one list to calculate a kpi from another(a little hard to comprehend)
print(weights.groupby(fruit).mean())
# use pandas groupby
cor = pd.concat([fruit, weights], axis=1)
print(cor.groupby(0).mean())

# question27: how to computer the euclidean distance between two series?
# euclidean distance is equal to 2-norm
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# using series one to one operation
result = sum((p - q) ** 2) ** 0.5
print(result)
# using numpy linalg(a function for calculating norm, argument ord default by 2)
result = np.linalg.norm(p - q, ord=2)
print(result)

# question28: how to find all the local maxima(or peaks) in a numeric series?
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
# using pandas shift
local_max = ser[(ser.shift(1) < ser) & (ser.shift(-1) < ser)]
print(local_max)
# using numpy
dd = np.diff(np.sign(np.diff(ser)))
local_max = np.where(dd == -2)[0] + 1
print(local_max)

# question29: how to replace missing spaces in a string with the least frequent character?
input_str = 'i have an apple'
# using pandas
ser = pd.Series(list(input_str.replace(" ", "")))
minimum = list(ser.value_counts().index)[-1]
out_str = input_str.replace(" ", minimum)
print(out_str)
# using Counter
from collections import Counter
copy = input_str
Counter_ = Counter(list(copy.replace(" ", "")))
minimum = min(Counter_, key=Counter_.get)
out_str = input_str.replace(" ", minimum)
print(out_str)

# question30: how to create a TimeSeries starting '2000-01-01'and 10 weekends(saturdays) after that
# having random numbers as values
random_number = pd.Series(np.random.randint(1, 10, 10))
date = pd.Series(pd.date_range('2000-01-01', periods=10, freq='W-SAT'))
output_ser = pd.concat({"Time": date, "Number": random_number}, axis=1)
print(output_ser)
