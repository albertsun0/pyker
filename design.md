# Pyker

# Goals:

- Keep track of poker game state
- Provide utility functions for creating poker bots + hand eval

Player

- money
- hand

Game

- players

Round

- pot
- rotation, bb, sb, ...
- player states
- game_state - preflop, flop, turn, river
- community
- log of all actions

  - prev actions
  - actions in current round so far [fold, raise, check, ...]

- Advanced logic
  - Handling Blinds, turns, reraises
  - Handling winner, distribution, side pots
