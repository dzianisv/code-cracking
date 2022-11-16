stream = [
  ["productguy", 0], # 0

  ["igrav", 1],

  ["igrav", 2],

  ["pilot764", 4],

  ["igrav", 5],

  ["productguy", 8],

  ["igrav", 9],

  ["productguy", 9],

  ["productguy", 10],

  ["sand", 11],

  ["productguy", 12],

  ["sand", 13],

  ["productguy", 14],

  ["sand", 15],

  ["igrav", 16],

  ["productguy", 17],

  ["mage41", 19],

  ["LordAeron", 20], # 2

  ["mage41", 35] # 5
]

reference_scoreboard = [
  [
    "igrav,3",
    "pilot764,1",
    "productguy,1"
  ],
  [
    "igrav,4",
    "productguy,5",
    "sand,2",
    "pilot764,1"
  ],
  [
    "productguy,7",
    "igrav,5",
    "sand,3",
    "LordAeron,1",
    "mage41,1",
    "pilot764,1"
  ],
  [
    "productguy,7",
    "igrav,5",
    "sand,3",
    "LordAeron,1",
    "mage41,1",
    "pilot764,1"
  ],
    [
    "productguy,7",
    "igrav,5",
    "sand,3",
    "LordAeron,1",
    "mage41,1",
    "pilot764,1"
  ],
[
    "productguy,7",
    "igrav,5",
    "sand,3",
    "LordAeron,1",
    "mage41,2",
    "pilot764,1"
  ]
]


def build_leaderboard(stream):
    scores = dict()
    week = 0
    scoreboard = []

    # o(1) * O(N) 

    i = 0
    while i < len(stream):
        user,timestamp = stream[i]
        if week == timestamp // 7:
            if user not in scores:
                scores[user] = 1
            else:
                scores[user] += 1
            i += 1
        else:
            scoreboard.append([ f"{user},{score}" for user, score in scores.items()])
            week += 1
    else:
        scoreboard.append([ f"{user},{score}" for user, score in scores.items()])

    return scoreboard        

my_scoreboard = build_leaderboard(stream)
print(my_scoreboard)
print(len(my_scoreboard))

assert len(my_scoreboard) == len(reference_scoreboard)
for i in range(len(my_scoreboard)):
    for r in my_scoreboard[i]:
        assert r in reference_scoreboard[i]