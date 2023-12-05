import os
import scipy.signal
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt


df=pd.read_csv(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\txt数据\signel_file.csv")

index,row= next(df.iterrows())
print(".....",index)
    # print(index)
    # print(row.shape)

    # print(row.values[1:row.shape[0]-1])
spec_value=list(row.values[1:])
spec_index=np.linspace(350, 2500, 2151)
    # print(spec_value)
# print(spec_value)
# print(spec_index)
# print(len(spec_value),len(spec_index))
with plt.style.context(('ggplot')):
    fonts = 6
    plt.figure(figsize=(5.2, 3.1), dpi=200)
    plt.plot(spec_index, spec_value)
    plt.xlabel('Wavelength (nm)', fontsize=fonts)
    plt.ylabel('reabsorbance', fontsize=fonts)
    plt.title("title", fontsize=fonts)
#     plt.plot(spec_index,spec_value)
    plt.show()

indice=scipy.signal.find_peaks(spec_value)
list_index=[]
# print(list_index)

for item in indice[0]:
    # print(int(item))
    list_index.append(int(spec_index[item]))
# map(int,list_index)
# map(str,list_index)
# print(list_index)
print(df.columns)
print(list_index)
stat_data=pd.DataFrame()
for item in list_index:
    print("this is ",item)
    filter_data=df.iloc[:,item-350]
    stat_data=pd.concat([stat_data,filter_data],axis=1)
stat_data=pd.concat([df.iloc[:,0],stat_data],axis=1)
print(df)
print(stat_data)
# stat_data.to_csv(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\txt数据\stat_data.csv")




# print (type(df.columns.tolist()[0]))
# print(indice[0])

# for item in indice[0].astype(int):

# print(df[spec_index[int(indice[0])]])



# plt.plot(indice[0],spec_value[0],"o")
# plt.show()
# print(indice)






    # signal.find_peaks(item[1:len(item)-1])
    # a=list(item)
    # spec=a[1]
    # print(spec.shape)
    # spec = spec[:, :(spec.shape[0] - 1)]
# print(type(a[1]))
# print(a[1][0:len(a)-1])
