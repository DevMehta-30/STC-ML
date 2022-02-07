import numpy as np
import pandas as pd

df= pd.read_csv("StudentsPerformance.csv")
df['Total']= df['math score'] + df['reading score'] + df['writing score']
df['Average']=df['Total']/3

#print(df)
print(df[["gender","Average"]].groupby("gender").mean())