# author:Lenovo
# datetime:2023/5/4 15:02
# software: PyCharm
# project:pytorch项目


import sys, os, re, platform
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import checkFasta
import readFasta
import numpy as np
import pandas as pd

def AAINDEX(fastas, **kw):

	if checkFasta.checkFasta(fastas) == False:
		print('Error: for "AAINDEX" encoding, the input fasta sequences should be with equal length. \n\n')
		return 0

	AA = 'ARNDCQEGHILKMFPSTWYVX'
	fileAAindex = os.path.split(os.path.realpath(__file__))[0] + r'\data\AAidx_sll.txt' if platform.system() == 'Windows' else sys.path[0] + '\data\AAidx_sll.txt'
	with open(fileAAindex) as f:
		records = f.readlines()[1:]

	AAindex = []
	AAindexName = []
	for i in records:
		AAindex.append(i.rstrip().split()[1:] if i.rstrip() != '' else None)
		AAindexName.append(i.rstrip().split()[0] if i.rstrip() != '' else None)

	index = {}
	for i in range(len(AA)):
		index[AA[i]] = i

	encodings = []
	header = ['#']
	for pos in range(1, len(fastas[0][1]) + 1):
		for idName in AAindexName:
			header.append('SeqPos.' + str(pos) + '.' + idName)
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], i[1]
		code = [name]
		for aa in sequence:
			if aa == '-':
				for j in AAindex:
					code.append(0)
				continue
			for j in AAindex:
				code.append(j[index[aa]]) #(29 * 29)
		encodings.append(code)

	return encodings


fastas = readFasta.readFasta(r"train_P1.txt")
kw=  {'path': r"AAINDEX",'train':r"train_P1.txt",'order':'ARNDCQEGHILKMFPSTWYVX'}
result=AAINDEX(fastas,**kw)

data=np.matrix(result[1:])
data_AAINDEX=pd.DataFrame(data=data[:,1:])
data_AAINDEX.to_csv('train_P1.csv')