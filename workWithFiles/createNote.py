import os

from conversation.input_data.input import InputCommand
from conversation.menues.menu_continue import refactor_menu, enter_menu
from workWithFiles.deleteNote import DeleteNote

os.chdir(os.path.dirname(__file__))


class CreateNote:
    def make_note(self, command: InputCommand):
        note_id = command.set_id()

        fill = f' id: {note_id}; created: {command.get_time()}; -> {command.get_headline()}; ' \
               f'Note: {command.get_text()};\n'
        with open(command.get_file(), 'a', encoding='utf-8') as file:
            file.writelines(fill)
        print(' Заметка добавлена!')

    def refactor_note(self):
        command = InputCommand()
        id_note = int(input(refactor_menu()))
        text = DeleteNote().change_note(id_note)
        if text is not None:
            text.split(';')
            headline = text[2].replace(' ->', '')
            command.set_headline(headline)

            answer = input(enter_menu())
            command.set_text(answer)

            fill = f' id: {id_note}; edited: {command.get_time()}; -> {command.get_headline()}; ' \
                   f'Note: {command.get_text()};\n'

            with open(command.get_file(), 'a', encoding='utf-8') as file:
                file.writelines(fill)
            print(' Заметка отредактирована!')
