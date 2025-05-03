import enum
from deck import Deck
from player import Player
from hand import Hand

MAX_RAISE_ROUNDS = 3


class GameState(enum):
    PREFLOP = "preflop"
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"


class PlayerStatus(enum):
    IN = "in"
    OUT = "out"


class Game:
    def __init__(self, players):
        self.players = players


class Round:
    def __init__(self, players, dealer_index=0, small_blind=1, big_blind=2, ante=0):
        self.deck = deck = Deck()
        deck.shuffle()

        self.players = players
        self.num_players = len(players)
        self.bets = [0] * len(players)
        self.player_status = [PlayerStatus.IN] * len(players)
        self.hands = []
        self.pot = 0
        self.community = []
        self.state = GameState.PREFLOP
        self.log = []
        self.dealer_index = dealer_index

        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ante = ante

        for _ in players:
            hand = [deck.deal(), deck.deal()]
            self.hands.append(hand)

    def add_cards(self, n=1):
        for _ in range(n):
            self.cards.append(self.deck.deal())

    def start_round(self):
        # rest round information
        current_player = (self.dealer_index + 1) % self.num_players
        self.player_status = [PlayerStatus.IN] * self.num_players

        # handle big and small blind
        self.bets[current_player] = self.small_blind
        self.bets[(current_player + 1) % self.num_players] = self.big_blind

        # broadcast round start to other players
        rounds = [GameState.PREFLOP, GameState.FLOP, GameState.TURN, GameState.RIVER]
        cards_to_deal = [3, 1, 1, 0]
        for index, round in enumerate(rounds):
            self.state = round
            # broadcast new_round message
            # TOOD: create some sort of types for messages
            message = {
                "event": "new_round",
                "dealer": self.dealer_index,
                "round_state": self.state,
                "community": self.community,
            }
            self.play_round()

            self.add_cards(cards_to_deal[index])

        # handle show and win logic
        win_conditions = []

        for i, hand in enumerate(self.hands):
            if self.player_status[i] == PlayerStatus.IN:
                win_conditions.append((hand.score_hand(self.community), i))

        win_conditions.sort(reverse=True)

        winner, bit_string = win_conditions[0]

        win_conditon, tb = Hand.display_winning_hand(bit_string)

        # distribute money to winner

        # handle side pots

        # handle show

        # everyone has to show up to winner?

        # message = {winner, win_conditions, shown_hands[], payouts[]}

    def play_round(self):
        # broadcast round start
        round_over = False

        for raise_round in range(MAX_RAISE_ROUNDS):
            current_player = (self.dealer_index + 1) % self.num_players

            if self.state == GameState.PREFLOP:
                # handle big and small blind

                # for first round, first 2 players are last to act
                current_player = (current_player + 2) % self.num_players

            for i in range(len(self.players)):
                player = self.players[current_player]
                # Actions = [fold, call/check, raise]
                #
                # request move from player
                current_player = (current_player + 1) % len(self.players)

                # broadcast move to other players

            if round_over:
                break
