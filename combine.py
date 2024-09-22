import os


def get_sorted_files_list(files_list):
    vocabulary = {}
    for file_name in files_list:
        with open(file_name, encoding='utf-8') as file:
            length = len(file.readlines())
            vocabulary[length] = file_name
    sorted(vocabulary.items())
    sorted_vocabulary = dict(sorted(vocabulary.items()))
    return sorted_vocabulary

def combine_files(files_list):
    sorted_vocabulary = get_sorted_files_list(files_list)
    with open('result_file.txt', 'w', encoding='utf-8') as result_file:
        for quantity, file_name in sorted_vocabulary.items():
            result_file.write(file_name + '\n')
            result_file.write(str(quantity) + '\n')
            with open(file_name, 'r', encoding='utf-8') as file:
                result_file.writelines(file.readlines())
                result_file.write('\n')


list_txt = [file_name for file_name in os.listdir() if file_name.endswith('.txt') and file_name != 'result_file.txt']

combine_files(list_txt)