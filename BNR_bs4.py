import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bnr.ro/Cursul-de-schimb--7372.aspx'
result = requests.get(url).text
link = BeautifulSoup(result, 'html.parser')

title = link.find_all('div', attrs={'class': 'contentDiv'})[0]
header = []
dataset = []
for tr_index in title.find_all('table'):
    for td_index in tr_index.find_all('tr'):
        td_list = []
        if td_index.find_all('th'):
            header = [th_index.get_text() for th_index in td_index.find_all('th')]

        for index, td_value in enumerate(td_index.find_all('td')):
            #  print(index, td_value)
            if index == 0:
                td_list.append(td_value.text)
            else:
                td_list.append(float(td_value.text.lstrip('   ').replace(',', '.')))

        dataset.append(td_list)

data_frame = pd.DataFrame(dataset, columns=header)
data_frame.to_csv("CursBNR.xls", header=header)

