#coding:gb2312
import os
import sys
from interface.iPlugin import Plugin
pwdlist=[]
sys.path.append('../')
wpath=os.path.dirname(__file__)
filepath=os.path.join(wpath,'file')
__all__ = ["fuzzerPwd"]
class fuzzerPwd(Plugin):
    """ 定义一个接口，其他 插件必须实现这个接口，name 属性必须赋值 """
    name = 'fuzzerPwd'
    description = '一个Fuzzer常用密码的神器'
    version = '0.0.1'
    
    def __init__(self):
        Plugin.__init__(self)
    
    #获取Fuzzer密码的模板，每行为一条放进pwdlist列表中
    def getPwdTemplat(self):
        fr=open(filepath+os.sep+'pwd.yx','r')
        while 1:
            line=fr.readline().strip()
            if not line:
                break
            pwdlist.append(line)

        fr.close()
    #输出最后的字典结果到当前目录下的password.txt文件
    def outputDicFile(self,fuzzerPwdList):
        f=open(filepath+os.sep+'password.txt','w')
        for pwd in fuzzerPwdList:
           f.write(pwd+'\n')
        f.close()
    def execute(self,args):
        word=raw_input('请输入Fuzzer密码的关键字[多个关键字","隔开]:')
        wordlist=word.split(',')
        self.getPwdTemplat()
        '''
            遍历列表，将密码模板的内容替换为列表里的关键字
        '''
        fuzzerResult=[]
        for word in wordlist:
            for i in pwdlist:
                i=i.replace('%username%',word)
                if i not in fuzzerResult:
                    fuzzerResult.append(i)
        '''
            最后输出所有Fuzzer出的密码
        '''
        for temp in fuzzerResult:
            print temp

        self.outputDicFile(fuzzerResult)
        return '结果已保存到'+filepath+os.sep+'password.txt中...'

