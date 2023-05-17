from conversation.input_data.input import InputCommand
from conversation.menues.menu_continue import headline_menu, enter_menu
from conversation.menues.menu_start import print_menu


class FillCommand:
    def choose_number(self, command: InputCommand):
        answer = int(input(print_menu()))
        command.set_number(answer)
        command.set_time()

    def fill_new_command(self, command: InputCommand):
        answer = input(headline_menu())
        command.set_headline(answer)

        answer = input(enter_menu())
        command.set_text(answer)
