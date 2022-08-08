
import json
import requests



url = "https://services.chipotle.com/restaurant/v3/restaurant"

payload = json.dumps({
  "latitude": 37.338739999999994,
  "longitude": -121.88525250000002,
  "radius": 800000467,
  "restaurantStatuses": [
    "OPEN",
    "LAB"
  ],
  "conceptIds": [
    "CMG"
  ],
  "orderBy": "distance",
  "orderByDescending": False,
  "pageSize": 4000,
  "pageIndex": 0,
  "embeds": {
    "addressTypes": [
      "MAIN"
    ],
    "realHours": True,
    "directions": True,
    "catering": True,
    "onlineOrdering": True,
    "timezone": True,
    "marketing": True,
    "chipotlane": True,
    "sustainability": True,
    "experience": True
  }
})
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Chipotle-CorrelationId': 'OrderWeb-0a7ad8fd-230a-42ab-bafd-d2c262c2d6f2',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Ocp-Apim-Subscription-Key': 'b4d9f36380184a3788857063bce25d6a',
  'Origin': 'https://www.chipotle.com',
  'Referer': 'https://www.chipotle.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'Cookie': 'f5avrbbbbbbbbbbbbbbbb=HDOHKIENKGIGGOLLJENEBAHLPHDEBHFODKDGBECDDMPCBJKGEELPHHLINFIOIFAICOAJLEGFOPBDNHLAANKEMBAMLDGALGIAGPMAPIPEEFIFODFJANBEMEEOADGIIHJL; TS015699ee=019be61247da4c6e5294f5d570cd796e19b036193d19fffc6c9a4eba9881e278a76689fc79258afbd4dca1069b02b3a01e86920865'
}

response = requests.request("POST", url, headers=headers, data=payload)

stores = json.loads(response.text)
all_store = []
for store in stores['data']:
    temp = {}
    temp["store_id"] = store['restaurantNumber']
    temp["street_address"] = store['addresses'][0]['addressLine1']
    temp["city"] = store['addresses'][0]['locality']
    temp["state"] = store['addresses'][0]['administrativeArea']
    temp["country_code"] = 'US'
    temp["zip_code"] = store['addresses'][0]['postalCode']
    temp["brand"] = 'Chipotle'
    temp["latitude"] = store['addresses'][0]['latitude']
    temp["longitude"] = store['addresses'][0]['longitude']
    link = 'https://locations.chipotle.com'
    link += f'/{temp["state"].lower()}'
    cityname = temp["city"].lower().replace(" ", "-")
    link += f'/{cityname}'
    addy = temp["street_address"].replace(" ", "-")
    link += f'/{addy.lower()}'
    temp["web_url"] = link
    all_store.append(temp)

final = json.dumps(all_store)
with open('chipotle_file.json', 'w') as out:
    out.write(final)
    
print('done')

