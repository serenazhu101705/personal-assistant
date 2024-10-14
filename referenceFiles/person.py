if a_i:
	person = ask.replace("who is ","")
	p = person
	person = person.replace(" ","-")
	try:
		try:
			with open('/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s/%s.dat' % (person, person), 'rb') as f:
				elems, stats, j, l, juices, heading = pickle.load(f)
			print('collected')
		except:
			if not os.path.exists("/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s" % person):
				os.mkdir("/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s" % person)
			url = "https://www.famousbirthdays.com/people/%s.html" % person
			scrape(url)
			results = soup.find(class_="bio col-sm-7 col-md-8 col-lg-6")
			elems = results.find_all("p")
			heading = soup.find("h1").text
			results = soup.find_all(class_="col-xs-6 col-md-12")
			images = soup.find(class_='img1')
			images = list(images)[3]
			images = list(images)
			l = []
			for i in images:
				try:
					k = i.findChildren('img')
					l.append(k[0]['src'])
				except:
					continue
			for i in range(len(results)):
				results[i] = results[i].text.replace("\n","")
			for i in ["Birthday","Birthplace","Age","Birth Sign"]:
				for el in range(len(results)):
					results[el] = results[el].replace(i,"").strip()
			birthday = soup.find(class_="stat box").text;k = birthday.split()
			module.remove(k, 'Birthday', "Happy", "Birthday!")
			months = [str.lower(i) for i in list(calendar.month_name) if i !='']
			for i in months:
				if i in k[0].lower():
					k[0] = str.capitalize(i)

			j = " ".join(k)
			results[0] = j
			stats = {"Birthday: ":results[0],"Birthplace: ":results[1],"Age: ":results[2],"Birth Sign: ":results[3]}
			low = soup.find(class_='popularity pop2')
			k = low.find(class_='row')
			juice = k.find_all(class_='btn-rank-wrapper col-xs-6 col-sm-3 col-md-2 col-lg-6')
			juices = []
			for i in juice:
				h = i.text.replace('#'," #")
				h = h.replace("\n\n","")
				juices.append(h)
			elems = [i.text for i in elems]
			with open("/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s/%s.dat" % (person, person),"wb") as f:
				pickle.dump([elems, stats, j, l, juices, heading],f, protocol = 2)
		print("\nHere's what I found on Famous Birthdays:\n\n")
		print(heading)
		for i,el in stats.items():
			print(i,el)
		print("\n")
		for i in elems:
			print(i,"\n")
		for i in juices:
			print(i)
		print("\nWould you like to see a picture of %s?" % string.capwords(p))
		pics = module.yesorno()
		if pics == 'yes':
			if len(os.listdir('/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s' % person)) != 1:
				for i in os.listdir('/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s' % person):
						k = subprocess.call([opener, '/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s/%s' % (person, i)])
			else:
				j = [str(i) for i in range(len(l))]
				for i in range(len(l)):
					nam = '/home/serena/Nextcloud/python/personal assistant/choices/ai/people/%s/%s.jpg' % (person, j[i])
					url = l[i]
					r = requests.get(url)
					with open (nam, 'wb') as f:
						k = f.write(r.content)
					k = subprocess.call([opener,nam])
		print("What would you like to talk about?")
	except:
		print("Sorry, I couldn't find anyone named %s. Please check your internet connection or spelling and try again." % (string.capwords(p)))

if "most popular people" in ask:
    try:
        with open("../personal assistant/choices/ai/popular","rb") as f:
            results = pickle.load(f)
            print("collected\n")
    except:
        scrape('https://www.famousbirthdays.com/most-popular-people.html')
        results = soup.find_all(class_= "face person-item clearfix")
        for i in range(len(results)):
            results[i] = results[i].text.replace("\n\n\n","\n")
            results[i] = results[i].replace("\n\n","\n")
        with open("../personal assistant/choices/ai/popular","wb") as f:
            pickle.dump(results, f, protocol = 2)
    print("Here's what I found on famous birthdays: \n")
    for i in range(10):
        print(results[i])
    print("Would you like to see the full list?")
    more = module.yesorno()
    if more == "yes":
        for i in range(10,len(results)):
            print(results[i])
    print("What would you like to talk about?")
if "birthday" in ask and "today" in ask:
    scrape("https://www.famousbirthdays.com")
    results = soup.find_all(class_="face face person-item")
    results += soup.find_all(class_="face face person-item hidden-xs")
    for i in range(len(results)):
    	results[i] = results[i].text.replace("\n","")
    print("Happy birthday to:\n")
    for i in results:
        print(i)
if "birthday" in ask and "tomorrow" in ask:
    scrape("https://www.famousbirthdays.com")
    results = soup.find_all(class_='face person-item-small')
    results += soup.find_all(class_='face person-item-small hidden-xxs')
    for i in range(len(results)):
    	results[i]= results[i].text.replace("\n"," ")
    print("Tomorrow's birthdays: \n")
    for i in results:
        print(i,"\n")

good = True
