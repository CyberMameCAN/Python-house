import requests

#resp = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=8990435')
resp = requests.get('https://zipcloud.ibsnet.co.jp/api/search',
                    params={'zipcode': '8990435'})

print(resp.status_code)
if resp.status_code == 200:
    #print(resp.text)
    resp_json = resp.json()
    results = resp_json['results'][0]
    address = results['address1'] + results['address2'] + results['address3']
    print(address)
