def helped(replacing):
        days = ask.replace(replacing, "").split()
        s = [i for i in days[1] if i in string.ascii_letters]
        days[1] = int(days[1][:-2]) if len(s) != 0 else int(days[1])
        months = list(calendar.month_name)
        days[0] = [i for i in range(len(months)) if months[i].lower() == days[0]][0]
        year_included = True if len(days) > 2 else False
        if not year_included:
                year = input("Which year?\n")
                while type(year) != int:
                        try: year = int(year)
                        except: year = input("That is not a valid year. Please try again\n")
                days.insert(0, year)
        else: days = [int(days[2])] + days[:2]
        return d.date(days[0], days[1], days[2])

if ask == "what time is it":
	print(f"\nIt is currently {d.time('%I:%M %p')}.")

if ask == "whats the date":
	print(f"\nToday is {today}.")
	
if "what day of the week is " in ask:
        day = str(helped("what day of the week is ")).split(", ")
        print(f"{day[1]}, {day[2]} is on a {day[0]}.")

if "how many days until" in ask: helped("how many days until ").calc_date(today)
