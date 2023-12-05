import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from collections import defaultdict
from random import uniform
from math import sqrt

class method_PCA():
    def __init__(self):
        pass
    def standardlize(self,data):
        scaler=StandardScaler()
        data_new=scaler.fit_transform(data)

        return data_new ,scaler.mean_,scaler.var_
    def pca(self,x,components=2):
        pca_result=PCA(n_components=components)
        principalcomponents=pca_result.fit_transform(x)
        pca_ev = pca_result.explained_variance_ratio_
        principalDF=pd.DataFrame(data=principalcomponents,columns=["component 1","component 2"])
        return principalDF , pca_ev
    #




if __name__=="__main__":
    data=pd.read_csv(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\txt数据\stat_data.csv")
    y=data.loc[:,["name"]]
    data=data.iloc[:,1:]
    pca=method_PCA()

    x,x_mean,x_var=pca.standardlize(data)
    principalDf,pca_ev=pca.pca(x)
    print(pca_ev)
    finalDf = pd.concat([principalDf, y], axis=1)
    finalDf['name_cata']=[x.split("_")[1] for x in finalDf["name"]]
    name_cata=set(finalDf["name_cata"].values.tolist())
    # finalDf.to_csv(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\txt数据\pca_data.csv")
    print(finalDf.head(10))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('2 Component PCA', fontsize=20)
    targets = name_cata
    colors = ['r', 'g', 'b','y']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf['name_cata'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'component 1']
                   , finalDf.loc[indicesToKeep, 'component 2']
                   , c=color
                   , s=50)
    ax.legend(targets)
    ax.grid()
    plt.show()





