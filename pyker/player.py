from abc import abstractmethod


class Player:
    def __init__(self, id, stack):
        self.id = id
        self.stack = stack

    @abstractmethod
    def handle_event(self):
        pass
