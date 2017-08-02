
from com.hhj.pystock.ml.csvReader import loadCsv
from com.hhj.pystock.ml.splitDataset import splitDataset

splitRatio = 0.67
filename = 'share.csv'
dataset = loadCsv(filename)
print('Loaded data file %s with %d rows' % (str(filename), len(dataset)))
train, test = splitDataset(dataset, splitRatio)
print('Split %d rows into train with %s and test with %s' % (len(dataset), train, test))