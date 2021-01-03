# py3_multithread_requests
```
from multiRequests import multiRequests

HEADERS={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36'}

urls = ["https://google.com","https://google.com","https://google.com","https://google.com"]
x = multiRequests(urls, 3, headers = HEADERS, timeout = 2)
y = x.run()
```
# Installation
python3 -m pip install -r requirements.txt

# Usage
First arg of multiRequests() is the array of urls to get. 2nd arg is the number of threads to spawn. 3 to n arg is any other option you would want to pass to requests inside each thread. run() will execute the requests. 
