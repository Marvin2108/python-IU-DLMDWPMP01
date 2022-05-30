import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlalchemy as db

# Datensätze laden
train = pd.read_csv("/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/train.csv")
test = pd.read_csv("/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/test.csv")
ideal = pd.read_csv(("/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/ideal.csv"))

"""print(train.head())
train.shape
sns.pairplot(train)
ideal.head()
ideal.shape
plt.plot(ideal['x'],ideal['y49'])
plt.scatter(train["x"],train["y4"])
plt.show()"""

# berechnet Residuen training - ideal
# NICHT ÄNDERN!! 

def calculateOneSumSquare():  # erst mal nur für ideal.y1
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro reihe ^2 
    """
    difference=[]
    for i in train.index:
        diff = (train['y1'][i] - ideal['y1'][i])**2
        difference.append(diff)
    return sum(difference)
print("def calculateLeastSquare", calculateOneSumSquare())
#print(pd.DataFrame(difference))


# minimalen wert für y1 berechnen 
df = pd.DataFrame(index=np.arange(-20,20,0.1),columns=np.arange(1,51))
#print(df.shape)

difference=[]
dfn = pd.DataFrame(index=np.arange(0,401))
print(dfn.shape)

def calculation ():
#für jede y-Spalte in ideal...
    for column in ideal.iloc[:,1:51]:
        dfn[column] = pd.NaT
        
        for column1 in train.iloc[:,1:5]:
            
        #print(column)
        #...die Differenz zwischen train und ideal berechnen (pro Zeile)
            for row in train.index:
                #print(row)
                squared_residual = (train['y1'][row] - ideal[column][row])**2
                difference.append(squared_residual)
                
                dfn[column][row] = squared_residual
                #dfn.insert(row, column, squared_residual)
        
#print(dfn.head(20))
df_sum = pd.DataFrame()
#OLS berechnen pro y
for column in dfn:
    sum_error = dfn[column].sum()
    #df_sum[column] = pd.NaT
    df_sum[column][0] = sum_error
print(df_sum.head())
    #print(column, dfn[column].sum().min())


# convert list to pd-DataFrame
df_difference_y1 = pd.DataFrame(difference)

#erst mal nur mit liste für y1


#DB Connection
#kein plan ey
"""
engine = db.create_engine('sqlite:///foo.db')
connection = engine.connect()
meta_data = db.MetaData()

train.to_sql('train', engine)

# wie sehe ich jetzt das tabelle erstellt wurde? 
"""

