class Words:

    def __init__(self, some_string: str):
        self.__some_string = some_string

    def find_smallest_word(self) -> str:
        words = self.__some_string.split(', ')
        smallest_word = words[0]

        for word in words:
            if word < smallest_word:
                smallest_word = word

        return smallest_word
