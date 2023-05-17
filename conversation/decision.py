from conversation.functions import Functions
from conversation.input_data.fill_command import FillCommand
from conversation.input_data.input import InputCommand
from workWithFiles.createNote import CreateNote


class Decide:
    __inputCommand = InputCommand()

    def decision(self):
        command = self.__inputCommand
        stop = Functions().return_to_menu()

        while stop:
            FillCommand().choose_number(command)
            if command.get_number() == 1:
                FillCommand().fill_new_command(command)
                CreateNote().make_note(command)
                stop = Functions().return_to_menu()

            elif command.get_number() == 2:
                CreateNote().refactor_note()
                stop = Functions().return_to_menu()

            elif command.get_number() == 3:
                Functions().remove_note()
                stop = Functions().return_to_menu()

            elif command.get_number() == 4:
                Functions().read_note()
                stop = Functions().return_to_menu()

            elif command.get_number() == 5:
                stop = False
        print(" Have a good day!")
