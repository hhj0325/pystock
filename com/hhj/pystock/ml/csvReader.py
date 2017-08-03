import csv


def load_csv(filename):
    """
    csv文件读取
    :param filename:
    :return:
    """
    lines = csv.reader(open(filename, "rt"))
    data_set = list(lines)
    for i in range(len(data_set)):
        data_set[i] = [float(x) for x in data_set[i]]
    return data_set
