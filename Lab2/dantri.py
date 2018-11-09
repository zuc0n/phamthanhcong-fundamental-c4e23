from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

#1. Connect to the page

url = "https://dantri.com.vn"
conn = urlopen(url)

#2. Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")
# print(page_content)
with open('file_dantri.html', 'wb') as s:
    s.write(raw_data)
#3. Find ROI region
soup = BeautifulSoup(page_content, "html.parser")
# print(soup.prettify())
ul = soup.find('ul', 'ul1 ulnew')
# print(ul.prettify())
# #4. Extract data

li_list = ul.find_all('li')
new_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']

    news = OrderedDict({
        'title': title,
        'link': link,
    })
    new_list.append(news)
#5. Save data
pyexcel.save_as(records=new_list, dest_file_name='dantri.xlsx')