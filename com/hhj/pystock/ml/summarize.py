import math


def mean(numbers):
    """
    计算平均值
    :param numbers:
    :return:
   """
    return sum(numbers) / float(len(numbers))


def st_dev(numbers):
    """
    计算标准方差
    :param numbers:
    :return:
    """
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


def summarize(data_set):
    """
    计算属性平均值、标准方差
    :param data_set:
    :return:
    """
    summaries = [(mean(attribute), st_dev(attribute)) for attribute in zip(*data_set)]
    del summaries[-1]
    return summaries


def summarize_by_class(data_set):
    """
    计算数据类的平均值和标准方差
    :param data_set:
    :return:
    """
    from com.hhj.pystock.ml.splitDataset import separate_by_class
    separated = separate_by_class(data_set)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries


# 测试方法
# t_numbers = [1, 2, 3, 4, 5]
# print('Summary of %s: mean= %f, st_dev= %f' % (t_numbers, mean(t_numbers), st_dev(t_numbers)))
#
# t_data_set = [[1, 20, 1], [2, 21, 1], [3, 22, 1]]
# summary = summarize(t_data_set)
# print('Attribute summaries: %s' % summary)
#
# t_data_set_2 = [[1, 20, 1], [2, 21, 0], [3, 22, 1], [4, 22, 0]]
# summary = summarize_by_class(t_data_set_2)
# print('Summary by class value: %s' % summary)
