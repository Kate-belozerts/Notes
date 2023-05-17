import os

from conversation.input_data.input import InputCommand

os.chdir(os.path.dirname(__file__))

class ReadNote:
    __file = InputCommand().get_file()

    def show_all_notes(self):
        with open(self.__file, 'r', encoding='utf-8') as file:
            for i in file:
                print(i)

    def show_date(self, date):
        with open(self.__file, 'r', encoding='utf-8') as file:
            for i in file:
                res = i.split(';')
                if date in res[1]:
                    print(i)

    def show_id(self, id_note):
        with open(self.__file, 'r', encoding='utf-8') as file:
            for i in file:
                res = i.split(';')
                res = res[0].split(':')

                if id_note == res[1].replace(" ", ""):
                    print(i)
