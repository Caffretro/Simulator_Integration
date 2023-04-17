# # from utilities import *
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#
# import pickle
#
# records = pickle.load(open('dataset.pickle','rb'))
#
# for time in records.keys():
#     for order in records[time]:
#             print(order)
#             sys.exit()
#
#
# pickle.dump(records,open('dataset.pickle','wb'))

# from azureml.opendatasets import NycTlcYellow
#
# from datetime import datetime
# from dateutil import parser
#
#
# end_date = parser.parse('2015-05-31')
# start_date = parser.parse('2015-05-01')
# nyc_tlc = NycTlcYellow(start_date=start_date, end_date=end_date)
#
# nyc_tlc_df = nyc_tlc.to_pandas_dataframe()
#
# nyc_tlc_df.info()
# print(nyc_tlc_df)
# import sys
# 
# import pickle
# data  = pickle.load(open("input/NYU_May.pickle",'rb'))
#
# for date in data.keys():
#     print(data[date])
    # for time in data[date].keys():
    #     print(date,time,data[date][time])
    #     sys.exit()

# a = ['mary','tony','bob']
# b = ['jan','march','may']
# dict_ = {'name':a,'birth':b}
#
#
# pd_data = pd.DataFrame(dict_)
# print(pd_data.columns)
# print(pd_data[pd_data.columns[:2]].values.tolist())
# ret = []
# with open("./10-10.out") as f:
#     lines = f.readlines()
#     for line in lines:
#         if "reward" in line:
#             print(float(line.split(":")[1].strip()))
#             ret.append(float(line.split(":")[1].strip()))
# print(ret)
# plt.plot([i for i in range(len(ret))],ret)
# plt.show()

from matplotlib import pyplot as plt

def get_train_curve(file):
    with open(file,"r") as f:
        lines = f.readlines()
        ret = []
        
        tmp = []
        for line in lines:
            if "reward" in line:
                tmp.append(float(line.split(" ")[-1].strip()))
                if len(tmp) % 5 == 0:
                    print(sum(tmp) / 5)
                    ret.append(sum(tmp) / 5)
                    tmp = []
        
        x = [i for i in range(len(ret))]
        print(len(x),len(ret))
        plt.plot(x,ret,'r+')
        plt.show()



if __name__ == "__main__":
    get_train_curve("1123.txt")