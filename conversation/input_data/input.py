import datetime
import time


class InputCommand:
    __id = 0
    __number = 0
    __headline = ""
    __text = ""
    __file = "note.csv"
    __time = datetime.datetime.now()

    def set_number(self, number):
        self.__number = number

    def set_headline(self, headline):
        self.__headline = headline

    def set_text(self, text):
        self.__text = text

    def set_time(self):
        self.__time = datetime.datetime.now()

    def set_id(self):
        self.__id = round(time.time() * 1000 % 1000)
        number = self.__id
        return int(number)

    def get_file(self):
        return self.__file

    def get_number(self):
        return self.__number

    def get_headline(self):
        return self.__headline

    def get_text(self):
        return self.__text

    def get_time(self):
        return self.__time
