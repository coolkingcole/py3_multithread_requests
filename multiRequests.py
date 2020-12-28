import queue
import threading
import time
import sys
from argparse import ArgumentParser
import requests

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, inqueue, outqueue):
        threading.Thread.__init__(self)
        self.in_queue = inqueue
        self.out_queue = outqueue
        #self.method = method

    def run(self):
        while True:
            #grabs host from queue
            host = self.in_queue.get()
            #host = self.in_queue.get(self)
            chunk = ""
            requestObj = 0
            try:
                #url = urllib2.urlopen(myurl, timeout=3)
                #if self.method =="get":
                requestObj = requests.get(host)
                #print(host)

            except:
                #print('hit exception....')
                requestObj = "request_failed"
                #pass
            chunk = [host, requestObj]
            #place chunk into out queue
            self.out_queue.put(chunk)

            #signals to queue job is done
            self.in_queue.task_done()

class DatamineThread(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue, outList):
        threading.Thread.__init__(self)
        self.out_queue = out_queue
        self.outList = outList

    def run(self):
        while True:
            #grabs host from queue
            chunk = self.out_queue.get()
            self.outList.append(chunk)
            #signals to queue job is done
            self.out_queue.task_done()

class multiRequests:
    def __init__(self, urlList, threadCount):
        self.urlList = urlList
        #self.requestType = requestType
        #self.options = options
        self.threadCount = threadCount
    
    def run(self):
        inqueue = queue.Queue()
        outqueue = queue.Queue()
        requestsLists = []
        #spawn a pool of threads, and pass them queue instance
        for i in range(self.threadCount):
            t = ThreadUrl(inqueue, outqueue)
            t.setDaemon(True)
            t.start()
        
        #populate queue with data
        for url in self.urlList:
            inqueue.put(url)
        
        # the threads for the writer, it only needs one really.    
        for i in range(20):
            dt = DatamineThread(outqueue,requestsLists)#args.output)
            dt.setDaemon(True)
            dt.start()
        #wait on the queue until everything has been processed
        inqueue.join()
        outqueue.join()
        return requestsLists
