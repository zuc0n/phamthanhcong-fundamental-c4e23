from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

cnt = urlopen(url)

raw_data = cnt.read()
page_content = raw_data.decode('utf8')

# with open("itune_chart.html", "wb") as f:
#     f.write(raw_data)

soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find('ul', '')

li_list = ul.find_all('li')

song_list = []
for li in li_list:
    a = li.h3.a
    b = li.h4.a 
    Title = a.string
    Artist = b.string

    songs = OrderedDict(
        {
            'Title': Title,
            'Artist': Artist,
        }
    )
    song_list.append(songs)
    options = {
     'default_search': 'ytsearch',
     'max_downloads': 1,
     'format': 'bestaudio/audio',
        
    }
    dl = YoutubeDL(options)
    dl.download([Title +  Artist])

pyexcel.save_as(records=song_list, dest_file_name='ItuneTopSongs.xlsx')

