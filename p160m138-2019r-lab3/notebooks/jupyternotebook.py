import os
import pandas as pd
from plotnine import *
path = '/data/raw/'
fileName = 'bank-full.csv'
currentPath = os.path.dirname(os.path.realpath("."))
file = open(f'{currentPath}{path}{fileName}', 'r')
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
for label in labels:
    plot = (ggplot(df, aes(x=label)) + geom_histogram() + ggtitle("Histogram of " + label))
    fileName = f"Histogram_{label}"
    ggsave(plot, filename=fileName, path=currentPath)
    
df.describe()
