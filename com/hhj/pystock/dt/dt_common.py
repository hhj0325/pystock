import math


def get_shanno_entropy(values):
    """
    根据给定列表中的值计算其Shanno Entropy
    """
    uniq_vals = set(values)
    val_nums = {key: values.count(key) for key in uniq_vals}
    probs = [v / len(values) for k, v in val_nums.items()]
    entropy = sum([-prob * math.log2(prob) for prob in probs])
    return entropy


def choose_best_split_feature(self, dataset, classes):
    """
    根据信息增益确定最好的划分数据的特征
    :param self:
    :param dataset: 待划分的数据集
    :param classes: 数据集对应的类型
    :return: 划分数据的增益最大的属性索引
    """
    base_entropy = self.get_shanno_entropy(classes)
    feat_num = len(dataset[0])
    entropy_gains = []
    for i in range(feat_num):
        splited_dict = self.split_dataset(dataset, classes, i)
        new_entropy = sum([
            len(sub_classes) / len(classes) * self.get_shanno_entropy(sub_classes)
            for _, (_, sub_classes) in splited_dict.items()
        ])
        entropy_gains.append(base_entropy - new_entropy)
    return entropy_gains.index(max(entropy_gains))
