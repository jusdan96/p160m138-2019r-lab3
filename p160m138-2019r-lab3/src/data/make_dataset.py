import sys
import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd

if len(sys.argv) == 4:
    DataFilePath = sys.argv[1]
    DataOutputPath = sys.argv[2]
    testDataSplit = float(sys.argv[3])
else:
    path = 'data/raw/'
    fileName = 'bank-full.csv'
    currentPath = os.path.dirname(os.path.realpath("."))
    DataFilePath = f'{currentPath}/../{path}{fileName}'
    DataOutputPath = f'{currentPath}/../data/interim'
    testDataSplit = 0.15

file = open(DataFilePath, 'r')
lines = file.readlines()

firstLine = True
values = {}
labels = []
for line in lines:
    splitValues = line.split(';')
    if firstLine:
        for splitValue in splitValues:
            splitValue = splitValue.replace('"', '').replace('\n', '')
            labels.append(splitValue)
            values[splitValue] = []
        firstLine = False
    else:
        for index, splitValue in enumerate(splitValues):
            splitValue = splitValue.replace('"', '').replace('\n', '')
            values[labels[index]].append(splitValue)


df = pd.DataFrame(data=values)

le = preprocessing.LabelEncoder()
df['target'] = (preprocessing.LabelEncoder().fit_transform(df['y']))

train, test = train_test_split(df, test_size=testDataSplit,stratify=df['target'])
train.to_csv(f'{DataOutputPath}/train.csv')
test.to_csv(f'{DataOutputPath}/test.csv')

