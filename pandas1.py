import pandas as pd
import numpy as np

# question1: how to import pandas and check its version?
print(pd.__version__)
print(pd.show_versions(as_json=True))

# question2: how to create a series from a list, numpy array or dict?
a_list = list("abcdefg")
numpy_array = np.arange(1, 10)
dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 5}
series1 = pd.Series(a_list)
series2 = pd.Series(numpy_array)
series3 = pd.Series(dictionary)
print(series1)
print(series2)
print(series3)

# question3: how to convert the index of a series into a column of a data frame?
mylist = list("abcdefghijklmnopqrstuvwxyz")
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
print(ser[:5])

ser_df = pd.DataFrame(ser)
ser_df.reset_index()
ser_df = ser.to_frame().reset_index()
print(ser_df)

# question4: how to combine many series to form a data frame?

ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
# solution1
ser_df = pd.DataFrame(ser1, ser2).reset_index()
print(ser_df.head())
# solution2
ser_df = pd.DataFrame({"col1": ser1, "col2": ser2})
print(ser_df.head())
# solution3
ser_df = pd.concat([ser1, ser2], axis=1)
print(ser_df.head())


# question5: how to assign name to the series' index?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser.name = "alphabets"
print(ser.name)
ser_out = ser.rename("other name")
print(ser_out.name)
