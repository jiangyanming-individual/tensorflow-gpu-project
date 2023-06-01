# author:Lenovo
# datetime:2023/5/5 17:37
# software: PyCharm
# project:tensorflow-gpu项目

from collections import Counter
import pandas as pd
import readFasta

"""增强分组氨基酸"""
def EGAAC_encode(index_seq,kw):

    """分为5组"""
    group={
        'Aliphatic group':'GAVLMI',
        'Aromatic groups':'FYW',
        'Positively charged groups':'KRH',
        'Negatively charged groups':'DE',
        'No charge group':'STCPNQ'
    }

    groupKeys=group.keys()
    # print(groupKeys)


    encoding=[]
    header=['#']
    for key in groupKeys:
        header.append(key)

    encoding.append(header)


    for index,sequence in zip(index_seq[0],index_seq[1]):

        # print(index,seq)
        ont_code=[]
        name,sequence=index, sequence
        count=Counter(sequence)
        ont_code.append(name)

        groupCount_dict={}
        for key in groupKeys:
            #遍历一组，然后进行计数：
            for aa in group[key]:
                # print(aa)
                groupCount_dict[key]=groupCount_dict.get(key,0)+count[aa]

        # print(groupCount_dict)

        #计算每一组的概率：
        for key in groupKeys:
            ont_code.append(round(groupCount_dict[key] / len(sequence),3))
        # print(ont_code)
        encoding.append(ont_code)

    print("transform over!")
    return encoding


index_seq= readFasta.readfasta('../dataset/train_datasets/train_K1.txt')
kw={'seq_order':'ARNDCQEGHILKMFPSTWYVX'}


res_encode=EGAAC_encode(index_seq,kw)
res=pd.DataFrame(data=res_encode)
res.to_csv('../generate_data/EGAAC_train_k1.csv')