import os
import pandas as pd
from pathlib import Path



os.chdir(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\txt数据")
P=Path(r"./")
df=pd.DataFrame()


for item in P.iterdir():
    data=pd.read_csv(str(item),header=None,encoding="utf-16LE",sep="\t",names=["样本","序号","波段","值"])
    df=pd.concat([df,data])


print (df.columns.tolist())
df=pd.pivot(df,index="样本",columns="波段",values="值")
print(df)
print(df.shape)
df.to_csv("./data.csv")


