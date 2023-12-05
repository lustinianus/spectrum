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
        ax.set_title('filter_spec_info', fontsize=20)
        spec_index = np.linspace(350, 2500, 2151)

        for spec_id,spec_infom in spec.iterrows():
            cata = spec_infom[-1]    #聚类后标签
            spec_infom=spec_infom[:-1]  #光谱信息
            cata_title=["outlier", "normal"]
            if cata==1:
                label=cata_title[0]
                color="r"
            else:
                label=cata_title[1]
                color="b"
            count_list.append(label)
            ax.plot(spec_index, spec_infom,label=label,color=color)
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





class prementrarty():
    def __init__(self):
        pass
    def spec_resample(self,spec):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('wavelength', fontsize=15)
        ax.set_ylabel('reabsorbance', fontsize=15)
        ax.set_title('filter_spec_info', fontsize=20)
        df_spec_re=pd.DataFrame()
        for spec_id, spec_infom in spec.iterrows():
            spec_infom = spec_infom[:-1]                     #spec_info 包含label
            spec_sign_re = signal.resample(spec_infom, 250)
            df_spec_re=pd.concat([df_spec_re,pd.Series(spec_sign_re)],axis=1)
            xre = np.linspace(350, 2500, len(spec_sign_re), endpoint=False)
            # ax.scatter(xre, spec_sign_re)                       #全部子图
        # plt.show()
        return spec_sign_re,xre,df_spec_re

    def spec_log(self,spec_info):
        spec_log=-np.log10(spec_info)
        xre = np.linspace(350, 2500, len(spec_log), endpoint=False)

        return spec_log



    def D1(self, sdata):
        """
        一阶差分
        """
        sdata = deepcopy(sdata).T
        if isinstance(sdata, pd.DataFrame):
            sdata = sdata.values
        temp1 = pd.DataFrame(sdata)
        temp2 = temp1.diff(1,axis=0)/10
        # print(temp2)    # 差分后
        temp3 = temp2.values
        return np.delete(temp3, 0, axis=0)


# def printer_spectrum(spec,):





if __name__=="__main__":
    df_initial=pd.read_csv(r"F:\xiehui\python_workspace\R_worksapace\spectrum project of zhejiang university\signel_data.csv")
    df_initial_name=df_initial["name"]
    df_initial=df_initial.drop(["name"],axis=1)
    print(df_initial.head(5))       #查看数据

    spec_print = printer_spec()   #绘图实例化

    count_list = []    #统计outlier数量 及绘图 聚类结果展示
    spec_cluster=printer_spec()
    spec_cluster.axspectrum(df_initial)
    # print(Counter(count_list))


    df_initial.drop(df_initial[df_initial.label == 1].index, inplace=True)   #去除异常值



    spec_pre=prementrarty()       #前处理测试
    examy,exam_x,df_spec_re=spec_pre.spec_resample(df_initial)   #重采样
    # plt.figure(figsize=(5.2, 3.1), dpi=200)
    # plt.scatter(exam_x, examy)
    # plt.show()


    df_spec_log=spec_pre.spec_log(df_spec_re)      #对数变化



    spec_res_sg = sg(x=df_spec_log.T, window_length=15, polyorder=2)   #savitzky-golay   注意转置
    output=pd.DataFrame(spec_res_sg)

    # output.to_csv(r"F:\xiehui\python_workspace\R_worksapace\spectrum project of zhejiang university\spec_res_sg.csv")
    spec_D1 = spec_pre.D1(spec_res_sg)



    spec_print.print_signel_curve(df_initial.T,title="df_initial").show()
    spec_print.print_signel_curve(df_spec_re,title="resample").show()
    spec_print.print_signel_curve(df_spec_log,title="log").show()
    spec_print.print_signel_curve(spec_res_sg.T, title="res_sg").show()
    spec_print.print_signel_curve(spec_D1,title="D1").show()


    print(pd.DataFrame(spec_D1).head(5))
    print("df_ini",pd.DataFrame(df_initial).shape,df_initial.head(5))
    print("resample",pd.DataFrame(df_spec_re).shape,pd.DataFrame(df_spec_re).head(5))
    print("log", pd.DataFrame(df_spec_log).shape,pd.DataFrame(df_spec_log).head(5))
    print("res_sg",output.shape,output.head(5))
    print("spec_d1",pd.DataFrame(spec_D1).shape,pd.DataFrame(spec_D1).head(5))




