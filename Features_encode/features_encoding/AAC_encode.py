# author:Lenovo
# datetime:2023/5/5 15:15
# software: PyCharm
# project:tensorflow-gpu项目




from collections import Counter
import pandas as pd
import readFasta

#Sequence = 'ARNDCQEGHILKMFPSTWYV'
def AAC_encode(index_seq,kw):

    if kw['seq_order']!=None:
        AA=kw['seq_order']
    else:
        AA='ACDEFGHIKLMNPQRSTVWY'

    encodings = []
    header=['#']
    for i in AA:
        header.append(i)
    encodings.append(header)

    for index,sequence in zip(index_seq[0],index_seq[1]):

        one_code=[]
        name,sequence=index,sequence
        # print(name)
        # print(seq)
        # break;
        count=Counter(sequence)
        # print(count)
        for key in count:
            #计算概率
            count[key]=round(count[key] / len(sequence),3)
        one_code.append(name)
        for key in AA:
            one_code.append(count[key])
        encodings.append(one_code)
    print("转换over!")
    return encodings


index_seq= readFasta.readfasta('../dataset/train_datasets/train_K1.txt')
kw={'seq_order':'ARNDCQEGHILKMFPSTWYVX'}
res_encode=AAC_encode(index_seq,kw)

#转成csv格式：
res_data=pd.DataFrame(data=res_encode)
res_data.to_csv('../generate_data/AAC_train_K1.csv')