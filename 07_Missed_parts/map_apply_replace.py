import pandas as pd
marks = pd.Series([85, 90, 78, 95])

# map() = Transform values according to a mapping; unmapped values become missing.
# result = marks.map({
#     85: "A",
#     90: "A+",
#     78: "B",
#     95: "A+"
# })
# print(result)

#  here except at "B" every other will be NaN
# result = result.map({"B": "C"})
# print(result)

# apply() lets you apply a function to each value in a Series or along rows/columns of a DataFrame.
new_marks = marks.apply(lambda x: x + 5)
print(new_marks)

#  replace() = Change specified values while keeping everything else unchanged.

updated_marks = new_marks.replace(83, 85)
print(updated_marks)