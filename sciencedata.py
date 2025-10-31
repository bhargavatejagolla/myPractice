# import re
# my_regex = re.compile("[0-9]+",re.I)
# print(my_regex)
# two_plus_three = 2+\
#     3
# print(two_plus_three)
# from collections import defaultdict,Counter
# lookup = defaultdict(int)
# my_counter = Counter()
# print(lookup)
# match = 10
# from re import *
# print(match)
# def double(x):
#     """This is a docstring
#     """
#     return 2*x

# def apply_to_one(f):
#     return f(1)
# my_double = double
# x = apply_to_one(my_double)

# y = apply_to_one(lambda x:x+4)


# def another_double(x):
#     return 2*x

# def my_print(message = "my default message"):
#     print(message)
# my_print("hello worlds")
# def full_name(first = "what-his-name",last = "something"):
#     return first +" "+ last
# print(full_name(first ="bharga....."))

# tab_string = r"\t"
# print(len(tab_string))
# import pandas as pd
# temperatures = pd.Series([20,22,23,19,21],index = ['Mon','Tue','Wed','Thus','Fri'])
# print(temperatures)
# print("Average temperatures:",temperatures.mean())
# weather_data = pd.DataFrame({
#     'Temperature':[20,22,23,19,21],
#     'Humidity':[45,47,50,43,42],
#     'WindSpeed':[10,12,8,15,11],

# },index = ['Mon','Tue','Wed','Thus','Fri'])
# print(weather_data)
# print(weather_data.mean())
# /import pandas as pd
# data_list = [
#     ['Alice', 25, 'New York'],
#     ['Bob', 30, ' San Francisco'],
#     ['Charlie', 35, 'Los Angeles']
# ]
# df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
# print(df_from_list)
# import pandas as pd
# data =[
#     {'name': 'Alice', 'age': 25, 'city': 'New York'},
#     {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
#     {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
# ]
# df = pd.DataFrame(data)
# print("common keys:\n",df)
# import pandas as pd
# data1 = [
#     {'name': 'Alice', 'age': 25, 'city': 'New York'},
#     {'name': 'Bob', 'age': 30},  # Missing 'city'
#     {'name': 'Charlie', 'city': 'Los Angeles'}  # Missing 'age'
# ]

# df1 = pd.DataFrame(data1)
# print('Missing keys:\n', df1)
# import pandas as pd
# data2 = [
#     {'name': 'Alice', 'age': 25, 'city': 'New York'},
#     {'name': 'Bob', 'age': 30, 'city': 'San Francisco', 'salary': 75000},
#     {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles', 'department': 'Sales'}
# ]

# df2 = pd.DataFrame(data2)
# print('Extra keys:\n', df2)impor
# import pandas as pd
# import numpy as np
# np.random.seed(0)
# student = pd.DataFrame({
#     'Name': [f"student_{i}" for  i in range(1,11)],
#     'Age' : np.random.randint(18,25,10),
#     'Grade': np.random.randint(60,101,10),
# })
# print(student)
# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 35, 28, 32],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
# })

# # Update your code below this line
# print(df[['Name', 'City']])
# print(df.iloc[4])
# import pandas as pd
# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 35, 28, 32],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
#     'Salary': [50000, 70000, 65000, 60000, 75000]
# })
# # Select rows where Age is greater than 30
# print(df[df['Age'] > 30])
# # Select rows where City is either New York or Boston
# print(df[df['City'].isin(['New York', 'Boston'])])
# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 35, 28, 32],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
#     'Salary': [50000, 70000, 65000, 60000, 75000]
# })

# # Update your code below this line
# print(df[df['Salary'] > 64000])
# print(df[df['Salary'].isin([70000,65000])])
# import pandas as pd
# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 35, 28, 32],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
#     'Salary': [50000, 70000, 65000, 60000, 75000]
# })

# # Select first 3 rows and first 2 columns
# print(df.iloc[:3, :2])

# # Select 'Age' and 'Salary' for 'Alice' and 'Bob'
# print(df.loc[[0, 1], ['Age', 'Salary']])
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [
#                   5, np.nan, np.nan, 8], 'C': ['a', 'b', 'c', None]})

# # Update your code below this line
# print(df.dropna())
# import pandas as pd

# df = pd.DataFrame({
#     'A': ['bt', 2, 3],
#     'B': [1.0, 2.0, 3.0],
#     'C': ['a', 'b', 'c'],
#     'D': [True, False, True],
#     'E': pd.date_range('20230101', periods=3),
#     'F': [1, 2, None]
# })

# # Update your code below this line
# print(df['A'].dtype)
# print(type(df['A'][0]))
# import pandas as  pd
# df = pd.DataFrame({
#     'A': ['1', '2', '3'],
#     'B': [1.1, 2.2, 3.3],
#     'C': [1, 2, 3]
# })

# df[['A', 'B', 'C']] = df[['A', 'B', 'C']].apply(pd.to_numeric, errors='coerce')
# print(df)
# for col in df.columns:
#     print(df[col].dtype)

# import pandas as pd
# import numpy as np
# n = 1_1000_000
# data = np.random.choice(['Apple', 'Banana', 'Cherry'], size=n)
# df = pd.DataFrame({'Fruit': data})
# print("Memory usage without Categorical:")
# print(df.memory_usage(deep=True))
# df['Fruit'] = df['Fruit'].astype('category')
# print("\nMemory usage with Categorical:")
# print(df.memory_usage(deep=True))
