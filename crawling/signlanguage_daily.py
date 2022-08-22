import csv
import time
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

output_file_name = 'signlanguage_daily.txt'
output_file = open('./' + output_file_name, "w", encoding="utf-8")
output_file.write("{}\t{}\t{}\n".format("id","word","url"))
output_file.close()

lastIndex = 368

id = 1
for i in range(1,lastIndex+1):
    pageIndex = i
    url = 'https://sldict.korean.go.kr/front/sign/signList.do?current_pos_index=&origin_no=0&searchWay=&top_category=CTE&category=&detailCategory=&searchKeyword=&pageIndex=' + str(pageIndex) +'&pageJumpIndex='
    print("index = ",i,"url = ",url)
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text,'html.parser')
    soupWord = soup.findAll('span',class_='tit')
    soupVid = soup.findAll('div', class_='tumb_w')
    for i in range(len(soupWord)):
        word = soupWord[i].text.strip().split(',')
        vidUrl = soupVid[i].findAll('img')[1].get('src')[:-11] + '700X466.mp4'
        for w in word:
            print(w,vidUrl)
            output_file = open('./' + output_file_name, "a", encoding="utf-8")
            output_file.write("{}\t{}\t{}\n".format(id, word, vidUrl))
            output_file.close()
            id += 1
    time.sleep(random.uniform(1,2))

file = pd.read_csv('./signlanguage_daily.txt')
new_csv_file = file.to_csv('./signlanguage_daily.csv',index=False)