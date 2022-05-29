import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlalchemy as db

# Datensätze laden
train = pd.read_csv("/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M. Sc. Data Science - IU/06 Python/Datensatz/train.csv")
test = pd.read_csv("/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M. Sc. Data Science - IU/06 Python/Datensatz/test.csv")
ideal = pd.read_csv(("/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M. Sc. Data Science - IU/06 Python/Datensatz/ideal.csv"))

print(train.head())
train.shape
sns.pairplot(train)
ideal.head()
ideal.shape
plt.plot(ideal['x'],ideal['y8'],label="ideal data")
plt.scatter(train["x"],train["y4"], color='green', label='Train data')
plt.legend()
plt.show()