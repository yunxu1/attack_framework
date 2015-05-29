# -*- coding:gb2312 -*-
__author__ = '云絮'
import os
import FrameworkPath
'''
    用于文件处理
'''

def getPocFileList():
    uri=FrameworkPath.poc_dir
    return os.listdir(uri)
#显示poc文件列表
def showPocFileList():
    filelist=getPocFileList()
    print '*'*15+'请选择exploit模块'+'*'*15
    for pocfile in filelist:
        print '[*]'+pocfile


