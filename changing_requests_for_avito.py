import csv

def get_clear_bad_words_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [sity_name.split('\n')[0] for sity_name in file.readlines() if sity_name != '\n']
    

def reborn_queries(file_path, file_extension='txt', length_limit=-1, bad_words_list=''):
    clear_bad_words_list = get_clear_bad_words_list(bad_words_list)

    with open(file_path, 'r', encoding='utf-8') as f:
        tag_list = csv.reader(f, quotechar='|')
        modify_tag_list = list(tag_list)[1:]
        FINAL_LIST :str = ''
        
        for row_list in modify_tag_list[:length_limit]:
            final_value = row_list[0].split(';')[0]
            if clear_bad_words_list:
                if [sity for sity in clear_bad_words_list if sity.lower() in final_value]:
                    continue
                FINAL_LIST += final_value + ', '
            else:
                FINAL_LIST += final_value + ', '
        print('Длина списка в символах - ', len(FINAL_LIST))
        
        with open(f'{file_path.split('.')[0]}_ref.{file_extension}', 'w', encoding='utf-8') as file:
            file.write(FINAL_LIST)
            print('--- writing is done! ---')


# if __name__ == '__main__':
    
#     bad_words_file = 'some_path/some_name_tag_file.file_extension'
#     reborneted_file_path = 'some_path/wordstat_top_queries_ORDER_STATUS.csv'
    
#     bad_words_list = get_clear_bad_words_list(bad_words_file)
#     reborn_queries(reborneted_file_path, bad_words_list)
