from conversation.menues.menu_continue import remove_menu
from conversation.menues.menu_sort import show_note, sorted_menu, id_note_menu
from conversation.parser.inputParser import date_parser
from workWithFiles.deleteNote import DeleteNote
from workWithFiles.readNote import ReadNote


class Functions:
    def return_to_menu(self):
        rtn = int(input(f'1 - меню\n'
                        f'2 - выход\n'))
        if rtn == 1:
            return True
        else:
            return False

    def read_note(self):
        choose = int(input(show_note()))
        if choose == 1:
            ReadNote().show_all_notes()

        elif choose == 2:
            date = date_parser(input(sorted_menu()))
            ReadNote().show_date(date)

        elif choose == 3:
            id_note = input(id_note_menu())
            ReadNote().show_id(id_note)

    def remove_note(self):
        delete = int(input(remove_menu()))
        DeleteNote().delete_note(delete)
