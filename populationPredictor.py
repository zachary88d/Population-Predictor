import math
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

country_df = pd.read_csv('csvData.csv')

country = input("Please select a country: ")

df = country_df[country_df['name'].str.contains(country)]
print(df)
countryPop = int(df['pop2021'] * 1000)
countryGrowth = df['GrowthRate']
print('The population of %s is %f' %(country,countryPop))
print('The growth rate of %s is %f' %(country,countryGrowth))

year = input("Of which year do you want to find the predicted population of %s? " %(country))
predictedPop = countryPop*math.exp(countryGrowth*(year - 2021))