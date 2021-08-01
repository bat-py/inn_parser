import multiprocessing as mp
from . import parser
from . import excel_writer
import csv


    
def csv_reader(inn_list):
    path_csv_file = input('Укажите полный путь к csv файлу: ')
    
    with open(path_csv_file, 'r' encoding='utf-8') as w:
        inns = csv.reader(w, delimiter=';')
        
        for i in inns:
            inn_list.put(i)





if __name__ == '__main__':
    #Defining precess count
    core_count = int(input('Количество процессов (если ничего не указать то будет рано количеству ядер CPU):'))
    if not core_count:
        core_count = mp.cpu_count()


    #Queue innt_list gets all inn list from csv file
    inn_list = mp.Queue()
    csv_reader(inn_list)


    #Queue parsed_data keeps all parsed datas 
    parsed_data = mp.Queue()


    #Creating Process
    procs = []
    for i in range(core_count):
        proc = mp.Process(target=, args=(inn_list, parsed_data))
        procs.append(proc)
        proc.start()


    #Completing Process 
    for proc in procs:
        proc.join()
        

    






