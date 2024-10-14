go = True
while go:
	print("What kind of joke would you like?\n")
	choices = [f"A {name} joke", "A fun riddle"]
	for i, el in enumerate(choices, 1):
		print(f"{i}. {el}")
	choice = module.numbers(1, len(choices))

	jokefile = directory + ('jokes.py' if choice == 1 else 'riddles.py')
	lines = module.read(jokefile, 'rl')
	laugh = random.choice(lines)
	print(laugh.replace(":", "\n"))
	go = module.yesorno("Would you like to hear another joke?")

