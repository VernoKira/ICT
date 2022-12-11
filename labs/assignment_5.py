''' 
The objective of this assignment is to clean the csv file of the attendance. 
The path to the csv file is "attendance_to_clean.csv" 
You can find it in the instruction folder. 
List of installed and authorized packages : 
    - csv 
    - pandas 
    - datetime 
    - numpy 
You cannot use other packages than the listed ones (except built-in default package in python). 
You can write you code after this comment : 
''' 
 
#Your code here: 
import csv 
import pandas as pd 
import datetime as dt 
import numpy as np 

# 1
missing_values = ["_", "error","two","NaN"]
df = pd.read_csv(r'attendance_to_clean.csv', na_values=missing_values)

for index, line in df.iterrows():
    try:
        int(line['NAME_STUDENT'])
        df.loc[index, 'NAME_STUDENT']=np.nan

    except:
        pass


# 2
for index, line in df.iterrows():
    try:
        if dt.datetime.strptime(line['DATE'], '%Y-%m-%d') < dt.datetime.strptime('2022-09-01', '%Y-%m-%d') or dt.datetime.strptime(line['DATE'], '%Y-%m-%d') > dt.datetime.strptime('2022-11-01', '%Y-%m-%d'):
            df.loc[index, 'DATE'] = np.nan
    except:
        df.loc[index, 'DATE']=np.nan
# df = df.sort_values(by =['DATE'])
# print(df)
# 3
# df = df.sort_values(by =['COUNT'])

for index, lines in df.iterrows():
    try:
        count = int(lines['COUNT'])
        if(count > 2):
            df.loc[index, 'COUNT']= np.nan
    except:
        df.loc[index, 'COUNT'] = np.nan

for index, lines in df.iterrows():
    try:
        time = int(lines['BEGIN_HOUR'])
        if(time> 17):
            df.loc[index,'BEGIN_HOUR'] = np.nan 
    except: 
        pass


# 4
df.dropna(inplace=True)
# 5
df.drop_duplicates(inplace=True)
#6
df.sort_values(by = ['NAME_STUDENT', 'DATE', 'BEGIN_HOUR', 'WEEK'], ignore_index= True, inplace= True)
df.reset_index(drop=True, inplace = True)
print(df)
