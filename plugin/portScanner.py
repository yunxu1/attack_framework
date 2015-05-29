# -*- coding:gb2312 -*-
__author__ = '云絮'
import sys
import socket
import threading
from Queue import Queue
sys.path.append('../')

from interface.iPlugin import Plugin

__all__ = ["portScanner"]
class scanner():
    def __init__(self,address,port):
        self.address=address
        self.port=port

    def scan(self):
        try:
            sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sk.connect((self.address,self.port))
            print '%s:%d..........open'%(self.address,self.port)
        except Exception,e:
             #print '%s:%d..........close'%(self.address,self.port)
            e
        finally:
            sk.close()
class scannerWork(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        while True:
            try:
                address,port=self.queue.get(False)
                scann=scanner(address,port)
                scann.scan()
            except Exception,e:
                sys.exit(0)
class portScanner(Plugin):

    name = "portScanner"
    version = '0.0.1'
    description='这只是一个单纯的端口扫描器'

    def __init__(self):
        Plugin.__init__(self)


    def execute(self,args):
        queue=Queue()
        for i in range(0,800):
            queue.put((args,i))
        for a in range(30):
            scanner1=scannerWork(queue)
            scanner1.start()
        scanner1.join()
        return 'scan done!'