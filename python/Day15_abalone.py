#!/usr/bin/env python
# coding: utf-8

# #### UCI 전복
# https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data
# 
# 1. [함수] requests 패키지를 이용해 데이터 가져와서 ndarray로 변환.
# 
# 2. [함수] 성별이 'M'인 데이터를 필터, Length 와 Diameter 간 상관도를 반환
# 
# 3. __name__ 값이 __main__이면, 1,2 함수를 실행, 2번함수의 반환값을 프린트.

# In[30]:


import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.set_printoptions(precision=5, suppress=True)


# In[31]:


def read_data():
    raw_data=[]
    x = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
    for line in x.text.split('\n'):
        raw_data.append(line.split(','))

    raw_data = raw_data[:-1]
    np_data = np.array(raw_data)
    return np_data

def get_corr(np_data):
    filter1 = np_data[:, 0] == 'M'
    length_list = np_data[filter1][:, 1].astype(np.float64)
    diameter_list = np_data[filter1][:, 2].astype(np.float64)

    return np.corrcoef(length_list, diameter_list)


# In[32]:

if __name__ == '__main__':
	d = read_data()
	out = get_corr(d)
	print(out)

