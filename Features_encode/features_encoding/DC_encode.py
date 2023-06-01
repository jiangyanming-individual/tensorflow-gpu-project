# author:Lenovo
# datetime:2023/5/7 11:30
# software: PyCharm
# project:tensorflow-gpu项目


"""二肽编码"""

from collections import Counter
import pandas as pd
import readFasta


"""含有未知的氨基酸 设置为X"""
def DC_encode(index_seq,kw):

    AA = 'ACDEFGHIKLMNPQRSTVWY'

    DC_list=[]
    for i in range(len(AA)):
        for j in range(len(AA)):
            DC_list.append(AA[i]+AA[j])
    # print(DC_list)
    encoding=[]
    header=['#']
    for dc in DC_list:
        header.append(dc)
    encoding.append(header)

    #生成氨基酸对应字典：
    index_dict={}
    for i in range(len(AA)):
        index_dict[AA[i]] = i
    # print(index_dict)

    for index,sequence in zip(index_seq[0],index_seq[1]):
        name,sequence=index,sequence
        one_code=[name]
        tempCode=[0] * 400 #400维的向量：
        for i in range(len(sequence) -1):
            if sequence[i]  == 'X' or sequence[len(sequence)-1] == 'X':
                continue
            else:
                #统计二肽出现的次数;出现一次加1；
                tempCode[index_dict[sequence[i]] * 20 + index_dict[sequence[i+1]]]=tempCode[index_dict[sequence[i]] * 20 + index_dict[sequence[i+1]]] +1
        #计算一个二肽的概率：
        if sum(tempCode) !=0:
            tempCode = [round(j / sum(tempCode),3) for j in tempCode]

        one_code=one_code+tempCode

        encoding.append(one_code)
    print("transform over!")
    return encoding


index_seq= readFasta.readfasta('../dataset/train_datasets/train_K1.txt')
kw={'seq_order':'ARNDCQEGHILKMFPSTWYVX'}
res_encode=DC_encode(index_seq,kw)
res=pd.DataFrame(data=res_encode)
res.to_csv('../generate_data/DC_train_k1.csv')