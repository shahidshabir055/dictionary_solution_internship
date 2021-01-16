# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:45:25 2021

@author: eshah
"""
import datetime 
import calendar 
from collections import defaultdict
def solution(day_dict):
    dd=[]
    vl=list(day_dict.values())
    for date in list(day_dict):
        Day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        Day=calendar.day_name[Day]
        dd.append(Day)
    temp = defaultdict(list)
    for dd, vl in zip(dd, vl):
        temp[dd].append(vl)
    Result = {key: sum(values) for key, values in temp.items()}
    key_order = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
    def_dict = {'Monday':0 , 'Tuesday':0 , 'Wednesday':0 , 'Thursday':0, 'Friday':0, 'Saturday':0 , 'Sunday':0}
    Result =dict(sorted(Result.items(), key=lambda i:key_order.index(i[0])))
    for key in def_dict:
        if not key in Result:
            ind = list(def_dict.keys()).index(key)
            val = ((list(Result.values())[ind-1]+ list(Result.values())[ind]))//2
            Result[key] = val
            Result =dict(sorted(Result.items(), key=lambda i:key_order.index(i[0])))  
    return Result
#day_dict= {'2020-01-01':4, '2020-01-02': 4, '2020-01-03': 6, '2020-01-04': 8, '2020-01-05': 2,
#         '2020-01-06': -6, '2020-01-07': 2, '2020-01-08': -2}
"""
Expected output:
{'Monday': -6, 'Tuesday': 2, 'Wednesday': 2, 'Thursday': 4, 'Friday': 6, 'Saturday': 8, 'Sunday': 2}

"""
day_dict={'2020-01-01':6, '2020-01-04': 12,'2020-01-05': 14,'2020-01-06': 2, '2020-01-07':4}
print(solution(day_dict)) 
