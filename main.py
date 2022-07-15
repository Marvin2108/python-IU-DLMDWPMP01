#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:10:53 2022

@author: marvinschmitt
"""

# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import sqlalchemy as db
import math

# Datensätze laden
train = pd.read_csv(
    "/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/train.csv")
train.set_index('x',inplace=True)
test = pd.read_csv(
    "/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/test.csv")
test_sorted = test.sort_values('x')
test_sorted.set_index('x', inplace=True)
#print(test_sorted.head(21))

ideal = pd.read_csv(
    "/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/ideal.csv")
ideal.set_index('x',inplace=True)

# DB Connection 
# https://leportella.com/sqlalchemy-tutorial/

engine = db.create_engine(
    "sqlite+pysqlite:////Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 "
    "Python/python-IU/pythonsqlite.db",
    echo=True, future=True)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


# train.to_sql('train',engine, index=False, if_exists='append')
# ideal.to_sql('ideal',engine, index=False, if_exists='append')


def visualize():
    #plt.plot(ideal['x'], ideal['y33'])
    #sns.pairplot(train)
    fig, axs = plt.subplots(nrows=4, ncols=2)
    fig.suptitle('Compare train to ideal')

    
    train.plot(y='y1',ax=axs[0,0])
    ideal.plot(y='y36',ax=axs[0,1], label='ideal y36')
 
    # train y2
    train.plot(y='y2',ax=axs[1,0])
    ideal.plot(y='y11',ax=axs[1,1], label='ideal y11')
    
    # train y3
    train.plot(y='y3',ax=axs[2,0])
    ideal.plot(y='y2',ax=axs[2,1],label='ideal y2')
    
    # train y4
    train.plot(y='y4',ax=axs[3,0])
    ideal.plot(y='y33',ax=axs[3,1],label='ideal y33')
    
    #plt.scatter(train["x"], train["y4"])
    plt.show()

class Calculation:
    # referenzwert
    
    def __init__(self,trainNumber):
        self.trainNumber = trainNumber
        
    def calculate_least_square(trainNumber):
         difference = []  # save values of residuals
         lowestValue = 999999999 # needed for selecting lowest value
         
          
         for column in ideal.columns:
              for i in train.index:
            

                diff = (train[trainNumber][i] - ideal[column][i]) ** 2
                difference.append(diff)
                #print(len(difference))


              new_value = sum(difference)

              if new_value < lowestValue:
                  lowestValue = new_value
                  ideal_function = column
                
         return ideal_function
                
   # hier weitermachen!     
        
        

def calculateSumSquareY1():  # erst mal nur für ideal.y1
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999  # indicator for lowest value


    for column in ideal.columns:
        # print(column)
        difference = []
        for i in train.index:
            

            diff = (train['y1'][i] - ideal[column][i]) ** 2
            difference.append(diff)
            #print(len(difference))


        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function_y1 = column
            pass
        # else:
        #   break
  #  print("LeastSquareValue y1:", lowest_value)

    return ideal_function_y1


def calculateSumSquareY2():  # erst mal nur für ideal.y2
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    # while ac_value :

    for column in ideal.columns:
        # print(column)
        difference = []
        for i in train.index:
            #print(column, ideal[column][i])
            #print(i ,":", train['y2'][i])
            diff = (train['y2'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
                 lowest_value = new_value
                 ideal_function_y2 = column
                 pass
        # else:
        #   break
   # print("LeastSquareValue y2:", lowest_value)

    return ideal_function_y2


def calculateSumSquareY3():  # erst mal nur für ideal.y3
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    for column in ideal.columns:
        # print(column)
        difference = []
        for i in train.index:
            # print(i)
            diff = (train['y3'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function_y3 = column
            pass
        # else:
        #   break
#    print("LeastSquareValue y3:", lowest_value)

    return ideal_function_y3


def calculateSumSquareY4():  # erst mal nur für ideal.y4
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    # while ac_value :

    for column in ideal.columns:
        # print(column)
        difference = []
        for i in train.index:
            # print(i)
            diff = (train['y4'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function_y4 = column
            bezeichner = column
            pass
        # else:
        #   break
   # print("LeastSquareValue y4:", lowest_value)

    return ideal_function_y4



def test_function(): 
    """
    Testfunktion zum Validieren der idealen Daten 
    Testet, welche ideale Funktion am Besten zu dem Testwert passt (Bedingung: < sqrt(2))
    """
    test_matrix = test.join(ideal_functions, on='x') # Schnittmenge von Testdaten und idealen Funktionen
    
    for column in test_matrix.columns[2:5]:
        for row in test_matrix.index:
            result = abs(test_matrix['y'][row] - test_matrix[column][row]) # abs = absoluter Wert            
            
            if result < math.sqrt(2) and result > 0:
                test_matrix.loc[row, 'ideal function'] = column
                test_matrix.loc[row, 'delta'] = result
                
    
    return test_matrix
            



def main():
    """
    Hauptmethode zum Aufrufen und Orchestrieren des Programms
    """
    
    global ideal_functions
    data = {calculateSumSquareY1():ideal[calculateSumSquareY1()],
            calculateSumSquareY2():ideal[calculateSumSquareY2()],
            calculateSumSquareY3():ideal[calculateSumSquareY3()],
            calculateSumSquareY4():ideal[calculateSumSquareY4()]
           }
    ideal_functions = pd.DataFrame(data)
    
 
    print("Ideal function Y1 =", calculateSumSquareY1(), "\n")
    print("Ideal function Y2 =", calculateSumSquareY2(), "\n")
    print("Ideal function Y3 =", calculateSumSquareY3(), "\n")
    print("Ideal function Y4 =", calculateSumSquareY4(), "\n")
    
    
    test = Calculation
    print (test.calculate_least_square('y1'))
    


#test

    visualize()
    #print(test_sorted['x'])
    #plt.plot(test_sorted['x'], test_sorted['y'])
    #print (test_function())

    print (test_function())
   


""" Ausführen der Main Methode"""
if __name__ == '__main__':
    main()
