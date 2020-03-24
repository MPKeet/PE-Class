

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#Create random first year of revenue 
df=pd.DataFrame(np.random.randint(100000,2500000,size=(10000,1)))

#Second Random Year of Revenue
Yr2Rev=pd.DataFrame(np.random.randint(150000,3000000,size=(10000,1)))

#Creates a third year of revenue with a 12% over the past year
df['Yr3Rev'] = df['Yr2Rev'].apply(lambda x: x*1.12)

#Creates equity ownership of owners
Equity=pd.DataFrame(np.random.uniform(0.1,1,size=(10000,1)))


df=df.rename(columns={'Equity':'Owner_Equity'})


df=df.rename(columns={df.columns[0]:'Yr1Rev'})

#Creates randomized assets
Assets=pd.DataFrame(np.random.randint(1000000,10000000,size=(10000,1)))

df['Assets']=Assets

df=df.rename(columns={'Total Assets':'Total_Assets'})

#Creates randomized liabilities
Liabilities=pd.DataFrame(np.random.randint())

#Creates Current assets from total assets with a 0.25 assumption
df['Current_Assets'] = df['Total_Assets'].apply(lambda x: x*0.25)

#Total Liabilities randomisation
Total_Liabilities=pd.DataFrame(np.random.randint(1000000,8000000,size=(10000,1)))
df['Total_Liabilities']=Total_Liabilities

#Calulate current liabilities from total liabilities, assumption of 0.25 ratio
df['Current_Liabilities'] = df['Total_Liabilities'].apply(lambda x: x*0.25)

#Calculate Liquidity_R given information
df['Liquidity_R'] = df.apply(lambda x: x['Current_Assets'] if x['Current_Assets'] < 1 else x['Current_Assets']/x['Current_Liabilities'], axis=1)


#Creates Randomized COGS Ratio
Avg_COGS_R=pd.DataFrame(np.random.uniform(0.1,0.8,size=(10000,1)))
df['Avg_COGS_R']=Avg_COGS_R

#Gross Profit Margin
df['Profit'] = df.apply(lambda x: x['Yr3Rev'] if x['Yr3Rev'] < 1 else ((x['Yr3Rev']-(x['Yr3Rev']*x['Avg_COGS_R']))/x['Yr3Rev']), axis=1)

#Useful for a few trial runs
df=df.drop(columns='DtoC')

#Writes df to csv
df.to_csv(r'/Users/maxwellkeeter/Desktop/CompSci Resources/Python/PE.csv')


print(df)
