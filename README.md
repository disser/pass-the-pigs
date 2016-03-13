pass-the-pigs
=============

A framework for comparing player strategies for "Pass the Pigs" game in Python


Usage
-----

Create a class in players.py which inherits the Player class.  The class must
implement the wants_to_roll(turn_score, total_score, other_scores) method,
and returns True if the strategy should roll.

turn_score: the player's current score for the turn.  It will be zero if 
the player has not yet rolled for this turn, so the strategy should always
roll in this case (or lose every game, your choice).

total_score: the player's current total score for the game.

other_scores: list of the total scores of every other player.

Play a number of games by specifying a list of STRATEGY:arg,...

Example:

    $ python passthepigs.py --games 100 Threshold:10 Threshold:20
    Strategy Threshold:10 win%: 44.00
    Strategy Threshold:20 win%: 56.00
    

