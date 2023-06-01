
"""
氨基酸组成：
"""
import re,os,sys,csv
from collections import Counter
import pandas as pd
import readFasta

#AA = 'ARNDCQEGHILKMFPSTWYV'
def AAC(fastas, **kw):

	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
	encodings = []
	header = ['#']
	for i in AA:
		header.append(i) #(#,A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,Y,V)
	encodings.append(header)

	# print(fastas)
	for index,seq in zip(fastas[0],fastas[1]):
		# name, sequence = i[0], re.sub('-', '', i[1])
		name,sequence=index,seq
		# print(name)
		# print(sequence)
		# break
		code=[]
		count = Counter(sequence)
		for key in count:
			count[key] = round(count[key] / len(sequence),3)

		code.append(name)
		for aa in AA:
			code.append(count[aa])
		encodings.append(code)

	# print(encodings)
	return encodings

fastas = readFasta.readfasta('../dataset/train_datasets/train_K1.txt')
kw=  {'path': r"AAC",'train':r"train_P1.txt",'order':'ARNDCQEGHILKMFPSTWYVX'}
data_AAC=AAC(fastas, **kw)

#转为pandas
AAC=pd.DataFrame(data=data_AAC)
AAC.to_csv('../generate_data/AAC_train_K1.csv')
