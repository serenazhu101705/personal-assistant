if ask == "leave some feedback":
	feedback = input("Sure. What would you like to say?\n")
	leaver = input("Please input your name.\n")
	while leaver == '':
		leaver = input("Sorry, you must input a valid name.\n")
	with open(directory + "feedback.txt", 'a') as f:
		f.write(f"\n{feedback} - {string.capwords(leaver)}\n")
	print("Thanks for the feedback!")
elif ask == "show me some reviews about yourself":
	feedback = module.read(directory + "feedback.txt", 'rl')
	feedback = [i.strip() for i in feedback if i.strip() != '']
	shown = set()
	while len(shown) != 5:
		shown.add(random.choice(feedback))
	for i in shown: print("\n" + i)
