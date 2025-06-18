players_done = False
players_bids = {}
while not players_done:
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  $"))
    players_bids[name] = bid
    yes_or_no = input("Are there any other bidders?: Type 'yes' or 'no':\n").lower()
    if yes_or_no == "no":
        players_done = True
    else:
        print("\n"*100)
max = 0
player = ""
for key in players_bids:
    if players_bids[key] > max:
        max = players_bids[key]
        player = key
print(f"The winner is {player} with a bid of ${max}")
