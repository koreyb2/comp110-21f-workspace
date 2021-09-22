"""UNC vs Duke Basketball Simulator!"""

__author__ = "730425339"

from random import randint
unc_score: int = 44
duke_score: int = 48
points: int = 0
probability: int = randint(1, 4)
probability_2: int = randint(1, 5)
player: str = ""
number: str = ""
game: int = 1
NAMED_CONSTANT = "\U0001F44B"


def main() -> None:
    """Beginning."""
    greet()
    enter_game(0)
    quit()


def greet() -> None:
    """Background."""
    global player
    global number
    player_name: str = str(input("What is your name? "))
    player = player_name
    print(f"{player}, you are a walk-on for the greatest basketball program of all time, UNC. By some miracle, Duke is currently winning against your team. Can you make the right decisions to win the game and become a campus legend?")
    jersey: str = str(input(f"What is your preferred jersey number {player}? "))
    number = jersey


def enter_game(x: int) -> int:
    """Entry point."""
    global unc_score
    global points
    global player
    global game
    print(f"You ready to go in, {player}?")
    print("1: Enter the game.")
    print("2: Stay on the bench.")
    print("3: Quit.")
    entry: int = int(input(f"Well, you ready or not, {player}? "))
    x = x + entry
    if x == 1:
        y: int = first_play(0)
        if y > 0:
            game_loop(0)
            if game == 2:
                second_play(points)
                game = game - 1
                game_loop(0)
                if game == 2:
                    third_play(points)
                    game = game - 1
                    benched(0)
                    game_loop(0)
                    if game == 2:
                        points = points + clutch_play(points)
                        game = game - 1
                        game_loop(0)
                        if game == 2:
                            last_play(points)
                            game == game + 1
                        if game == 1:
                            benched(0)
                            last_play(points)
                            game = game + 2
                        if game == 0:
                            game == game + 3
                    if game == 1:
                        benched(0)
                        last_play(points)
                        game = game + 2
                    if game == 0:
                        game = game + 3
                if game == 1:
                    benched(0)
                    points = points + clutch_play(points)
                    game_loop(0)
                    if game == 2:
                        last_play(points)
                        game == game + 1
                    if game == 1:
                        last_play(points)
                        game = game + 2
                    if game == 0:
                        game = game + 3
                if game == 0:
                    game = game + 3
            if game == 1:
                benched(0)
                third_play(points)
                game_loop(0)
                if game == 2:
                    points = points + clutch_play(points)
                    game = game - 1
                    game_loop(0)
                    if game == 2:
                        last_play(points)
                        game = game + 1
                    if game == 1:
                        benched(0)
                        last_play(points)
                        game = game + 2
                    if game == 0:
                        game = game + 3
                if game == 1:
                    benched(0)
                    last_play(points)
                    game = game + 2
                if game == 0:
                    game = game + 3
            if game == 0:
                game = game + 3
        else:
            game_loop(0)
            if game == 2:
                second_play(points)
                game = game - 1
                game_loop(0)
                if game == 2:
                    third_play(points)
                    game = game - 1
                    benched(0)
                    points = points + clutch_play(points)
                    game_loop(0)
                    if game == 2:
                        last_play(points)
                        game = game + 1
                    if game == 1:
                        last_play(points)
                        game = game + 2
                    if game == 0:
                        game = game + 3 
                if game == 1:
                    benched(0)
                    points = points + clutch_play(points)
                    game_loop(0)
                    if game == 2:
                        last_play(points)
                        game = game + 1
                    if game == 1:
                        last_play(points)
                        game = game + 2
                    if game == 0:
                        game = game + 3
                if game == 0:
                    game = game + 3
    if x == 2:
        print("Are you sure about that?")
        print("0: Yes")
        print("1: No")
        yes_or_no: int = int(input("Yes or no? "))
        if yes_or_no == 0:
            x = 3
        if yes_or_no == 1:
            print("Then get in the game!")
            y: int = first_play(0)
            if y >= 0:
                game_loop(0)
                if game == 2:
                    second_play(points)
                    game = game - 1
                    game_loop(0)
                    if game == 2:
                        third_play(points)
                        game = game - 1
                        benched(0)
                        game_loop(0)
                        if game == 2:
                            points = points + clutch_play(points)
                            game = game - 1
                            game_loop(0)
                            if game == 2:
                                last_play(points)
                                game = game + 1
                            if game == 1:
                                benched(0)
                                last_play(points)
                                game = game + 2
                            if game == 0:
                                game = game + 3
                        if game == 1:
                            benched(0)
                            points = points + clutch_play(points)
                            game_loop(0)
                            if game == 2:
                                last_play(points)
                                game = game + 1
                            if game == 1:
                                last_play(points)
                                game = game + 2
                            if game == 0:
                                game = game + 3
                        if game == 0:
                            game = game + 3
                    if game == 1:
                        benched(0)
                        points = points + clutch_play(points)
                        game_loop(0)
                        if game == 2:
                            last_play(points)
                            game = game + 1
                        if game == 1:
                            last_play(points)
                            game = game + 2
                        if game == 0:
                            game = game + 3
                    if game == 0:
                        game = game + 3
                if game == 1:
                    benched(0)
                    points = points + clutch_play(points)
                    game_loop(0)
                    if game == 2:
                        last_play(points)
                        game = game + 1
                    if game == 1:
                        last_play(points)
                        game = game + 2
                    if game == 0:
                        game = game + 3
                if game == 0:
                    game = game + 3
    if x == 3:
        x = x
    return x


def game_loop(x: int) -> int:
    """Game loop."""
    global game
    x = 0
    print(f"The score is UNC {unc_score} - Duke {duke_score}")
    print(f"Your Total Points: {points}")
    print("What do you want to do next?")
    print("1: Continue to the next play.")
    print("2: Go to the bench.")
    print("3: Quit")
    game_loop: int = int(input("Choose option: "))
    if game_loop == 1:
        game = game + 1
        return x
    if game_loop == 2:
        game = 1
        return x
    if game_loop == 3:
        game = game - 1
        return x
    return x


def first_play(y: int) -> int:
    """First Play."""
    global unc_score
    global points
    y = 0
    print("The ball has been passed to you. What will you do?")
    print("1: Shoot contested shot. Probability: 25%")
    print("2: Make long pass to open player. Probability: 50%")
    print("3: Make easy pass to teammate. Probability: 75%")
    first: int = int(input("What play will you make? "))
    if first == 1:
        if probability == first:
            y = 1
            print(f"Number {number} from way downtown!")
            unc_score = unc_score + 3
            points = points + 2
            return y
        else:
            print(f"Bad decision here by number {number}.")
            return y
    if first == 2:
        if probability > first:
            y = 1
            print(f"What a pass by number {number}!")
            unc_score = unc_score + 2
            points = points + 1
            return y
        else:
            print(f"And a turnover here by {player}")
            return y
    if first == 3:
        if probability <= first:
            y = 1
            print(f"Good pass by {player}!")
            unc_score = unc_score + 2
            points = points + 1
            return y
        else:
            print("Great play by the defender on what should have been an easy pass.")
            return y
    return y


def second_play(z: int) -> int:
    """The next decision."""
    global unc_score
    global points
    print("UNC got the ball back from Duke.")
    print("1: Make easy pass to teammate. Probability: 80%")
    print("2: Drive to the basket. Probability: 60%")
    print("3: Pull up jumpshot. Probability: 50%")
    second: int = int(input("What play do you make now? "))
    if second == 1:
        if second < probability_2:
            print(f"Good pass by {player}")
            z = z + 1
            unc_score = unc_score + 2
            points = points + 1
            return z
        else:
            print(f"A bad pass from {player}")
            return z
    if second == 2:
        if second < probability_2:
            print(f"And {player} gets all the way to the hoop here for the score!")
            z = z + 2
            unc_score = unc_score + 2
            points = points + 2
            return z
        else:
            print(f"Number {player} is not able to finish at the rim.")
            return z
    if second == 3:
        if second > probability_2:
            print(f"A great shot by {player} of UNC!")
            z = z + 3
            unc_score = unc_score + 3
            points = points + 3
            return z
        else:
            print(f"A miss here by number {number}")
            return z
    return z


def third_play(b: int) -> int:
    """Clutch play!"""
    global duke_score
    global unc_score
    global points
    b = points
    duke_score = duke_score + 2
    print("Duke scored a big bucket to keep pace in this contest.")
    print("Can you make the right play in the clutch?")
    print("1: Make easy pass for the score. Probability: 100%")
    print("2: Drive to the basket. Probability: 60%")
    print("3: Pull up for 3. Probability: 50%")
    third: int = int(input("Choose option: "))
    if third == 1:
        points = points + 1
        unc_score = unc_score + 2
        print(f"{player} made the right pass here.")
    if third == 2:
        if third < probability_2:
            points = points + 2
            unc_score = unc_score + 2
            print(f"{player} gets to the hoop for the score.")
        else:
            print(f"Number {number} can't finish at the rim.")
    if third == 3:    
        if third >= probability:
            points = points + 3
            unc_score = unc_score + 3
            print(f"{player} makes a huge bucket from downtown!")
        else:
            print(f"Number {number} probabaly should not have shot that one.")
    return b


def benched(x: int) -> int:
    """Taking a break."""
    global unc_score
    global duke_score
    unc_score = unc_score + 4
    duke_score = duke_score + 4
    if points == 0:
        print(f"{player} is still on the bench in this tight contest.")
    if points >= 1 and points <= 4:
        print(f"{player} going to the bench after a short stint in the game.")
    if points > 4:
        print(f"{player} going back to the bench after a stellar performance here.")
    return x


def clutch_play(x: int) -> int:
    """A big play."""
    global unc_score
    print(f"{player} is in the game down the stretch and could be a key part of UNC winning this game.")
    print("Your total points up to this point will determine how effective you are in this play.")
    if x < 3:
        print(f"Number {number} did not seem to be comfortable in that play and resulted in a turnover.")
        x = 0
    if x >= 3 and x < 6:
        print(f"Number {number} comes up with a huge bucket here to help Carolina.")
        x = 2
        unc_score = unc_score + 2
    if x >= 6:
        print(f"Number {number} from way downtown to get the crowd into it here at the Dean Dome.")
        x = 3
        unc_score = unc_score + 3
    return x


def last_play(x: int) -> int:
    """The Final Play."""
    global points
    global unc_score
    print("The end of the game is close and the crowd is hype. Continue the chant for extra points.")
    print("TAR")
    heels: str = str(input("Continue the chant: "))
    if heels == "HEELS" or heels == "Heels" or heels == "heels":
        points = points + 3
    if points < 3:
        print(f"{player} missed the shot here at the end of the game.")
    if points >= 3 and points < 8:
        print(f"And {player} gets an easy layup.")
        unc_score = unc_score + 2
    if points >= 8:
        print(f"{player} throws it down with authority.")
        unc_score = unc_score + 2
    return x


def quit() -> None:
    """End of the game."""
    global unc_score
    global duke_score
    global points
    global player
    winner_score: int 
    loser_score: int
    winner: str = ""
    print(f"Final: UNC {unc_score} - Duke {duke_score}")
    if unc_score > duke_score:
        winner = "UNC"
        winner_score = unc_score
        loser_score = duke_score
    if unc_score < duke_score:
        winner = "Duke"
        winner_score = duke_score
        loser_score = unc_score
    if unc_score == duke_score:
        print(f"And the game ends in a tie despite {player}'s best efforts.")
    difference = winner_score - loser_score
    if unc_score != duke_score:
        print(f"And {winner} wins by {difference}.")
    if unc_score > duke_score and points > 4:
        print(f"The player of the game has to be number {number}, {player} from UNC!")
    print(f"Total points for {player}: {points}")
    print("Game over!")
    print(f"Goodbye, {player} {NAMED_CONSTANT}.")


if __name__ == "__main__":
    main()