import csv

def get_clear_sity_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [sity_name.split('\n')[0] for sity_name in file.readlines() if sity_name != '\n']
    

def reborn_queries(file_path, sity_list=''):
    with open(file_path, 'r', encoding='utf-8') as f:
        qwe = csv.reader(f, quotechar='|')
        or_list = list(qwe)[1:]
        ORIG_LIST:str = ''
        
        for row_list in or_list[:35]:
            final_value = row_list[0].split(';')[0]
            if sity_list:
                if [sity for sity in sity_list if sity.lower() in final_value]:
                    continue
                ORIG_LIST += final_value + ', '
            else:
                ORIG_LIST += final_value + ', '
        print('Длина списка - ', len(ORIG_LIST))
        
        with open(f'{file_path.split('.')[0]}_ref.txt', 'w', encoding='utf-8') as file:
            file.write(ORIG_LIST)
            print('--- writing is done! ---')
            
        
if __name__ == '__main__':
    
    sity_path = 'C:/Users/Val/Desktop/Обучалки_и_писульки/Писульки/города_россии.txt'
    reborneted_file_path = 'C:/Users/Val/Desktop/Promo/запросы и скрипты/wordstat_top_queries_ORDER_STATUS.csv'
    
    sity_list = get_clear_sity_list(sity_path)
    reborn_queries(reborneted_file_path, sity_list)