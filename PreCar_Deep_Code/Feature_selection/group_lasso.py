# author:Lenovo
# datetime:2023/5/4 15:04
# software: PyCharm
# project:pytorch项目


import scipy.io as sio
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold
import utils.tools as utils
#from dimensional_reduction import mutual_mutual
from sklearn.preprocessing import scale,StandardScaler
from dimensional_reduction import Light_lasso

data_=pd.read_csv(r'train_P1.csv')
data=np.array(data_)
data=data[:,1:]

[m1,n1]=np.shape(data)
label1=np.ones((int(m1/2),1))#Value can be changed
label2=np.zeros((int(m1/2),1))
label=np.append(label1,label2)
shu=scale(data)
X=shu
y=label


data_2,importance=Light_lasso(X,y.T.ravel(),0.05)
data_2,importance=Light_lasso(X,y,0.02)
shu=data_2
data_csv = pd.DataFrame(data=shu)
data_csv.to_csv('Group_Lasso.csv')
data_csv = pd.DataFrame(data=importance)
data_csv.to_csv('GL_importance.csv')