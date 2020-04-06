import pandas as pd
import numpy as np

# question11: how to bin a numeric series to 10 groups of equal size?
# function about cut and qcut
ser = pd.Series(np.random.random(20))
print(pd.qcut(ser, q=10))
print(pd.qcut(ser, q=10, labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head())

# question12: how to convert a numpy array to a data frame of given shape?
ser = pd.Series(np.random.randint(1, 10, 35))
# via numpy
print(pd.DataFrame(np.array(ser).reshape(7, 5)))
# only pandas
print(pd.DataFrame(ser.values.reshape(7, 5)))

# question13: how to find the positions of numbers that are multiples of 3 from a series?
np.random.RandomState(0)
ser = pd.Series(np.random.randint(1, 5, 10))
# using where clause
ser.where(lambda x: x % 3 == 0).dropna()
print(ser)

# question14: how to extract items at given positions from a series?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 3, 8, 14, 20]
# solution1 via loc
ser_output = ser.loc[pos]
print(ser_output)
# solution2 via series take, since we haven used numpy take in pandas3.py, it has the same meaning
ser_output = ser.take(pos)
print(ser_output)

# question15: how to stack two series vertically and horizontally?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
# vertically
ser1.append(ser2)
# we can also use concat and axis 0
ser_output1 = pd.concat([ser1, ser2], axis=0)
print(ser_output1)

# horizontally, by the way review the method of set title of data frame
ser_output2 = pd.concat({"col1": ser1, "col2": ser2}, axis=1)
print(ser_output2)
