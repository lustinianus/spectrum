import pandas as pd
import os
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier



df = pd.read_excel(r".\leaf_single.xlsx")
df_com = pd.read_excel(r".\leaf_complex.xlsx")
column_ls=df.columns.tolist()

column_ls[2],column_ls[3]=column_ls[3],column_ls[2]

df_com.columns=column_ls

#获取9-2类似数据中的主类
df["group"] = pd.to_numeric(df.iloc[:,0].apply(lambda x : int(x.split("-")[0])))

df["source_type"]="single"
df_com["group"] = pd.to_numeric((df_com.iloc[:,0]))
df_com["source_type"]="complex"

#按类排序
df_result = pd.concat([df,df_com]).sort_values(by="group",ascending=True)


#去除不能数字化的值
df_DROPNA=df_result.apply(pd.to_numeric,errors="coerce").iloc[:,1:]
df_DROPNA["name"],df_DROPNA["source_type"]=df_result["序号"].astype(str),df_result["source_type"]



print(df_DROPNA)
print("*"*50)


df_info=df_DROPNA.info()
print(df_info)
print("-"*40)
print(df_DROPNA.describe(include="all"))
print("-"*40)
print(df_DROPNA.isnull().sum())


df_DROPNA.to_csv("./result.csv")