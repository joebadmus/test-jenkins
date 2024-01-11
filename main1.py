import pandas as pd

rows = pd.read_csv("test.csv", nrows=2)

print("print 2 rows")
print(rows)

print("print columns")
names = pd.read_csv("test.csv", usecols=['name'])
print(names)

print("print conditional rows")
older_then_26 = pd.read_csv("test.csv", usecols=['name'])

print(older_then_26[rows["age"]] > 26)
