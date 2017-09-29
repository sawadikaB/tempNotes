def group_crawl(self, objects):
        '''异步抓取
        :param objects: 这个参数的长度不能太长，否则会造成爆栈。
        :return: tree、obj[url或者参数]
        '''
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_url = {executor.submit(self._, obj): obj for obj in objects}
            for future in concurrent.futures.as_completed(future_to_url):
                obj = future_to_url[future]
                tree = future.result()
                yield tree, obj
# 这是异步的一个写法， 另外可以使用gevent包来写，

#  gevent
import time
import requests
session = requests.Session()
import gevent.monkey
gevent.monkey.patch_socket()
start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def fetch(pid):
    response = session.get('http://www.baidu.com')
    if response.status_code == 200:
        print('已经采集到了！时间：%s', tic())

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
