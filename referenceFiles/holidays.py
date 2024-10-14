if 'ask' in globals():
	ask = string.capwords((ask.replace("when is ", '')))
	normals = [(holidays[i][0], i) for i in holidays if type(holidays[i][0]) == str]
	specials2 = [(holidays[i], i) for i in holidays if type(holidays[i][0]) == list]
	for i in specials2:
		for el in [el[0] for el in i[0]]:
			normals.append((el, i[1]))
	day = [i for i in normals if module.strreplace(i[0], j) == ask][0]
	print(f"\n{day[0]}, {today.year}, is on {day[1]}.")
else:
	def holiday(month, week_day, first = True):
	    week_day = week_day - 1
	    r = list(calendar.monthrange(today.year, month))[1]
	    days = [i for i in range(1, r + 1) if calendar.weekday(today.year, month, i) == week_day]
	    return min(days) if first else max(days)

	holidays = {'January 01': ["New Year's Day", 'Welcome to 2021!'], 'January 20': ['Martin Luther King Jr. Day', 'Celebrating one of the most influential figures in US history and recognizing the civil rights movement.'], 'February 14': ["Valentine's Day", '"Being deeply loved by someone gives you strength, while loving someone deeply gives you courage." – Lao Tzu, Philosopher'], 'February 17': ["George Washington's Birthday", 'Honoring our heroic founding father and one of the most import figures in American History.'], 'May 31': ['Memorial Day', "Mourning our country's heroes with this special national holiday."], 'July 04': ['Independence Day', 'Celebrating 245 years of greatness. Happy birthday America!'], 'September 06': ['Labor Day', 'Enjoy a day off and start the first day of school tomorrow!'], 'October 12': [['Columbus Day', "Don't know why we celebrate this holiday, but as of now, it is still a national holiday."], ['Justin\'s Birthday', 'fatty patty 2.0 is stupid fat ugly zitty']], 'October 17': ["Serena's Birthday", "Happy Birthday to the creator of this program! She is so awesome!"],'November 11': ["Veteran's Day", 'Honoring the brave men and women who stood up and gave their lives for us.'], 'November 25': ['Thanksgiving', 'Remembering the first thanksgiving dinner with this national holiday and honoring the brave pilgrims that came to America almost 400 years ago.'], 'December 25': ['Christmas', "It's the most wonderful time of the year!"], 'December 31': ["New Year's Eve", 'Countdown to 2022!']}
	
	todays_date = (str(today).split(",")[1].strip()).split()
	holiday = [holidays[i] for i in holidays if f"{todays_date[0]} {todays_date[1]}" == i or f"{todays_date[0]} 0{todays_date[1]}" == i]
	if len(holiday) > 0:
		holiday = holiday[0]
		h = [(holiday[0], holiday[1])] if type(holiday[0]) == str else [tuple(i) for i in holiday]

		for i in h:
			wish = "Merry" if i[0] == "Christmas" else "Happy"
			print(f"\n{wish} {i[0]}!")
			print(f"\nA special note from {name}'s team:\n{i[1]}\n")
