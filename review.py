
class Team:
    def __init__(self, name):
        self.name = name
        self.played = 0
        self.won = 0
        self.lost = 0
        self.tied = 0
        self.points = 0
        self.scored = 0
        self.given = 0
        self.faced = 0
        self.bowled = 0
teams = {}
while True:
    try:
        n = int(input("Enter no of teams: "))
        if n >= 2:
            break
        print("Min 2teams required.")
    except ValueError:
        print("Enter valid number.")

for i in range(n):
    while True:
        name = input("Enter team name: ").strip()

        if name == "":
            print("Name cannot be empty")
        elif name.lower() in [x.lower() for x in teams]:
            print("Duplicate team given")
        else:
            teams[name] = Team(name)
            break
total_matches = n*(n - 1)
pair_count = {}
match = 1

while match <= total_matches:
    print("\nMatch", match)
    a = input("First team: ").strip()
    b = input("Second team: ").strip()
    if a not in teams or b not in teams:
        print("Team does not exist.")
        continue
    if a == b:
        print("A team cannot play against itself.")
        continue
    pair = tuple(sorted([a, b]))
    if pair not in pair_count:
        pair_count[pair] = 0
    if pair_count[pair] >= 2:
        print("These teams already played twice.")
        continue

    valid = True
    data = []
    for team in [a, b]:
        try:
            runs = int(input(team + " runs: "))
            wickets = int(input(team + " wickets lost: "))
            overs = int(input(team + " completed overs: "))
            balls = int(input(team + " remaining balls: "))
            if runs < 0 or wickets < 0 or wickets > 10:
                valid = False
            if overs < 0 or overs > 20:
                valid = False
            if balls < 0 or balls > 5:
                valid = False
            if overs == 20 and balls != 0:
                valid = False
            data.append([runs, wickets, overs, balls])
        except ValueError:
            valid = False
            break

    if not valid:
        print("Invalid match data. Enter the match again.")
        continue

    r1, w1, o1, b1 = data[0]
    r2, w2, o2, b2 = data[1]
    balls1 = o1 * 6 + b1
    balls2 = o2 * 6 + b2
    if w1 == 10 and balls1 < 120:
        balls1 = 120
    if w2 == 10 and balls2 < 120:
        balls2 = 120
    t1 = teams[a]
    t2 = teams[b]
    t1.played += 1
    t2.played += 1
    t1.scored += r1
    t1.given += r2
    t2.scored += r2
    t2.given += r1
    t1.faced += balls1
    t1.bowled += balls2
    t2.faced += balls2
    t2.bowled += balls1
    if r1 > r2:
        t1.won += 1
        t1.points += 2
        t2.lost += 1
        print(a, "wins")
    elif r2 > r1:
        t2.won += 1
        t2.points += 2
        t1.lost += 1
        print(b, "wins")
    else:
        t1.tied += 1
        t2.tied += 1
        t1.points += 1
        t2.points += 1
        print("Match tied")

    pair_count[pair] += 1
    match += 1
table = []
for team in teams.values():
    if team.faced > 0:
        rate1 = team.scored * 6 / team.faced
    else:
        rate1 = 0
    if team.bowled > 0:
        rate2 = team.given * 6 / team.bowled
    else:
        rate2 = 0
    nrr = rate1 - rate2
    table.append([
        team.points, nrr, team.name, team.played,
        team.won, team.lost, team.tied,
        team.scored, team.given,
        team.faced / 6, team.bowled / 6
    ])

for i in range(len(table)):
    for j in range(0, len(table) - i - 1):

        if table[j][0] < table[j + 1][0]:
            temp = table[j]
            table[j] = table[j + 1]
            table[j + 1] = temp

        elif table[j][0] == table[j + 1][0]:
            if table[j][1] < table[j + 1][1]:
                temp = table[j]
                table[j] = table[j + 1]
                table[j + 1] = temp

print("\nFINAL POINTS TABLE")
print("{:<5} {:<15} {:<7} {:<5} {:<5} {:<5} {:<7} {:<10} {:<10} {:<12} {:<12} {:<8}".format(
    "Pos", "Team", "Played", "Won", "Lost", "Tied",
    "Points", "Scored", "Given", "Overs Faced",
    "Overs Bowled", "NRR"
))

i = 1
for row in table:
    print("{:<5} {:<15} {:<7} {:<5} {:<5} {:<5} {:<7} {:<10} {:<10} {:<12.2f} {:<12.2f} {:<8.3f}".format(
        i, row[2], row[3], row[4], row[5], row[6],
        row[0], row[7], row[8], row[9], row[10], row[1]
    ))
    i += 1




