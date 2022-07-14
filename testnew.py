import pandas as pd
import tushare as ts 
import matplotlib.pyplot as plt
ts.set_token('c70a176ea90399a88c372b9c78ed2dad0363b7c3dd9b8a0010220e9d')
pro=ts.pro_api()

ningde=ts.get_k_data(code='300750',start='1994-01-01')
# print(tianye)
ningde.to_csv('ningde.csv')
Ningde=pd.read_csv('ningde.csv',index_col='date',parse_dates=['date'])
# Ningde=Ningde['2019':'2022']
print(Ningde)
Ningde['close'].plot(x='date',kind='line')
#version v1.0
#version v2.0
#version v3.0
plt.show() 