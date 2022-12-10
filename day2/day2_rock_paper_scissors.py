data = open("AdventOfCodeDay2Input.txt", "r")
rounds = [line.split("\n") for line in data.readlines()]

my_score_1 = 0
my_score_2 = 0

options = {
    "A":"rock",
    "B":"paper",
    "C":"scissors",
    "X":"rock",
    "Y":"paper",
    "Z":"scissors"
}

for round in range(0, len(rounds)):
    play = rounds[round]
    round_choices = play[0]

    opponent_choose = options[round_choices[0]]
    my_choose = options[round_choices[2]]
    my_choose_strategic = round_choices[2]

    def strategy(opponent, strategic_response):
        my_election = ""
        if strategic_response == "X": # necesito perder
            match opponent:
                case "rock":
                    my_election = "scissors"
                case "paper":
                    my_election = "rock"
                case "scissors":
                    my_election = "paper"
        elif strategic_response == "Y": # necesito empatar
            my_election = opponent
        elif strategic_response == "Z": # necesito ganar
            match opponent:
                case "rock":
                    my_election = "paper"
                case "paper":
                    my_election = "scissors"
                case "scissors":
                    my_election = "rock"
        return my_election
            

    def rock_paper_scissors_score(opponent, my):
        if  opponent == my:
            return 3
        elif opponent == "scissors" and my == "rock":
            return 6
        elif opponent == "paper" and my == "scissors":
            return 6
        elif opponent == "rock" and my == "paper":
            return 6
        else:
            return 0

    def points_per_election(choose):
        match choose:
            case "rock":
                return 1
            case "paper":
                return 2
            case "scissors":
                return 3

    my_score_1 += points_per_election(my_choose)
    my_score_1 += rock_paper_scissors_score(opponent_choose,my_choose)

    my_election_strategic = strategy(opponent_choose, my_choose_strategic)
    my_score_2 += points_per_election(my_election_strategic)
    my_score_2 += rock_paper_scissors_score(opponent_choose, my_election_strategic)

print(my_score_1)
print(my_score_2)