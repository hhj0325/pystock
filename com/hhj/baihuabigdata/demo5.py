"""
page 137
"""
from math import log

education = (2.0/12, 5.0/12, 5.0/12)
junior_college = (1.0/2, 1.0/2)
undergraduate = (3.0/5, 2.0/5)
master = (4.0/5, 1.0/5)
date_per = (junior_college, undergraduate, master)


def info_date(p):
    info = 0
    for v in p:
        info += v * log(v, 2)
    return info


def infoA():
    info = 0
    for i in range(len(education)):
        info += -education[i] * info_date(date_per[i])
    return info

print(infoA())
