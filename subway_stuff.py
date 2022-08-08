import requests
from bs4 import BeautifulSoup
import json
import threading
url = 'https://restaurants.subway.com/united-states/'
state_list = []

req = requests.get(url).text

sub = BeautifulSoup(req, 'html.parser')
for i in sub.find('ul', class_ = "Directory-listLinks"):
    href = i.find('a')['href'][-2:]
    href = url + href
    state_list.append(href)

state_list.pop(-1)

finale = [state_list[:25], state_list[25:]]

def genius(link1):
    for states in link1:
        state_store = []  
        req = requests.get(states).text
        sub = BeautifulSoup(req, 'html.parser')
        for i in sub.find('ul', class_ = "Directory-listLinks"):
            href = i.find('a')['href'][17:]
            href = url + href
            state_store.append(href)
        print(state_store)
        
        for x in state_store:
            req = requests.get(x).text
            sub = BeautifulSoup(req, 'html.parser')
            if sub.find('ul', class_ = "Directory-listTeasers Directory-row") is not None:
                inner = []
                for i in sub.find_all('div', class_ = "Teaser-innerWrapper"):
                    href = i.find('a')['href'][20:]
                    href = url + href
                    inner.append(href)
                
                for final in inner:
                    try:
                        req = requests.get(final).text
                        sub = BeautifulSoup(req, 'html.parser')
                        temp = {}
                        temp["street_address"] = sub.find('span', class_ = "c-address-street-1").text
                        temp["city"] = sub.find('span', class_ = "c-address-city").text
                        temp["state"] = sub.find('abbr', itemprop="addressRegion").text
                        temp["country_code"] = 'US'
                        temp['hours'] = sub.find('div', class_ = "c-hours-details-wrapper js-hours-table")['data-days']
                        temp["zip_code"] = sub.find('span', itemprop="postalCode").text
                        temp['web_url'] = final
                        temp["brand"] = 'Subway'
                        temp["latitude"] = sub.find('span', class_ = "coordinates").find_all('meta')[0]['content']
                        temp["longitude"] = sub.find('span', class_ = "coordinates").find_all('meta')[1]['content']
                        one_location = json.dumps(temp)
                        with open('official_subway_file.txt', 'a') as out:
                            out.write(one_location + '\n')
                    except Exception as e:
                        print(e)

                
            
            else:
                try:
                    temp = {}
                    temp["street_address"] = sub.find('span', class_ = "c-address-street-1").text
                    temp["city"] = sub.find('span', class_ = "c-address-city").text
                    temp["state"] = sub.find('abbr', itemprop="addressRegion").text
                    temp["country_code"] = 'US'
                    temp['hours'] = sub.find('div', class_ = "c-hours-details-wrapper js-hours-table")['data-days']
                    temp["zip_code"] = sub.find('span', itemprop="postalCode").text
                    temp['web_url'] = x
                    temp["brand"] = 'Subway'
                    temp["latitude"] = sub.find('span', class_ = "coordinates").find_all('meta')[0]['content']
                    temp["longitude"] = sub.find('span', class_ = "coordinates").find_all('meta')[1]['content']
                    one_location = json.dumps(temp)
                    with open('official_subway_file.txt', 'a') as out:
                        out.write(one_location + '\n')
                except Exception as e:
                    print(e)
    print('done')


for each in finale:
    threading.Thread(target=genius,args=(each,)).start()


