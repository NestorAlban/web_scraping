import datetime
from datetime import datetime as ds
import os


class Creation():
    def __init__(self) -> None:
        pass

    def check_file(self, file_txt_path, title, body):
        try:
            response_1 = None
            datetime_date = datetime.date.today().strftime('%d-%m-%Y')
            datetime_time = ds.now().strftime('%H:%M:%S')
            if os.path.isfile(file_txt_path):
                with open(file_txt_path) as f:
                    lines = f.readlines()
                    print(lines)
                response_1 = 'read'
            else:
                with open(file_txt_path, 'w', encoding = 'utf-8') as f:
                    f.write(title)
                    f.write('\n\n')
                    f.write(body)
                    f.write('\n\n')
                    f.write(f'This file was created the {datetime_date}, at {datetime_time}')
                response_1 = 'created'
        except ValueError as ve:
            print(ve)
        return print(f'File was {response_1}')

    def create_foder(self, path1, path2, today, t1, t2, t3, b1, b2, b3):
        try:
            p_1 = f'{path1}/{path2}'
            p_2 = f'{path1}/{path2}/{today}'
            summary_1 = f'{path1}/summary_1.txt'
            summary_2 = f'{path1}/{path2}/summary_2.txt'
            summary_3 = f'{path1}/{path2}/{today}/summary_3.txt'
            if not os.path.isdir(path1):
                os.mkdir(path1)
            self.check_file(summary_1, t1, b1)
            if not os.path.isdir(p_1):
                os.mkdir(p_1)
            self.check_file(summary_2, t2, b2)
            if not os.path.isdir(p_2):
                os.mkdir(p_2)
            self.check_file(summary_3, t3, b3)
            path_to_folder = f'{path1}/{path2}/{today}'
        except ValueError as ve:
            print(ve)
        return path_to_folder

    def create_categories_foder(path1, category):
        try:
            p_1 = f'{path1}/{category}'
            if not os.path.isdir(path1):
                os.mkdir(path1)
            if not os.path.isdir(p_1):
                os.mkdir(p_1)
            path_to_folder = f'{path1}/{category}'
        except ValueError as ve:
            print(ve)
        return path_to_folder