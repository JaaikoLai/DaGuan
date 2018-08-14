#encoding=utf-8
import pandas as pd
import numpy as np
import tensorflow as tf

class DaGuan(object):
    def __init__(self, data_path='./data/'):
        self.raw_train_file = data_path + 'train_set.csv' 
        self.raw_test_file = data_path + 'test_set.csv'
    def processData(self):
        print(self.raw_train_file)
        df = pd.read_csv(self.raw_train_file)
        print(df)
        X_Train = None
        Y_Train = None
        X_Test = None
        Y_Test = None
        return X_Train, Y_Train, X_Test, Y_Test



if __name__ == "__main__":
    d = DaGuan()
    d.processData()
