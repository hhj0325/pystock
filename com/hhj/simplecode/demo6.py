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
    """
    afasfasdf
    """
    __slots__ = ('__name', 'score')
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
    print(bart.__doc__)
    print(Student.count)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
hasattr(obj, "x")


class Screen(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)


