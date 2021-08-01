import requests 



url = 'https://pb.nalog.ru/search.html#quick-result'
HEADERS = {
    'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'accept' : '*/*',
}


PARAMS = {
        'queryAll' : '2636032690',
        'mode' : 'search-all',
        'page' : 'page=1',
        'pageSize' : '10'
        }
i = 0

while True:
    s = requests.get(url, headers=HEADERS, params=PARAMS)
    i += 1
    print(s.status_code, i)


