from changing_requests_for_avito import *



bad_words_file = 'some_path/some_name_tag_file.file_extension'
reborneted_file_path = 'some_path/wordstat_top_queries_ORDER_STATUS.csv'
    
bad_words_list = get_clear_bad_words_list(bad_words_file)
reborn_queries(reborneted_file_path, bad_words_list)