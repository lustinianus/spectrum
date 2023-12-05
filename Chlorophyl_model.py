import os
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter,OrderedDict
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from collections import defaultdict
from random import uniform
from math import sqrt,log
from scipy import signal
from scipy.signal import savgol_filter as sg
import pandas as pd
from copy import deepcopy
from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy
from examine_result import printer_spec,prementrarty



class fetch_data():
    def __init__(self):
        pass


    def spilte_index(self,dataframe):   #分割测量叶绿素含量的
        #dataframe 叶绿素含量数据
        #returan [(),(),....]
        list_index=[]
        for item in dataframe.index:
            x, y = item.split(sep="-")
            z=dataframe.iloc[dataframe.index.get_loc(item),5]
            list_index.append([x, y, z])
        return list_index


    def spec_index(self,df): #返回名字切割后的类和index的列表
        spec_index=[]
        spec_cata=[]
        for item in df["name"]:
            name_spilt = item.split(sep="_")
            spec_index.append(int(name_spilt[2].split(sep=".")[0]))
            spec_cata.append(name_spilt[1])

        return spec_index,spec_cata


    #
    # def spec_info(self,df)
    def spec_mean(self,data_chlorphyl,mean=5):
        df_mean=pd.DataFrame()
        data_chlorphyl.iloc[:, 1:] = data_chlorphyl.iloc[:, 1:].apply(pd.to_numeric, errors="ignore")
        for i in range(int(len(data_chlorphyl) / mean)):
            temp = data_chlorphyl[mean *i:mean*(i+1)]
            col_mean = temp.mean(axis=0, numeric_only=True)
            df_col_mean=pd.DataFrame(col_mean).T
            df_mean = pd.concat([df_mean, df_col_mean])
        return df_mean



if __name__=="__main__":
    os.chdir(r"F:\xiehui\python_workspace\R_worksapace\spectrum project of zhejiang university")
    df_total=pd.read_csv(r".\data.csv",dtype=str)
    df_chlorphyl=pd.read_csv(r".\chlorphyl\chlorphyl.csv", encoding='unicode_escape').T.iloc[1:,]
    # df_chlorphyl.colums=["a1","a2","a3","a4","a5"]
    # print(df_chlorphyl.index)


    fetch_data=fetch_data()  #将所有数据的类型和编号切出
    df_total["index"],df_total["cata"]=fetch_data.spec_index(df_total)


    des_index=fetch_data.spilte_index(df_chlorphyl)  #叶绿素文件index




    #筛选数据
    # print(Counter(df["cata"].tolist()))
    # print(set(df["cata"].tolist()))
    data_chlorphyl=pd.DataFrame()
    for item in des_index:
        cata,index,value=item
        temp_df=df_total[df_total["cata"]==str(cata)]
        df_filter=temp_df.iloc[0+15*int(index):15*(int(index)+1),]
        # df_filter.iloc[:,1:]=df_filter.iloc[:,1:].apply(pd.to_numeric,errors="ignore")
        # col_mean=df_filter.mean(axis=0,numeric_only=True)
        # df_filter.loc[len(df_filter)]=col_mean.T
        # print(df_filter)
        df_filter.loc[:,"value"]=value
        data_chlorphyl=pd.concat([data_chlorphyl,df_filter])




    #五条一平均
    data_mean=fetch_data.spec_mean(data_chlorphyl,15)

    print("mean",data_mean.head(5))
   # print(cata,df_filter.head(5)
    spec_print=printer_spec()


    df_initial=data_mean.iloc[:,0:2151]   #输入的不含标签value等值





    spec_pre = prementrarty()
    #
    examy, exam_x, df_spec_re = spec_pre.spec_resample(df_initial)
    df_spec_log = spec_pre.spec_log(df_spec_re)
    spec_res_sg = sg(x=df_spec_log.T, window_length=15, polyorder=2)
    spec_D1 = spec_pre.D1(spec_res_sg)



    des_data=pd.DataFrame(spec_D1).T
    des_data=des_data.reset_index()
    data_mean=data_mean.reset_index()
    des_data=pd.concat([des_data,data_mean.iloc[:,-3:]],axis=1)




    des_data.to_csv("./data_chlorphyl_sec.csv")
    #
    # # print(spec_D1.head(5))
    # # print(data_chlorphyl.head(6))
    # # print(df_spec_re.shape)
    spec_print.print_signel_curve(df_initial.T, title="df_initial").show()
    spec_print.print_signel_curve(spec_D1, title="D1").show()








    # df_chlorphyl[:,]






