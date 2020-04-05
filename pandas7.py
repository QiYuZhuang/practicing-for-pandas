import pandas as pd
import numpy as np

# question31: how to fill an intermittent time series so all missing dates show up with
# values of previous non-missing date?
date = pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08'])
input_ser = pd.Series([1, 10, 3, np.nan], index=list(date))
output_ser = input_ser.resample('D').bfill().ffill()  # D represents Day
print(output_ser)

# question32: how to compute the auto correlations of a numeric series?
input_ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
auto_correlations = [input_ser.autocorr(i).__round__(2) for i in range(11)]
print(auto_correlations[1:])
print('Lag having highest correlation:', np.argmax(np.abs(auto_correlations[1:])) + 1)

# question33: how to import only every nth row from csv file to create a data frame?
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataset = pd.read_csv('housing.csv', delimiter=r'\s+', names=column_names, chunksize=50)
data_frame = pd.concat([chunk.iloc[0] for chunk in dataset], axis=1)
data_frame_2 = data_frame.transpose()
data_frame_2.index = list(range(11))
print(data_frame_2)

# question34: how to change column values when importing csv to a data frame?
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataset = pd.read_csv('housing.csv', delimiter=r'\s+',
                      names=column_names, converters={"MEDV": lambda x: "HIGH" if float(x) >= 25 else "LOW"})
print(dataset)

# question35: how to create a data frame with rows as strides from a given series?
L = pd.Series(range(15))
index_1 = np.arange(0, 15, 2)
output_array = np.array([L[index_1[i]:index_1[i+2]] for i in range(6)])
print(output_array)
