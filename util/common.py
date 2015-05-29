# -*- coding:gb2312 -*-
__author__ = '云絮'
import os
import re
'''
    通用部分
'''
#解析post请求，将key=value的形式转换为{key:value}的字典类型
def parseUrl(posturl):
    dict={}
    s=posturl.split('&')
    for re1 in s:
        dit=re1.split('=')
        dict[dit[0]]=dit[1]
    return dict
#正则匹配，返回匹配结果的列表
def regex(text,pattern):
    r=re.compile(pattern)
    result=r.findall(text)
    return result
#字符串打印模板
def printPretty(str1):
    print '[*]'+'='*39
    print '[*]'+str1
    print '[*]'+'='*39