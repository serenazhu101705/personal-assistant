game_directory = '../programs/'
games = [i.replace(".py", '') for i in os.listdir(game_directory)]
for i, el in enumerate(games, 1):
    print(" %d. %s\n" % (i, el))
game_choice = input(f"Choose a game, {player}.\n")
y = [str(i) for i in range(1,len(games)+1)]
while game_choice not in y and game_choice not in games:
    game_choice = input("Please choose a valid game.\n")
try: game_choice = games[int(game_choice) - 1]
except: pass
game_file = game_directory + game_choice + ".py"
exec(open(game_file).read())
