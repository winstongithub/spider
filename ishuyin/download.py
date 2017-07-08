import os
import requests
from bs4 import BeautifulSoup


def download(du,index):
    print(du)
    mr=requests.get(du)
    f=open( str(index)+'.mp3','wb')
    f.write(mr.content)
    f.close()
        
def geturl(url,index):
    r=requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    a=soup.select('#urlDown')
    s = a[0].get('href').split('*')
    du=''
    for i in s:
        if len(i) != 0:
            du = du + chr(int(i))
    download(du,index)    
if __name__=='__main__':
    for i in range(1,30):
        url = r'http://www.ishuyin.com/player.php?mov_id=5113&look_id={0}&player=down'.format(i)
        geturl(url,i)
