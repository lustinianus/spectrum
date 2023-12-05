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



class printer_spec():       #图像绘制
    def PlotSpectrum(self,spec, title='原始光谱', x=0, m=1):
        """
        :param spec: shape (n_samples, n_features)
        :return: plt
        """
        if isinstance(spec, pd.DataFrame):
            spec = spec.values
        spec = spec[:, :(spec.shape[1] - 1)]
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        wl = np.linspace(x, x + (spec.shape[1] - 1) * m, spec.shape[1])
        with plt.style.context(('ggplot')):
            fonts = 6
            plt.figure(figsize=(5.2, 3.1), dpi=200)
            plt.plot(wl, spec.T)
            plt.xlabel('Wavelength (nm)', fontsize=fonts)
            plt.ylabel('reabsorbance', fontsize=fonts)
            plt.title(title, fontsize=fonts)
        return plt



    def axspectrum(self,spec):   #画图方法
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('wavelength', fontsize=15)
        ax.set_ylabel('reabsorbance', fontsize=15)
        ax.set_title('spec_info', fontsize=20)
        spec_index = np.linspace(350, 2500, 2151)

        for spec_id,spec_infom in spec.iterrows():
            cata = spec_infom[-1]    #聚类后标签
            spec_infom=spec_infom[:-1]  #光谱信息
            cata_title=["outlier", "normal"]
            if cata==1:
                label=cata_title[0]
                color="b"
            else:
                label=cata_title[1]
                color="b"
            count_list.append(label)
            ax.plot(spec_index, spec_infom,color=color)
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        ax.grid()

        plt.show()


    def print_signel_curve(self,spec,title="spec_info"):
        spec=spec.T
        if isinstance(spec, pd.DataFrame):
            spec_index,spec_info= next(spec.iterrows())
        else:
            spec=pd.DataFrame(spec)
            spec_index, spec_info = next(spec.iterrows())
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        wl = np.linspace(350, 2500, spec.shape[1])
        with plt.style.context(('ggplot')):
            fonts = 6
            plt.figure(figsize=(5.2, 3.1), dpi=200)
            plt.plot(spec_info)
            plt.xlabel('Wavelength (nm)', fontsize=fonts)
            plt.ylabel('reabsorbance', fontsize=fonts)
            plt.title(title, fontsize=fonts)
        return plt
def print_signel_curve(self,spec,title="spec_info"):
    spec=spec.T
    if isinstance(spec, pd.DataFrame):
        spec_index,spec_info= next(spec.iterrows())
    else:
        spec=pd.DataFrame(spec)
        spec_index, spec_info = next(spec.iterrows())
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    wl = np.linspace(350, 2500, spec.shape[1])
    with plt.style.context(('ggplot')):
        fonts = 6
        plt.figure(figsize=(5.2, 3.1), dpi=200)
        plt.plot(spec_info)
        plt.xlabel('Wavelength (nm)', fontsize=fonts)
        plt.ylabel('reabsorbance', fontsize=fonts)
        plt.title(title, fontsize=fonts)
    return plt




df_initial=pd.read_csv(r"F:\xiehui\python_workspace\R_worksapace\spectrum project of zhejiang university\signel_data.csv")
df_initial_name = df_initial["name"]
df_initial = df_initial.drop(["name"], axis=1)
spec_print = printer_spec()

count_list = []
spec_cluster = printer_spec()
spec_cluster.axspectrum(df_initial)


