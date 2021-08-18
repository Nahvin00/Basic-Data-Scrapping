from bs4 import BeautifulSoup
import requests
import pandas as pd

threads_text=[]
replies_text=[]
views_text=[]
date_text=[]

for i in range(1,11):
    url = "https://www.mentalhealthforum.net/forum/forums/depression-forum.366/page-" + str(i)
    request = requests.get(url)
    page = request.text
    soup = BeautifulSoup(page, 'lxml')

    for threads in soup.find_all('div', attrs={'class': 'structItem-title'}):
        threads_text.append(threads.get_text().strip())

    for replies in soup.find_all('dl', attrs={'class': 'pairs pairs--justified'}):
        reply = replies.get_text().strip().split()
        replies_text.append(reply[1])

    for views in soup.find_all('dl', attrs={'class': 'pairs pairs--justified structItem-minor'}):
        view = views.get_text().strip().split()
        views_text.append(view[1])

    for date in soup.find_all('time', attrs={'class': 'structItem-latestDate u-dt'}):
        date_text.append(date.get_text().strip())

data={'Title':threads_text,'Replies':replies_text,'Views':views_text,'Date/Time':date_text}
all_threads=pd.DataFrame(data)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(all_threads)
