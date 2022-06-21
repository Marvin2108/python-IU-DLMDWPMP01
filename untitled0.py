#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:42:19 2022

@author: marvinschmitt
"""

# DB Connection
# https://www.sqlitetutorial.net/sqlite-python/creating-database/

def create_connection(db_file):
    # create a database connection to a SQLite database 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)

    return conn
if __name__ == '__main__':
   conn = create_connection(r"/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/python-IU/pythonsqlite.db")

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)
        
        
        
#main

    database = r"/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/python-IU/pythonsqlite.db"
    
    sql_create_training_table = """ CREATE TABLE IF NOT EXISTS training (
                                        x float PRIMARY KEY,
                                        y1 float NOT NULL,
                                        y2 float NOT NULL,
                                        y3 float NOT NULL,
                                        y4 float NOT NULL
                                        ); """
    train.to_sql(training,conn)
   
    conn = create_connection(database)
    create_table(conn,sql_create_training_table)
    
    
    
    
    
    
    """
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
df_difference_y1 = pd.DataFrame(difference)"""