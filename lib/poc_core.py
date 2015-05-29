# -*- coding:gb2312 -*-
__author__ = '云絮'
import ConfigParser
import FrameworkPath
import os
import requests
import util.common as common
from time import sleep
class Poc_Core:
    def __init__(self,pocFile):
        self.pocFile=pocFile
    #解析poc文件
    def parsePoc(self):
        try:
            cf=ConfigParser.ConfigParser()
            cf.read(FrameworkPath.poc_dir+os.sep+self.pocFile)
            items=cf.items("exploit")
            pocpath=items[0][1]
            payload=items[1][1]
            res_match=items[2][1]
            requestMethod=items[3][1]
            return pocpath,payload,res_match,requestMethod
        except Exception,e:
            print '解析poc文件失败，请确认内容是否规范:%s'%(e)
    #通过给定的poc和返回正则去执行攻击测试
    def attact(self,url):

        pocpath,payload,res_match,requestMethod=self.parsePoc()
        requestMethod=requestMethod.lower().strip()
        if requestMethod=='post':
            postdata=common.parseUrl(payload)
            r=requests.post(url+'/'+pocpath,data=postdata)
            if r.status_code==200:
                m=common.regex(r.content,res_match)
                if m:
                    for resut in m:
                        common.printPretty('result:'+resut)
                else:
                    common.printPretty('攻击结果抓取失败...将打印所有返回内容...')
                    sleep(1)
                    common.printPretty(r.content)
        elif requestMethod=='get':
            r=requests.get(url+'/'+pocpath+payload)
            if r.status_code==200:
                m=common.regex(r.content,res_match)
                if m:
                    for resut in m:
                        common.printPretty('result:'+resut)
                else:
                    common.printPretty('攻击结果抓取失败...将打印所有返回内容...')
                    sleep(1)
                    common.printPretty(r.content)

