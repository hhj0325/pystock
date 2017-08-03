
from com.hhj.pystock.ml.csvReader import load_csv
from com.hhj.pystock.ml.predict import get_predictions, get_accuracy
from com.hhj.pystock.ml.splitDataset import split_data_set
from com.hhj.pystock.ml.summarize import summarize_by_class

split_ratio = 0.8
file_name = 'share.csv'
# 从csv文件中获取数据集
data_set = load_csv(file_name)
print('Loaded data file %s with %d rows' % (str(file_name), len(data_set)))

# 将数据集切割为训练集和测试集
train, test = split_data_set(data_set, split_ratio)
print('Split %d rows into train = %d and test = %d ' % (len(data_set), len(train), len(test)))

# 训练集，按照是否换病，计算每个属性的期望、方差
summarize = summarize_by_class(train)
print('Summary by class value: %s' % summarize)

# 计算每个数据的归属区间
t_predictions = get_predictions(summarize, test)
print('Predictions: %s' % t_predictions)

# 计算出的数据和原始数据比较，验证成果正确率
t_accuracy = get_accuracy(test, t_predictions)
print('Accuracy: %f' % t_accuracy)


