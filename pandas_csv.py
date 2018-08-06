
import pandas as pd
import os

path = "C:/Users/dada/Desktop/test"
files = os.listdir(path)
df1 = pd.DataFrame()
for file in files:
    filename = file.split(".")[0]
    df = pd.read_csv(path+'/'+filename+'.csv', encoding='utf-8', index_col=0,)
    # pd.set_option('display.max_rows',6)
    df1 = pd.concat([df1, df], join='outer')

df1.to_excel('test.xlsx', sheet_name='sheet1')