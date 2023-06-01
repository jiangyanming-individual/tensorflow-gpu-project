
# author:Lenovo
# datetime:2023/5/5 15:40
# software: PyCharm
# project:tensorflow-gpu项目


def AAindex_encode(samples):

    with open('./AAindex/AAindex_normalized.txt',mode='r') as f:
        records=f.readlines()[1:]
        f.close()

    AA='ARNDCQEGHILKMFPSTWYV'

    AAindex_names=[]
    AAindex=[]

    for i in records:
        # print(i.rstrip().split()[0])  #得到AAindex的names
        AAindex_names.append(i.rstrip().split()[0] if i.rstrip()!='' else None)
        AAindex.append(i.rstrip().split()[1:] if i.rstrip()!='' else None)


    #前29种物理化学性质：props是一个列表：
    props = 'FINA910104:LEVM760101:JACR890101:ZIMJ680104:RADA880108:JANJ780101:CHOC760102:NADH010102:KYTJ820101:NAKH900110:GUYH850101:EISD860102:HUTJ700103:OLSK800101:JURD980101:FAUJ830101:OOBM770101:GARJ730101:ROSM880102:RICJ880113:KIDA850101:KLEP840101:FASG760103:WILM950103:WOLS870103:COWR900101:KRIW790101:AURR980116:NAKH920108'.split(':')

    if props:
        tempAAindex_names=[]
        tempAAindex=[]

        for p in props:
            #如果29种的一种存在
            if AAindex_names.index(p) !=-1:
                tempAAindex_names.append(p)
                tempAAindex.append(AAindex[AAindex_names.index(p)])

        #如果找到了，就将前29种的性质直接替代AAindx；
        if len(tempAAindex_names)!=0:
            AAindex_names=tempAAindex_names
            AAindex=tempAAindex

    # print(AAindex)
    # print(len(AAindex))

    #20种氨基酸序列的字典： ARNDCQEGHILKMFPSTWYV (0-19)
    seq_index={}
    for i in range(len(AA)):
        seq_index[AA[i]]=i

    AAindex_encodings=[]
    for i in samples:
        name,sequence,label=i[0],i[1],i[2]
        code=[name,label]

        for aa in sequence:#一条氨基酸序列；
            if aa == '-':
                for aaindex in AAindex: #29个AAindex全部为0
                    code.append(0)
            for aaindex in AAindex:
                code.append(aaindex[seq_index.get(aa)])#添加存在的aaindex;

        AAindex_encodings.append(code)
    return AAindex_encodings

AAindex_encode() #需要传入序列：(name,seq,label)

