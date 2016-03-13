from pigs.game import roll_by_turns, Game
import pigs.players
import optparse


def create_player(spec):
    """
    Take a string of the form Class:arg1,arg2 and return result of pigs.players.Class(arg1, arg2)
    """

    player_class, arglist = spec.split(":")
    args = [spec] + list(int(arg) if arg.isdigit() else arg for arg in arglist.split(","))

    assert player_class in dir(pigs.players), "Player class %s not found." % player_class
    PlayerClass = getattr(pigs.players, player_class)
    assert issubclass(PlayerClass, pigs.players.Player), "Class %s is not of type Player" % player_class

    return PlayerClass(*args)


def main():
    parser = optparse.OptionParser()
    parser.add_option("--games", "-n", type="int", default=100)
    opts, specs = parser.parse_args()

    games = []
    wins = dict((spec, 0) for spec in specs)

    for n in range(opts.games):
        game = Game()
        for spec in specs:
            player = create_player(spec)
            game.add_player(player)

        game.play()
        wins[game.winner().name] += 1
        games.append(game)

    for spec, total in wins.items():
        print "Strategy %s win%%: %0.2f" % (spec, total*100.0/opts.games)



if __name__ == "__main__":
    main()

