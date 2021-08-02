import requests

def csv_reader(inn_list):
    path_csv_file = input('Укажите полный путь к csv файлу: ')

    with open(path_csv_file, 'r', encoding='utf-8') as w:
        inns = csv.reader('w', delimiter=';')

        for i in inns:
            inn_list.put(i)








# Queue innt_list gets all inn list from csv file
inn_list = mp.Queue()
csv_reader(inn_list)

# Queue parsed_data keeps all parsed datas
parsed_data = mp.Queue()

# Creating Process
procs = []
for i in range(core_count):
    proc = mp.Process(target=, args=(inn_list, parsed_data))
    procs.append(proc)
    proc.start()

# Completing Process
for proc in procs:
    proc.join()





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


