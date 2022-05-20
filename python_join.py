import pandas as pd
import os

df = []

for i in range(1, 9):    

    pathf = 'SimResults-2022-05-10-15.07/'+str(i)+'/'
    for filename in os.listdir(pathf):
        print(filename)
        if filename.endswith('.csv'):
            df1 = pd.read_csv(filename, header=None)

            for row in df1:
                df.append(row)

dat = pd.DataFrame(df)
print(len(dat))
print(dat.head())
