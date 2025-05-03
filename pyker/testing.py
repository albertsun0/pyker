from card import Card, Rank, Suit
from deck import Deck
from hand import Hand
import time


def main():
    print("Hello from pyker!")

    # for i in range(1000):
    #     deck = Deck()
    #     deck.shuffle()

    #     cards = [deck.deal() for _ in range(5)]

    #     h = Hand([deck.deal() for _ in range(2)])
    #     start = time.time()
    #     wincond, tiebreak = h.score_hand(cards)
    #     diff = time.time() - start
    #     # print(diff)
    #     print(
    #         [str(card) for card in h.cards],
    #         [str(card) for card in cards],
    #         wincond.name,
    #         [str(card) for card in tiebreak],
    #     )

    deck = Deck()
    deck.shuffle()

    deck.shuffle()

    h = Hand([deck.deal(), deck.deal()])

    # print(h.desc())

    h = Hand(
        [Card(rank=Rank.ACE, suit=Suit.CLUB), Card(rank=Rank.ACE, suit=Suit.HEART)]
    )

    # print(h.desc())

    h = Hand(
        [
            Card(rank=Rank.FOUR, suit=Suit.HEART),
            Card(rank=Rank.SEVEN, suit=Suit.DIAMOND),
        ]
    )

    board = [
        Card(rank=Rank.THREE, suit=Suit.DIAMOND),
        Card(rank=Rank.FIVE, suit=Suit.CLUB),
        Card(rank=Rank.TWO, suit=Suit.CLUB),
        Card(rank=Rank.FIVE, suit=Suit.CLUB),
        Card(rank=Rank.TWO, suit=Suit.CLUB),
    ]

    # print(h.display_winning_hand(h.score_hand(board)))

    start = time.time()
    print(h.monte_carlo(board, other_player_count=2))
    print(time.time() - start)
    # print(h)


if __name__ == "__main__":
    main()
