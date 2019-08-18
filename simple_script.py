import numpy as np
import os
import pandas as pd



a=np.array([1,2,3,4,8])
b=a*2-3

os.chdir(r'C:\Users\Чигин Сергей\Desktop\repo_for_testing\input_data')
df=pd.read_excel('data_sample.xls')

c=df['column_1'].max()

b=b+c

print(b)

