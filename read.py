import pandas as pd
data = pd.read_csv('data1.csv',sep='|')
x=data.loc[data['md5']=="1d980953ea54f78f1bef99bee4d9ba3b"]
print(x)
