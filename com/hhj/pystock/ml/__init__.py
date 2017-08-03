"""
关于朴素贝叶斯
朴素贝叶斯算法是一个直观的方法，使用每个属性归属于某个类的概率来做预测。你可以使用这种监督性学习方法，对一个预测性建模问题进行概率建模。
给定一个类，朴素贝叶斯假设每个属性归属于此类的概率独立于其余所有属性，从而简化了概率的计算。这种强假定产生了一个快速、有效的方法。
给定一个属性值，其属于某个类的概率叫做条件概率。对于一个给定的类值，将每个属性的条件概率相乘，便得到一个数据样本属于某个类的概率。
我们可以通过计算样本归属于每个类的概率，然后选择具有最高概率的类来做预测。
通常，我们使用分类数据来描述朴素贝叶斯，因为这样容易通过比率来描述、计算。一个符合我们目的、比较有用的算法需要支持数值属性，同时假设每一个数值属性服从正态分布(分布在一个钟形曲线上)，这又是一个强假设，但是依然能够给出一个健壮的结果。

样本属性的意义
1. Number of times pregnant
2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3. Diastolic blood pressure (mm Hg)
4. Triceps skin fold thickness (mm)
5. 2-Hour serum insulin (mu U/ml)
6. Body mass index (weight in kg/(height in m)^2)
7. Diabetes pedigree function
8. Age (years)
9. Class variable (0 or 1)
"""