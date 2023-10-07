class Sublist:

    def __init__(self, main_list: list, target_sublist: list):
        self.__main_list = main_list
        self.__target_sublist = target_sublist

    def is_sublist(self) -> bool:
        if not self.__target_sublist:
            return True

        if self.__target_sublist == self.__main_list:
            return True

        for item in range(len(self.__main_list)):
            if self.__main_list[item:item + len(self.__target_sublist)] == self.__target_sublist:
                return True

        return False

