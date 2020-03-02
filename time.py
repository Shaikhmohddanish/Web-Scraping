import time
import requests
url="https://bit.ly/2vqkYSu"
t1=time.time()
requests.get(url)
t2=time.time()
print(-t1+t2)