from pyker.card import Card, Rank, Suit
from pyker.deck import Deck


def main():
    print("Hello from pyker!")

    deck = Deck()

    print(deck)

    deck.shuffle()

    print("\n-------\n")

    print(deck)
    # print(Suit.DIAMOND)

    # print(Rank.ACE)

    # print(Card(Rank.ACE, Suit.DIAMOND))


if __name__ == "__main__":
    main()
