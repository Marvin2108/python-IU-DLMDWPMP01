# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlite3
import sqlalchemy as db

# Datensätze laden
train = pd.read_csv(
    "/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/train.csv")
test = pd.read_csv(
    "/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/test.csv")
test.sort_values(0, 1)
# print(test)
ideal = pd.read_csv(
    "/Users/marvinschmitt/Library/CloudStorage/OneDrive-Persönlich/M.Sc. Data Science/06 Python/Datensatz/ideal.csv")

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
    print(train.head())
    train.shape
    sns.pairplot(train)
    ideal.head()
    ideal.shape
    plt.plot(ideal['x'], ideal['y49'])
    plt.scatter(train["x"], train["y4"])
    plt.show()


# berechnet Residuen training - ideal
# NICHT ÄNDERN!! 

def calculateSumSquareY1():  # erst mal nur für ideal.y1
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    # while ac_value :

    for column in ideal.columns[1:]:
        # print(column)
        for i in train.index:
            difference = []
            # print(i)
            diff = (train['y1'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function = column
            pass
        # else:
        #   break
    print("The ideal function for y1 is:", ideal_function)

    return lowest_value


def calculateSumSquareY2():  # erst mal nur für ideal.y1
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    # while ac_value :

    for column in ideal.columns[1:]:
        # print(column)
        for i in train.index:
            difference = []
            # print(i)
            diff = (train['y2'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function = column
            pass
        # else:
        #   break
    print("The ideal function for y2 is:", ideal_function)

    return lowest_value


def calculateSumSquareY3():  # erst mal nur für ideal.y1
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    for column in ideal.columns[1:]:
        # print(column)
        for i in train.index:
            difference = []
            # print(i)
            diff = (train['y3'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function = column
            pass
        # else:
        #   break
    print("The ideal function for y3  is:", ideal_function)

    return lowest_value


def calculateSumSquareY4():  # erst mal nur für ideal.y1
    """
    Returns sum of squared residuals
    -------
   berechnet train - ideal pro zeile ^2 
    """
    lowest_value = 999999999

    # while ac_value :

    for column in ideal.columns[1:]:
        # print(column)
        for i in train.index:
            difference = []
            # print(i)
            diff = (train['y4'][i] - ideal[column][i]) ** 2
            difference.append(diff)

        new_value = sum(difference)

        if new_value < lowest_value:
            lowest_value = new_value
            ideal_function = column
            pass
        # else:
        #   break
    print("The ideal function for y4 is:", ideal_function)

    return lowest_value


def main():
    """
    Hauptmethode zum Aufrufen und Orchestrieren des Programms
    """

    # print("ach hallo!")
    print("LeastSquare Y1 =", calculateSumSquareY1(), "\n")
    print("LeastSquare Y2 =", calculateSumSquareY2(), "\n")
    print("LeastSquare Y3 =", calculateSumSquareY3(), "\n")
    print("LeastSquare Y4 =", calculateSumSquareY4(), "\n")


#    visualize()


""" Ausführen der Main Methode"""
if __name__ == '__main__':
    main()
