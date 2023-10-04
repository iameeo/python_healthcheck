import requests
import xml.etree.ElementTree as ET

filePath = "D:/file.txt"

def fileRead():
    f = open(filePath, 'r')
    line = f.readline()
    f.close()
    return line

def fileWrite(text):
    f = open(filePath, 'w')
    f.write(text)
    f.close()

def slackMessage(text):
    text = text
    url = 'https://hooks.slack.com/services/TMGE25VGT/B05GZRKLRU1/'
    url = url + '78IBMFJojDSDx6ON7wEXiOe7'
    payload = { "text" : text }

    requests.post(url, json=payload)

res = requests.get("https://rss.blog.naver.com/emoticonews.xml")
root = ET.fromstring(res.text)

i=0
for data in root.iter('item'):
    if(i == 0):
        oldText = fileRead()
        if(oldText != data[2].text):
            fileWrite(data[2].text)
            slackMessage("신규 이모티콘 : " +data[3].text)
        break

siteList = ['https://www.barunsoncard.com','https://m.barunsoncard.com','https://www.barunsonmall.com','https://m.barunsonmall.com','https://www.premierpaper.co.kr','https://m.premierpaper.co.kr','https://deardeer.kr']

for i in siteList:
    try:
        response = requests.get(i)
        if response.status_code != 200 :
            slackMessage(str(i) + " : " + str(response.status_code))
    except:
        slackMessage("error : " + str(i))
        continue