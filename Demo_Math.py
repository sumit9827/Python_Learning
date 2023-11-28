# # import math
# # x = math.pi
# # print(x)

# # float_list = (.1, .2, .3, .4)

# # print(math.fsum(float_list))

# import numpy as np

# some_list = [1,2,3,4,5,6,7,8]

# print(type(some_list))

# some_array = np.array(some_list)

# print(type(some_array))

# print(some_array)

# ones_array = np.ones(5)

# print(ones_array)

# range_array = np.arange(8)

# print(range_array)

# reshape_array = range_array.reshape(4,2)

# print(reshape_array)

import pandas as pd

df = pd.DataFrame({
    'name' : ["john", "Alice", "Sumit"],
    'gender': ["M", "F", "M"],
    'age' : [45, 20, 30]
})

print(df)

# print(df.describe())

sub_df = df[['name', 'age']]

print(sub_df)
groupby_df = df.groupby(by = 'gender').count()
print(groupby_df)