import random


def split_data_set(data_set, split_ratio):
    """
    分割为训练集和测试集
    :param data_set:
    :param split_ratio:
    :return:
    """
    train_size = int(len(data_set) * split_ratio)
    train_set = []
    copy = list(data_set)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy.pop(index))
    return [train_set, copy]


def separate_by_class(data_set):
    separated = {}
    for i in range(len(data_set)):
        vector = data_set[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated
