import math


def calculate_probability(x, mean, st_dev):
    """
    计算正态分布概率
    :param x:
    :param mean:
    :param st_dev:
    :return:
    """
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(st_dev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * st_dev)) * exponent


def calculate_class_probabilities(summaries, input_vector):
    """
    计算属性归属不同区间的概率
    :param summaries:
    :param input_vector:
    :return:
    """
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            # 获取平均值和标准差
            mean, st_dev = classSummaries[i]
            x = input_vector[i]
            # 多个属性概率相乘（核心）
            probabilities[classValue] *= calculate_probability(x, mean, st_dev)
    return probabilities

#  测试方法
# t_x = 1
# t_mean = 1
# t_st_dev = 0.6
# probability = calculate_probability(t_x, t_mean, t_st_dev)
# print('Probability of belonging to this class: %f' % probability)
#
# t_summaries = {0: [(1, 0.5)], 1: [(2, 1)]}
# t_input_vector = [1.1, '?']
# t_probabilities = calculate_class_probabilities(t_summaries, t_input_vector)
# print('Probabilities for each class: %s ' % t_probabilities)
