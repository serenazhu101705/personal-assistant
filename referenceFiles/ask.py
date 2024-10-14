#hates, compliments, isname, none

#name
if ("whats" in ask and "name" in ask) or "who" in ask:
	me = True if "my" in ask or "am" in ask else False
	if not me:
		status = "My manufacturer, Serena Zhu, named me after Harry Styles" if built_in else f"I was given this name by you"
		print(f"\nMy name is {name}. {status}. If you would like to change my name, just type in \"Harry, change your name.\"")
	else:
		print(f"\nYou've asked me to call you {player}. If you would like to change your name, just type in \"{name}, change my name.\"")
        
elif 'name' in ask and 'change' in ask:
	me = True if 'my' in ask else False
	ha = 'player' if me else 'name'
	globals()[ha] = string.capwords(input("Sure. What would you like to change it to?\n"))
	while globals()[ha] == '':
		print("Sorry, you must input a valid name.")
		globals()[ha] = string.capwords(input())
	ja = 'your' if me else 'my'
	print(f"Ok, {ja} new name is now {globals()[ha]}!")
	built_in = False if not me else built_in
	database()
	

