import requests
import time
t1=time.time()
li=["https://bit.ly/2vqkYSu","https://bit.ly/3aqlYoH","https://bit.ly/32DA0Ra"]
for i in range(0,len(li)):
    url=li[i]
    s=requests.session()
    response=s.get(url)
    fp=open(f"saif{i}.pdf",'wb')
    fp.write(response.content)
    fp.close()
t2=time.time()
print(t2-t1)