import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def from_1_to_100(n=False):
    l1 = []
    l2 = []
    for i in range(101):
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    if n:
        print("Парні числа: {}".format(l1))
    else:
        print("HeПарні числа: {}".format(l2))
