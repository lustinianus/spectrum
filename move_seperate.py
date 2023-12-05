import os
from pathlib import Path
import shutil


p=Path(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\temp")
list_data=list(p.iterdir())
for i in range(0,len(list_data)-1,1000):
    temp=list_data[i:i+1000]
    if not os.path.exists(p/str(i)):
        os.makedirs(p/str(i))
    for item in temp:
        shutil.copy(item,p/str(i))









