def predict(summaries, input_vector):
    """
    单一预测
    :param summaries:
    :param input_vector:
    :return:
    """
    from com.hhj.pystock.ml.probability import calculate_class_probabilities
    probabilities = calculate_class_probabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for classValue, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = classValue
    return best_label


def get_predictions(summaries, test_set):
    """
    多重预测
    :param summaries:
    :param test_set:
    :return:
    """
    predictions = []
    for i in range(len(test_set)):
        result = predict(summaries, test_set[i])
        predictions.append(result)
    return predictions


def get_accuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(test_set))) * 100.0


#  测试方法
# t_summaries = {'A': [(1, 0.5), (2, 0.5)], 'B': [(20, 5.0), (2, 0.5)]}
# t_input_vector = [19.1, 3]
# t_result = predict(t_summaries, t_input_vector)
# print('Prediction: %s' % t_result)

# t_summaries = {'A': [(1, 0.5)], 'B': [(20, 5.0)]}
# t_testSet = [[1, '?'], [4, '?']]
# t_predictions = get_predictions(t_summaries, t_testSet)
# print('Predictions: %s' % t_predictions)

# t_testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
# t_predictions = ['a', 'a', 'a']
# t_accuracy = get_accuracy(t_testSet, t_predictions)
# print('Accuracy: %f' % t_accuracy)

