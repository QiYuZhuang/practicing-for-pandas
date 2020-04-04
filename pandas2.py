import pandas as pd
import numpy as np

# question6: how to get the items of series A not present in series B
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser_out = ser1[~ser1.isin(ser2)]
print(ser_out)

# question7: how to get the items not common to both series A and series B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# solution1 via pandas
a_not_b = ser1[~ser1.isin(ser2)]
b_not_a = ser2[~ser2.isin(ser1)]
ser_output = a_not_b.append(b_not_a, ignore_index=True)
print(ser_output)
"""
function prototype of append has four important arguments,
DataFrame.append(other, ignore_index=False, verify_integrity=False, sort=None)
ignore_index, when it comes to True, it avoid repeating, default is false
case other is one_dimension, it builds via columns
case other is two_dimension, it builds via rows
case other is three or more dimensions, it only add an element to DataFrame
"""
# solution2 via numpy
ser_u = pd.Series(np.union1d(ser1, ser2))
ser_i = pd.Series(np.intersect1d(ser1, ser2))
ser_output = ser_u[~ser_u.isin(ser_i)]
print(ser_output)

# question8: how to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
state = np.random.RandomState(1000)
# generate Pseudo Random Number
ser = pd.Series(state.normal(10, 5, 25))
# solution1 via pandas
print(ser.describe())
# solution2 via numpy
print(np.percentile(ser, q=[0, 25, 50, 75, 100]))

# question9: how to get frequency counts of unique items of a series?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser_output = ser.value_counts()
print(ser)

# question10: how to keep only 2 most frequent values as it is and replace  everything else as 'Other'
np.random.RandomState(0)
ser = pd.Series(np.random.randint(1, 5, [12]))
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
