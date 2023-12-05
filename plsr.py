import pandas as pd
import numpy as np
import os
from sklearn.cross_decomposition import PLSRegression

if __name__=="__main__":
    os.chdir(r"F:\xiehui\python_workspace\R_worksapace\spectrum project of zhejiang university\chlorphyl\chlorphyl")
    df=pd.read_csv(".\data_for_plsr.csv")
