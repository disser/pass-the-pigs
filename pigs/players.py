import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def wants_to_roll(self, turn_score, total_score, other_scores):
        assert False


class FiftyFifty(Player):
    def wants_to_roll(self, turn_score, total_score, other_scores):
        return random.random() < 0.50


class Threshold(Player):
    def __init__(self, name, threshold):
        Player.__init__(self, name)
        self.threshold = threshold

    def wants_to_roll(self, turn_score, total_score, other_scores):
        if turn_score < self.threshold:
            return True
        else:
            return False

