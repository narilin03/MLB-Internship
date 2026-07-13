import pandas as pd

data=pd.read_csv("Day4/practice_tasks/Titanic-Dataset.csv")
print("Dataset loaded\n")

print("First 5 rows:\n", data.head(5))
print("\nLast 5 rows:\n", data.tail(5))

print("\nDataset Information:")
data.info()

print("\nMissing Values in each column:\n", data.isnull().sum())

print("\nFiltered Data(Passengers under 18):")
under18=data[data["Age"]<18]
print(under18.head())

print("\nSummary Statistics:\n",data.describe())

