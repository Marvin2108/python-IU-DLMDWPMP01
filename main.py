#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:10:53 2022

@author: marvinschmitt
"""

# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
import os
import math

dirname = os.path.dirname(__file__) # get current directory
print ("current directory:", dirname)



"""
loading given csv files into a pandas dataframe
using relative path to find CSV-files 
The CSV-files have to be in the same path! 
"""

# training dataset    
training = pd.read_csv(os.path.join(dirname, 'training.csv')) # relative directory to current file
training.set_index('x',inplace=True) # set index to x

# ideal dataset 
ideal = pd.read_csv(
        os.path.join(dirname, 'ideal.csv'))
ideal.set_index('x',inplace=True) # set index to x

# test dataset    
test = pd.read_csv(
        os.path.join(dirname, 'test.csv'))



"""
This section creates a database, and
creates new tables for given training and ideal datasets
"""

engine = db.create_engine("sqlite:///database.sqlite")
if not database_exists(engine.url):
    create_database(engine.url)


training.to_sql('training',engine, index=True, if_exists='replace') # creates new table in db out of dataframe
ideal.to_sql('ideal',engine, index=True, if_exists='replace') # creates new table in db out of dataframe


"""
creating own Exception class called RangeError for checking training column
"""
class RangeError(Exception):
# einen Konstruktor definieren
    
    def __init__(self):
        
        # eine eigene Nachricht als Attribut definieren
        my_message = 'Eigener Fehler'
        self.my_message = my_message
        


        
        
"""
This section creates Calculation super class with trainingNumber as variable
The LeastSquareMethod inherites trainingNumber and calculates the values
"""
class Calculation(): 
    
    def __init__(self,trainingNumber):
        self.trainingNumber = trainingNumber
        
class LeastSquareMethod(Calculation):

    def calculate_least_square(trainingNumber):
    #    print("o",getattr(idealY1, trainingNumber))

        """
        this function calculates for each given trainingNumber its ideal function
        from the ideal dataset using Minimum SumLeastSquared

        Output:
        -------
        idealFunction : TYPE
        returns corresponding ideal function for given trainingNumber
        e.g. y36
        """
        
        # Exception for only 4 allowed trainingNumbers
        try:
            if trainingNumber not in ['y1','y2','y3','y4']:
                raise RangeError
        except:
            print("RangeError: This is a range error. Watch out!")
        else:
        
            lowestValue = 999999999 # needed for calculating lowest value 
              
            for column in ideal.columns: # durchlauf für jedes y aus ideal
                 sumSquared = []  # save values of residuals per column
                 
                 for i in training.index: # jede Zeile im training-Datensatz
                    diff = (training[trainingNumber][i] - ideal[column][i]) ** 2
                    sumSquared.append(diff) # um später summenwert pro spalte aus ideal zu haben
    
                 newValue = sum(sumSquared)
    
                 if newValue < lowestValue:  # prüfen, ob ein y Wert aus ideal besser ist als der bisherige beste Wert
                     lowestValue = newValue
                     idealFunction = column
            print("ideal function for",trainingNumber, "=", idealFunction)
                
            return idealFunction
                        

def visualize_train_to_ideal():
    """
    This function creates subplots to compare training data 
    with its corresponding ideal function
    """
    #plt.plot(ideal['x'], ideal['y33'])
    #sns.pairplot(training)
    fig, axs = plt.subplots(nrows=4, ncols=2)
    fig.suptitle('Compare training to ideal')
    
    training.plot(y='y1',ax=axs[0,0])
    ideal.plot(y='y36',ax=axs[0,1], label='ideal y36')
 
    # training y2
    training.plot(y='y2',ax=axs[1,0])
    ideal.plot(y='y11',ax=axs[1,1], label='ideal y11')
    
    # training y3
    training.plot(y='y3',ax=axs[2,0])
    ideal.plot(y='y2',ax=axs[2,1],label='ideal y2')
    
    # training y4
    training.plot(y='y4',ax=axs[3,0])
    ideal.plot(y='y33',ax=axs[3,1],label='ideal y33')
    
    #plt.scatter(training["x"], training["y4"])
    plt.show()



def test_function():
    """
    Testfunktion zum Validieren der zuvor ermittelten idealen Datensätze 
    Testet, welche ideale Funktion am Besten zu dem Testwert passt (Bedingung: < sqrt(2))

    Returns
    -------
    test_matrix : TYPE: DataFrame
        Spalten: x,y, 4 ideale Funktionen, best fit, delta.

    """
    test_matrix = test.join(ideal_functions, on='x') # Schnittmenge von Testdaten und idealen Funktionen
    
    for column in test_matrix.columns[2:5]:
        for row in test_matrix.index:
            result = abs(test_matrix['y'][row] - test_matrix[column][row]) # abs = absoluter Wert            
            
            if result < math.sqrt(2) and result > 0:
                test_matrix.loc[row, 'best fit'] = column
                test_matrix.loc[row, 'delta'] = result
    
    test_matrix.to_sql('test',engine, index=False, if_exists='replace')
    
    ax = test_matrix.plot(x='x',y=['y'],kind='scatter', label='test-data',color='purple')
   # training.plot(ax=ax,use_index=True, label='training')
    ideal_functions.plot(ax=ax)    

    return test_matrix          



def main():
    """
    This is the main method of the Python script which orchestrates the program
    """
    
    global ideal_functions # new DF in order to save determined ideal functions
    
    # create instances for each training column
    idealY1 = LeastSquareMethod # Instanz 1
    idealY2 = LeastSquareMethod # Instanz 2
    idealY3 = LeastSquareMethod # Instanz 3
    idealY4 = LeastSquareMethod # Instanz 4
    
    try:
        data = {idealY1.calculate_least_square('y1') : ideal[idealY1.calculate_least_square('y1')],
                idealY2.calculate_least_square('y2') : ideal[idealY2.calculate_least_square('y2')],
                idealY3.calculate_least_square('y3') : ideal[idealY3.calculate_least_square('y3')],
               # idealY3.calculate_least_square('y20') : ideal[idealY3.calculate_least_square('y20')],  # test exception
                idealY4.calculate_least_square('y4') : ideal[idealY4.calculate_least_square('y4')]
                }
    
    except KeyError:
        print("KeyError: This y-value is not within the training dataset!")
    
    else:
        ideal_functions = pd.DataFrame(data)
        print (test_function()) # returns dataframe of test_matrix

    

    visualize_train_to_ideal() # call function to visualize ideal data compared to training data




   
""" Ausführen der Main Methode"""
if __name__ == '__main__':
    main()
