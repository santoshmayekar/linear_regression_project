import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter
from q03_linear_regression.build import linear_regression


def linear_predictor(linear_model, X, y):
    '''Enter Code Here'''
    return y_pred, mse, mae, r2