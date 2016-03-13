import random

PINK      = 1
DOT       = 2
RAZORBACK = 4
TROTTER   = 8
SNOUTER   = 16
JOWLER    = 32
PIGOUT    = -1


def check_probabilities(iterations):
    results = {}
    for iteration in xrange(iterations):
        r = roll_a_pig()
        if r in results:
            results[r] = results[r] + 1
        else:
            results[r] = 1
    print results


def roll_a_pig():
    roll = random.randint(1,3939)
    if roll <= 1344:
        return PINK
    elif roll <= 1344 + 1295:
        return DOT
    elif roll <= 1344 + 1295 + 767:
        return RAZORBACK
    elif roll <= 1344 + 1295 + 767 + 365:
        return TROTTER
    elif roll <= 1344 + 1295 + 767 + 365 + 137:
        return SNOUTER
    else:
        return JOWLER


def roll_two_pigs():
    rolls = roll_a_pig() | roll_a_pig()

    if rolls == PINK | DOT:
        return PIGOUT
    elif rolls == TROTTER or rolls == RAZORBACK:
        return 20
    elif rolls == SNOUTER:
        return 40
    elif rolls == JOWLER:
        return 60
    elif rolls == PINK or rolls == DOT:
        return 1
    else:
        score = 0
        if rolls & PINK or rolls & DOT:
            score = score + 1
        if rolls & RAZORBACK or rolls & TROTTER:
            score = score + 5
        if rolls & SNOUTER:
            score = score + 10
        if rolls & JOWLER:
            score = score + 15
        # print "roll", rolls, "is", score
        return score


def roll_by_turns(turns):
    total_score = 0
    for turn in xrange(0, turns):
        score = roll_two_pigs()
        if score == PIGOUT:
            return 0
        else:
            total_score = total_score + score
    return total_score


class Game(object):
    def __init__(self):
        self.players = []
        self.scores = {}


    def add_player(self, player):
        self.players.append(player)


    def winner(self):
        for player in self.players:
            if player.score >= 100:
                return player
        return None


    def player_turn(self, player):
        score = 0
        other_scores = list(p.score for p in self.players if p is not player)
        while player.wants_to_roll(score, player.score, other_scores):
            rolls = roll_two_pigs()
            if rolls == PIGOUT:
                #print "player %s pigged out." % player.name
                return 0
            else:
                score = score + rolls
        # print "player %s scored %s" % (player.name, score)
        return score


    def play(self):
        while self.winner() is None:
            player = self.players[0]
            self.players = self.players[1:] + [player]

            player_score = self.player_turn(player)
            player.score = player.score + player_score
            # print "player %s new score is %s" % (player.name, player.score)
        #print "Final scores: %s" % ", ".join("Player {0.name}: {0.score}".format(player) for player in self.players)

