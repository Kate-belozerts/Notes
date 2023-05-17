import os

from conversation.input_data.input import InputCommand

os.chdir(os.path.dirname(__file__))


def correct_note(note):
    return ' id: ' + str(note)


class DeleteNote:
    __file = InputCommand().get_file()

    def delete_note(self, id_note):
        id_note = correct_note(id_note)
        with open(self.__file, 'r', encoding='utf-8') as file:
            content = file.readlines()
            lst = list()
            for i in content:
                res = i.split(';')
                if id_note not in res[0]:
                    lst.append(i)

        with open(self.__file, 'w', encoding='utf-8') as file:
            for i in range(len(lst)):
                file.writelines(lst[i])
        if len(content) != len(lst):
            print(' Удалено!')
        else:
            print(' Не нашлось такой заметки...')

    def change_note(self, id_note):
        id_note = correct_note(id_note)
        result = ''
        with open(self.__file, 'r', encoding='utf-8') as file:
            content = file.readlines()
            lst = list()
            for i in content:
                res = i.split(';')
                if id_note not in res[0]:
                    lst.append(i)
                else:
                    result = i

        with open(self.__file, 'w', encoding='utf-8') as file:
            for i in range(len(lst)):
                file.writelines(lst[i])
        if len(content) != len(lst):
            return result
        else:
            print(' Такой заметки не существует!')
