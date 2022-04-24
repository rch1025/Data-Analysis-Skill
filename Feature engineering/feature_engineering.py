#!/usr/bin/env python
# coding: utf-8

# In[2]:
"""df_change1이 안 된 이유는 core(8개)와 분할된 데이터 개수(8개)가 일치해서 [[]]형식이 [] 형식으로 바뀌었기 때문이다."""

import pandas as pd
from tqdm import tqdm

"""함수 정의"""
def df_change(df_index_list, data):
    new_trnd_data = pd.DataFrame()
    for step in df_index_list:
        for idx in tqdm(step):
            #print(idx)
            df = pd.DataFrame({'EQP_NO' : data['EQP_NO'][idx],
                          'TRND_DATE' : data['TRND_DATE'][idx],
                          'time': data['TAG_COMPRS_VAL'][idx][0::2],
                          'TAG_COMPRS_VAL': data['TAG_COMPRS_VAL'][idx][1::2]})
            new_trnd_data = pd.concat([new_trnd_data, df], axis=0)
    return new_trnd_data


# In[ ]
def df_change2(df_index_list, data):
    new_trnd_data = pd.DataFrame()
    for idx in df_index_list:
        df = pd.DataFrame({'EQP_NO' : data['EQP_NO'][idx],
                      'TRND_DATE' : data['TRND_DATE'][idx],
                      'time': data['TAG_COMPRS_VAL'][idx][0::2],
                      'TAG_COMPRS_VAL': data['TAG_COMPRS_VAL'][idx][1::2]})
        new_trnd_data = pd.concat([new_trnd_data, df], axis=0)
    return new_trnd_data