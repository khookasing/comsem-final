import requests
from bs4 import BeautifulSoup
import re
import os
import time

song_count = 0

def writeFile(song_url):
    #print('hi')
    global song_count
    song_count += 1
    req_resp = requests.get(song_url)
    req_soup = BeautifulSoup(req_resp.text, 'html.parser')

    if req_soup.find(class_ = 'fsZx1') == None:
        artist = ''
    else:
        artist = req_soup.find(class_ = 'fsZx1').text.split('\n')[1].strip()
    artist = re.sub('[^A-Za-z一-龠\d\(\)_ ]', '', artist)
    if artist == '':
        artist = 'StrangeName'
    
    if req_soup.find(class_ = 'fsZx2') == None:
        title = ''
    else:
        title = req_soup.find(class_ = 'fsZx2').text.strip()
    title = re.sub('[^A-Za-z一-龠\d\(\)_ ]', '', title)
    if title == '':
        title = 'StrangeTitle' + str(song_count)
    
    req_lyrics = req_soup.find('dd','fsZx3')

    if(req_lyrics!=None):

        s = str(req_lyrics)
        start = re.search('<br/><br/>',s).start()
        s = s[start:]
        req_lyrics = BeautifulSoup(s, 'html.parser')

        if re.search('\[(([a-z]|\d|\:|\.|)+|([a-z]+:\S{1,4}))\]',req_lyrics.text)!=None:
            end = re.search('\[(([a-z]|\d|\:|\.|)+|([a-z]+:\S{1,4}))\]',req_lyrics.text).start()
            lyrics = req_lyrics.text[:end]
        else:
            lyrics = req_lyrics.text

        lyrics = lyrics.replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網','')
        lyrics = re.sub(r'感謝.{5,20}(修正|提供)歌詞', '', lyrics)

        path = artist + '_' + title + '.txt'
        while_count = 0
        while os.path.exists(path) & (while_count < 100):
            while_count += 1
            path += '0'
        
        with open(path, 'w') as f:
            f.write(lyrics)
        
        print(artist + ' ' + title)
        print(lyrics[:min(25,len(lyrics))] + '...')
        
artists = [ 
            'https://mojim.com/twh109122.htm',
            'https://mojim.com/twh101283.htm',
            'https://mojim.com/twh107946.htm',
            'https://mojim.com/twh102164.htm',
            'https://mojim.com/twh104613.htm',
            'https://mojim.com/twh100967.htm'
          ]


curDir = os.getcwd()
sleep_count = 0

if not os.path.exists('data'):
    os.mkdir('data')
    print('Directory \"data\" Created ')
else:
    print('Directory \"data\" already exists')

curDir += '/data'
if not os.path.exists('lyrics'):
    os.mkdir('lyrics')
    print('Directory \"lyrics\" Created ')
else:
    print('Directory \"lyrics\" already exists')
curDir += '/lyrics'
os.chdir(curDir)

for i in artists:
    resp = requests.get(i)
    #歌手網址
    soup = BeautifulSoup(resp.text, 'html.parser')

    artist = soup.find_all(itemprop = 'title')[-1].text.strip()
    artist = re.sub('[^A-Za-z一-龠\d\(\)_ ]', '', artist)
    if artist == '':
        artist = 'StrangeName'
    
    if not os.path.exists(artist):
        os.mkdir(artist)
        print('Directory \"' + artist + '\" Created ')
    else:
        print('Directory \"' + artist + '\" already exists')

    artDir = curDir + '/' + artist
    os.chdir(artDir)
    
    block3 = soup.find_all('dd', 'hb2')
    block4 = soup.find_all('dd', 'hb3')
    
    for j in (block3 + block4):
        song_left = j.find_all('span','hc3')
        song_right = j.find_all('span','hc4')
        for k in (song_left + song_right):
            song_link = k.find_all('a')
            for l in song_link:
                song_url = 'https://mojim.com' + l.get('href')
                writeFile(song_url)
                #sleep
                sleep_count += 1
                if sleep_count >100:
                    print('======......sleeping......======')
                    time.sleep(3)
                    sleep_count = 0
    
    os.chdir(curDir)

