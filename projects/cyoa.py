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


def main() -> None:
    """Beginning."""
    greet()
    enter_game(0)


def greet() -> None:
    """Background."""
    global player
    global number
    player_name: str = str(input("What is your name? "))
    player = player_name
    print(player + ", you are a walk-on for the greatest basketball program of all time, UNC. By some miracle, Duke is currently winning against your team. Can you make the right decisions to win the game and become a campus legend?")
    jersey: str = str(input("What is your preferred jersey number " + player + "? "))
    number = jersey


def enter_game(x: int) -> int:
    """Entry point."""
    global unc_score
    global points
    global player
    print("You ready to go in, " + player + "?")
    print("1: Enter the game.")
    print("2: Stay on the bench.")
    print("3: Quit.")
    entry: int = int(input("Well, you ready or not, " + player + "? "))
    x = x + entry
    if x == 1:
        y: int = first_play(0)
        if y > 0:
            points = points + 1
            if y > 1:
                points = points + 1
            unc_score += 3
            print("And the score is now UNC " + str(unc_score) + " - Duke " + str(duke_score))
            if move_on(0) == 1:
                second_play(points)
                if move_on(0) == 1:
                    third_play(points)
                    move_on(0)
                if move_on(0) == 2:
                    benched(0)
                if move_on(0) == 3:
                    quit()
            if move_on(0) == 2:
                benched(0)
            if move_on(0) == 3:
                quit()
    if x == 2:
        print("Are you sure about that?")
        print("0: Yes")
        print("1: No")
        yes_or_no: int = int(input("Yes or no? "))
        if yes_or_no == 0:
            quit()
        if yes_or_no == 1:
            print("Then get in the game!")
            y: int = first_play(0)
            if y > 0:
                points = points + 1
                if y > 1:
                    points = points + 1
                unc_score += 3
                print("And the score is now UNC " + str(unc_score) + " - Duke " + str(duke_score))
                a: int = move_on(0)
                if a == 1:
                    second_play(points)
                    if a == 1:
                        third_play(points)
                        a
                    if a == 2:
                        benched(0)
                    if a == 3:
                        quit()
                if a == 2:
                    benched(0)
                if a == 3:
                    quit()
    if x == 3:
        quit()
    return x


def move_on(x: int) -> int:
    """Game loop."""
    x = 0
    print("What do you want to do next?")
    print("1: Continue to the next play.")
    print("2: Go to the bench.")
    print("3: Quit")
    game_loop: int = int(input("Choose option: "))
    if game_loop == 1:
        x = x + 1
        return x
    if game_loop == 2:
        x = x + 2
        return x
    if game_loop == 3:
        x = x + 3
        return x


def first_play(y: int) -> int:
    """First Play."""
    global unc_score
    y = 0
    print("The ball has been passed to you. What will you do?")
    print("1: Shoot contested shot. Probability: 25%")
    print("2: Make long pass to open player. Probability: 50%")
    print("3: Make easy pass to teammate. Probability: 75%")
    print("4: Quit.")
    first: int = int(input("What play will you make? "))
    if first == 1:
        if probability == first:
            y = 1
            print("Number " + number + " from way downtown!")
            unc_score = unc_score + 3
            return y
        else:
            print("Bad decision here by number " + number + ".")
            return y
    if first == 2:
        if probability > first:
            y = 1
            print("What a pass by number " + number + "!")
            unc_score = unc_score + 2
            return y
        else:
            print("And a turnover here by " + player)
            return y
    if first == 3:
        if probability <= first:
            y = 1
            print("Good pass by " + player + "!")
            return y
        else:
            print("Great play by the defender on what should have been an easy pass.")
            return y
    if first == 4:
        quit()


def second_play(z: int) -> int:
    """The next decision."""
    global unc_score
    print("UNC got the ball back from Duke.")
    print("1: Make easy pass to teammate. Probability: 80%")
    print("2: Drive to the basket. Probability: 60%")
    print("3: Pull up jumpshot. Probability: 50%")
    print("4: Quit")
    second: int = int(input("What play do you make now? "))
    if second == 1:
        if second < probability_2:
            print("Good pass by " + player)
            z = z + 1
            unc_score = unc_score + 2
            return z
        else:
            print("A bad pass from " + player)
            return z
    if second == 2:
        if second < probability_2:
            print("And " + player + " gets all the way to the hoop here for the score!")
            z = z + 2
            unc_score = unc_score + 2
            return z
        else:
            print("Number " + number + " is not able to finish at the rim.")
            return z
    if second == 3:
        if second > probability_2:
            print("A great shot by " + player + " of UNC!")
            z = z + 3
            unc_score = unc_score + 3
            return z
        else:
            print("A miss here by number " + number)
            return z


def third_play(b: int) -> int:
    """Clutch play!"""
    global duke_score
    duke_score = duke_score + 2
    print("Duke scored a big bucket to keep pace in this contest.")
    print("Your adventure points up to this point will decide how clutch you are in crunch time.")


def benched(x: int) -> int:
    


def quit() -> None:
    global unc_score
    global duke_score
    global points
    global player
    print("Final: UNC " + str(unc_score) + " - Duke " + str(duke_score))
    if unc_score > duke_score:
        winner: str = "UNC"
        winner_score: int = unc_score
        loser: str = "Duke"
        loser_score: int = duke_score
    else:
        winner: str = "Duke"
        winner_score: int = duke_score
        loser: str = "UNC"
        loser_score: int = unc_score
    difference: int = winner_score - loser_score
    print("And " + winner + " wins by " + str(difference) + "!")
    if unc_score > duke_score and points > 4:
        print("The player of the game has to be number " + number + ", " + player + " from UNC!")
    print("Total points for " + player + ": " + str(points))
    print("Game over!")


if __name__ == "__main__":
    main()