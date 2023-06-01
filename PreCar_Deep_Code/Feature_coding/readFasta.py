# author:Lenovo
# datetime:2023/5/5 11:54
# software: PyCharm
# project:tensorflow-gpu项目


"""
读取fasta文件
返回值: indexList seqList
"""
def readfasta(filapath):

    f=open(file=filapath,mode='r')
    lines=f.readlines()
    f.close()


    indexList=[]
    seqList=[]

    tempSeq=""

    for line in lines:

        if '>' in line:
            #读取的是第一列序列：
            indexList.append(line[1:].strip())
            seqList.append(tempSeq.strip()) #第一次加入空字符串；
            tempSeq=""
        else:
            #读取的是真正的字符串
            tempSeq+=line.strip()

    seqList.append(tempSeq.strip()) #将最后的一个序列加入；

    del seqList[0] #删除第一个空的字符串
    return indexList,seqList


# indexList,seqList=readfasta('../dataset/train_datasets/train_K1.txt')
# print(len(indexList))
# print(len(seqList))
# print(indexList)
# print(seqList)



