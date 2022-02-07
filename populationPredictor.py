import math
from msilib.schema import tables
import numpy as np
import pandas as pd
from tabulate import tabulate
from datetime import date

def getTable(table):
    header = ["Year", "Population"]
    print(tabulate(table,header))
    
def getPopulation(currentYear):
    time = int(year) - 2021
    predictedPop = countryPop * math.exp(countryGrowth*time)
    
    
if __name__ == "__main__":
    isYear = False
    currentDate = date.today()
    currentYear = currentDate.year
    print(currentYear)
    intervalColumn = []
    country_df = pd.read_csv('csvData.csv')
    country = input("Please select a country: ")
    df = country_df[country_df['name'].str.contains(country)]
    print(df)
    countryPop = int(df['pop2021'] * 1000)
    countryGrowth = df['GrowthRate']
    print('The population of %s is %.0f' %(country,countryPop))
    print('The growth rate of %s is %.4f' %(country,countryGrowth))

    while(isYear == False):
        year = input("Select a year after the year 2022: ")
        if(int(year) <= 2022):
            isYear = False
            year = input("Invalid year. Please select a year after 2022: ")
        else:
            isYear = True
    
    yearInterval = input("Please choose the year interval for predicting the population: ")
    
    
    while (currentYear <= int(year)):
        intervalColumn.append(currentYear)
        currentYear += int(yearInterval)
        
    
    print(intervalColumn)
    getTable(intervalColumn)