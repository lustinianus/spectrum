import os
from pykrige.ok import OrdinaryKriging
import numpy as np
from matplotlib import pyplot as plt
from osgeo import gdal
from gma.algorithm.spmis.interpolate import *
import geopandas
from math import radians, sin, cos, asin, sqrt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import gma
import fiona
from shapely.geometry import Polygon, Point
from scipy.interpolate import Rbf#引入径向基函数
import pandas as pd
from gma.map import plot
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.colors as cor





def strong_layering(img, layer):
    """
    强分层法
    :param img: 输入灰度图像
    :param layer: 灰度级数分层数
    :return:伪彩色增强图像(ndim=2)
    """
    w, h = img.shape[:2]
    img_color = np.zeros((w, h), dtype=np.uint8)

    for row in range(w):
        for col in range(h):
            interval = 256 // layer  # 分层的灰度级数间隔
            I_layer = img[row][col] // interval  # 像素所在层数(0-layer)
            img_color[row][col] = I_layer * interval

    return img_color



