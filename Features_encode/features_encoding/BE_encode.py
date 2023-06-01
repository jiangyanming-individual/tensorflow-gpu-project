# author:Lenovo
# datetime:2023/5/8 17:26
# software: PyCharm
# project:tensorflow-gpu项目





"""二进制编码"""

from collections import Counter
import pandas as pd
import readFasta

def BE_encode(index_seq,kw):


    if kw['seq_order'] !=None:
        AA=kw['seq_order']
    else:
        AA='ACDEFGHIKLMNPQRSTVWYX'

    encoding=[]
    header=['#']
    for i in range(27):
        header.append(i)
    encoding.append(header)

    for index,sequence in zip(index_seq[0],index_seq[1]):

        name,sequence=index,sequence
        one_code=[name]
        for i in sequence:
            vector=[0] * 21
            vector[AA.index(i)]=1

            one_code.append(vector)
        encoding.append(one_code)
    print("transform over!")
    return encoding



index_seq= readFasta.readfasta('../dataset/train_datasets/train_K1.txt')
kw={'seq_order':'ARNDCQEGHILKMFPSTWYVX'}

res_code=BE_encode(index_seq,kw)
res=pd.DataFrame(data=res_code)
res.to_csv('../generate_data/BE_train_k1.csv')

