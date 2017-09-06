__author__ = 'yg.jang'

import sys

"""
THis si the "nester.py" module and it provides one function called print_lol()
which prints lists that may or may not include nested lists.
"""


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    """----------------------------------------------------------------------
     This function takes one positional argument calloed "the_list", which
    is any Python list (of - possibly - nested lists). Each date item in the
    provided list is (recursively) printed to the screeen on it's own line.
    - add indent printable function
    - add select indent or not indent using 'indent' Flag
    - 출력대상을 지정할 수 있는 인자값 추가

    :param the_list: 문자열 리스트
    :param indent: 들여쓰기 사용여부
    :param level: 들여쓰기 초기 Tab 값
    :param out: 출력대상
    :return:
    ----------------------------------------------------------------------"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)
