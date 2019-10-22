import csv,os

BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 获取项目路径
CASEPATH = os.path.join(BASEPATH,'case')    # 获取测试用例文件目录路径
DRIVERPATH = os.path.join(BASEPATH,'driver')    # 获取浏览器驱动目录路径


REPORTPATH = os.path.join(BASEPATH,'report')    # 获取测试报告文件目录路径
DATAPATH = os.path.join(BASEPATH,'data')     # 获取测试数据文件目录路径

