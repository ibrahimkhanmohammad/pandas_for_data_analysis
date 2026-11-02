#           join() combines two DataFrames using their indexes by default.

import pandas as pd

'''
students = pd.DataFrame({ "Name": ["Ali", "Ahmed", "Sara"]}, index=[1, 2, 3])
scores = pd.DataFrame({ "Score": [85, 90, 95]}, index=[1, 2, 3])

result = students.join(scores)
print(result)
'''

# Suppose the indexes don't match:
students = pd.DataFrame({"Name": ["Ali", "Ahmed", "Sara"]}, index=[1, 2, 3])
scores = pd.DataFrame({"Marks": [85, 90, 95]}, index=[2, 3, 4])

# result = students.join(scores, how="left")         #   1 2 3
# result = students.join(scores, how="right")        #   2 3 4
# result = students.join(scores, how="inner")        #   2 3
# result = students.join(scores, how="outer")        #   1 2 3 4
# print(result)