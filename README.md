# py3_multithread_requests
```
from multiRequests import multiRequests
from fake_useragent import UserAgent

ua = UserAgent()
UserAgent_currrent = ua.random
HEADERS={'User-Agent': UserAgent_currrent}

urls = ["https://google.com","https://google.com","https://google.com","https://google.com"]
x = multiRequests(urls, 3, headers = HEADERS, timeout = 2)
y = x.run()
```
