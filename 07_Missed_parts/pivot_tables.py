import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [30000, 40000, 25000, 35000, 50000, 45000]
})

'''Use pivot_table() to calculate the average salary:
- Department should be the rows (index).
- Gender should be the columns.
- Salary should be the values.
- Use mean as the aggregation function.'''

avg_salary = df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="mean")
print(avg_salary)

