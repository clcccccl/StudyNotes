#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pdb
import datetime
import traceback


def exceptions_note():
    '''
    异常处理
    '''
    try:
        a = 1 / 0
    except:
        error_info = sys.exc_info()
        pdb.set_trace()
        # 异常栈跟踪
        print traceback.format_exc()
        # 异常关键信息
        print str(error_info[1])
    else:
        # 无异常时调用
        pass
    finally:
        # 最终执行
        pass


def log_note():
    '''
    日志
    '''
    pass


def str_note():
    '''\
    字符串
    '''
    # 转义 "\"
    print '\'\n\\'
    print r'\'\n\\'
    print u'Hello\\u0020World !'
    print ur'Hello\\u0020World !'
    # Unicode -> utf-8
    print u"盲枚眉".encode('utf-8')
    # utf-8 -> Unicode 不给第二参数为ascii
    print unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')


def type_note(value):
    '''
    变量类型
    '''
    # type(None) == 'NoneType'
    print type(value)
    if isinstance(value, str):
        print 'str'
    # bool形变量也是int形～～～
    elif isinstance(value, int):
        print 'int'
    elif isinstance(value, long):
        print 'long'
    elif isinstance(value, float):
        print 'float'
    elif isinstance(value, bool):
        print 'bool'
    elif isinstance(value, unicode):
        print 'unicode'
    elif isinstance(value, datetime.datetime):
        print 'datetime.datetime'
    else:
        print 'other type'


def list_note():
    '''
    链表
    '''
    list_1 = [1, 2]
    list_2 = [2, 3, 4]
    value = 2
    # 添加元素至末尾 可存在相同元素
    list_1.append(value)  # [1, 2, 2]
    # 添加list_2至list_1末尾 作为一个元素
    list_1.append(list_2)  # [1, 2, 2, [2, 3, 4]]
    # 将list_2链接到list_1后
    list_1.extend(list_2) == list_1 + list_2  # [1, 2, 2, [2, 3, 4], 2, 3, 4]
    # 指定位置插入元素 位置过大添加至末尾
    value_2 = 'asd'
    list_1.insert(100, value_2)  # [1, 2, 2, [2, 3, 4], 2, 3, 4, 'asd']
    # 删除list_1中指定值的第一个元素
    list_1.remove(2)  # [1, 2, [2, 3, 4], 2, 3, 4, 'asd']
    # 从链表的指定位置删除元素，并将其返回。如果没有指定索引，返回最后一个元素。
    list_1.pop()  # asd
    list_1.pop(2)  # [2, 3, 4]
    # 删除片段
    del list_1[2:4]
    # 删除变量
    del list_1
    # 指定值的索引
    list_1.index(3)  # 3
    list_1.count(2)  # 2
    list_1.insert(0, 'asd')
    print list_1
    # 把链表当作队列使用
    from collections import deque
    queue = deque(list_1)
    # 队列加入元素
    queue.append("Terry")  # deque(['asd', 4, 3, 2, 2, 1, 'Terry'])
    # 队列先进先出
    print queue.popleft()  # asd
    print queue  # deque([4, 3, 2, 2, 1, 'Terry'])
    # 栈
    list_1.append('top')
    list_1.pop()

    # 就地排序
    list_1.sort(cmp=None, key=None, reverse=False)  # [1, 2, 2, 3, 4, 'asd']
    # 就地倒排链表中的元素
    list_1.reverse()  # ['asd', 4, 3, 2, 2, 1]
    # list map 排序
    records.sort(key=lambda map: map[key], reverse=True)
    # list过滤
    list_3 = [row for row in list_1 if row > 1]

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]


def time_note():
    '''
    时间操作
    '''
    # 获取现在的时间 同datetime.datetime.today()
    now = datetime.datetime.now()
    # 获取一段时间后的时间
    date_1 = now - datetime.timedelta(days=1, hours=2, minutes=3, seconds=4.4)
    # 年 月 日 。。。
    [now.year, now.month, now.day, now.hour, now.minute, now.second]
    # 两个时间相差天数
    (now - date_1).days
    pass


def main():
    exceptions_note()
    pass

if __name__ == '__main__':
    main()
    pass
