import redis
import urllib.request
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
counter=0
for i in tqdm(range(30000,40000)):
    load_url = "https://review.travel.rakuten.co.jp/hotel/voice/"+str(i)+"/?f_sort=4&f_next=20"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    if('指定されたページが見つかりません' in soup.title.text):
        pass
    else:
        load_url = 'https://us-central1-arctic-conduit-280420.cloudfunctions.net/GetVector?type=1&value='+str(i)
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")
        if(soup.text=='Error: could not handle the request\n'):
            pass
        else:
            r.set('hotel:'+str(i)+':vec',soup.text)
            counter=counter+1
print(counter)