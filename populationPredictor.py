import math
import numpy as np
import pandas as pd
from tabulate import tabulate

def makeTable():
    print(tabulate())
    
if __name__ == "__main__":
    country_df = pd.read_csv('csvData.csv')
    country = input("Please select a country: ")
    df = country_df[country_df['name'].str.contains(country)]
    print(df)
    countryPop = int(df['pop2021'] * 1000)
    countryGrowth = df['GrowthRate']
    print('The population of %s is %.0f' %(country,countryPop))
    print('The growth rate of %s is %.4f' %(country,countryGrowth))

    year = input("Of which year do you want to find the predicted population of %s? " %(country))
    time = int(year) - 2021
    predictedPop = countryPop * math.exp(countryGrowth*time)
    yearInterval = input("Please choose the year interval for predicting the population: ")
    print('The predicted population of %s is expected to be %.0f' %(country,predictedPop))