#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

"""a test module """

__author__ = 'Michael Liao'


def func1():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


class Student(object):
    count = 0

    def __init__(self, name, score):
        self.__name = name
        self.score = score
        Student.count += 1

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

if __name__ == '__main__':
    func1()
    print(func1.__code__)
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()
    print(type(bart))
    print(type(bart) == Student)
    print(dir(bart))
    print(bart.__dir__())
    print(Student.count)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
hasattr(obj, "x")
