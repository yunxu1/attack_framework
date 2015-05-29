# -*- coding:gb2312 -*-
__author__ = '云絮'
import util.FileUtil as fileUtil
import lib.poc_core as pocCore
import argparse
import sys
import os
import lib.plugin_core as pluginCore


pluginObj=pluginCore.pluginCore()
def get_args():
    p=argparse.ArgumentParser()
    p.add_argument('-host',metavar='',help='指定目标域名或IP')
    p.add_argument('-exp',metavar='',help='指定一个exploit利用模块,查看exp列表输入exp=list')
    p.add_argument('-script',metavar='',help='选择一个插件使用,查看插件列表输入script=list')
    arguments=p.parse_args()
    return arguments
def parse_args():
    global pluginObj
    args=get_args()
    script=args.script
    exp=args.exp
    host=args.host
    if script=='list':
        pluginObj.showPluginList()
        print '[#]usage：'+os.path.basename(__file__)+' -script scriptName'
        sys.exit()
    if exp=='list':
        fileUtil.showPocFileList()
        print '[#]usage：'+os.path.basename(__file__)+' -host http://localhost/ -exp cmsexp.poc'
        sys.exit()
    if host!=None and exp!=None:
        executeExp(host,exp)
    if script!=None:
        use_script(script,host)

#用户选择使用插件
def use_script(scriptName,host=None):
    global pluginObj
    pluginObj.usePlugin(scriptName,host)
#执行用户选择的exp
def executeExp(host,pocfile):
    a=pocCore.Poc_Core(pocfile)
    a.attact(host)
if __name__ == '__main__':
    parse_args()