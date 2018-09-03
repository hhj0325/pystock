from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Student(object):
    def __init__(self, name, gender=Gender.Male):
        self.name = name
        self.gender = gender

    def __str__(self) -> str:
        return 'Student object (name: %s)' % self.name

    def __repr__(self) -> str:
        return 'Student object (name: %s)' % self.name

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


if __name__ == '__main__':
    print(Student('Michael'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')

    bart = Student('Bart')
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')

