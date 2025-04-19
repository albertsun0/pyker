from abc import abstractmethod


class Player:
    @abstractmethod
    def handle_event(self):
        pass
