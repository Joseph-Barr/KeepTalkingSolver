class Error(Exception):
    pass

class DictSwapException(Error):
    def __init__(self, message):
        super().__init__(message)