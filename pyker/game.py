from deck import Deck


class Game:
    def __init__(self, players):
        self.deck = deck = Deck()
        deck.shuffle()

        self.players = players

        for player in players:
            hand = [deck.deal(), deck.deal()]
            player.send_event("hand", hand)

            wait_for(player)
