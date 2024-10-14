#ask, CHANGE THE NAME THING PROBLEM
exec(open('../personal assistant/choices/ai/ask').read())

#talks list
months = [i for i in calendar.month_name if i != ""]
dayss = [i for i in range(1, 29)]
yearss = [i for i in range(2020,2031)]
weekdayss = "%s %s, %s" % (random.choice(months), random.choice(dayss), random.choice(yearss))
holidayss = []
for i in holidays:
	holidayss.append(holidays[i][0])
peopless = ["Serena Williams","Nick Jonas","Harry Styles","Justin Bieber","Selena Gomez","Donald Trump","Barack Obama","Stephen Curry"]

sorries = ["Sorry, I'm not sure I understand, %s. Please make sure you typed in the correct spelling and grammar." % player,"I'm still fairly new at this and don't know many commands. Make sure you typed in a command from the list.","Say that again, %s? Make sure you typed in the correct command." % player,"Sorry, I don't know that one. Make sure you typed in the correct command."]

talks2 = ['what time is it',"what's the date","what's your name","what's my name","what can we talk about","can you change your name","check the daily news.","check the weather for today.","open a website in chrome.","tell me a joke.","show me some recipes.","play a game.","check my contacts.","search something on google.","can I change my name","search up an image.","what day of the week is %s" % weekdayss, "when is %s" % random.choice(holidayss), "%s a file." % random.choice(["open","delete"]), "who is %s" % random.choice(peopless),"who are the most popular people on the internet","who has a birthday today","who has a birthday tomorrow","who am I","who are you","open the tutorial.","leave some feedback.","show me some reviews about yourself.","check MyCircle.", "show collected people"]

talks = [str.lower(i) for i in talks2]
for i in range(len(talks)):
    for el in j:
        if el in talks[i]:
            talks[i] = talks[i].replace(el,"")

elses = ["can i ","can you ","can we ","lets "]
for i in talks:
    for el in elses:
        if el + ask in talks or ask.replace(el,"") in talks:
            ask = ask.replace(el, '')
            good = True
            break
for i in talks:
    if i in ask or ask in i:
        good = True
        break
ai= ['what day of the week is', 'when is',"a file","who is","weather"]
for i in ai:
    if i in ask or ask in talks:
        good = True
        if i in ask:
            a_i = True
            File = i
            break
        else:
            a_i = False
    else:
        good = False
        a_i = False

#farewell
others = ["goodbye", "nothing","nada","see you","bye","see ya"]
farewell = module.TrueorFalse(others, ask)
if ask in others or farewell:
    selfc = False;compliment = False
    print("Goodbye %s! See you next time!" % player)
    again = "no"
        

#options, tutorial, feedback, compliments, and hate 
idk = ["what can", "what should","i dont know","idk"]
dontknow = module.TrueorFalse(idk,ask)
         
if dontknow or bored:
    print("Here is a list of things you can ask me:\n")
    things = random.sample(talks2,10)
    for i in things:
        if "." in i:
            print("%s, %s" % (name,i))
        else:
            print("%s, %s?" % (name, i))
    print("\nTo stop talking to %s, type in \"Goodbye %s\"" % (name, name))

if 'you' not in ask and 'i ' not in ask:
    hate = False
    selfh = False
if hate or selfh:
    hatesme = ["Oh no, you shouldn't say that","No, I think you are very nice","No don't say that, you are amazing!","No, I disagree. You are an amazing master!"]
    hates = ["Oh no, I'm sorry", "That's not very nice.","I'm sorry, I'll try harder","Please contact my manufacturer with concerns","I'm trying my best, %s" % player]
    if selfh:
        print(random.choice(hatesme))
    else:
        print(random.choice(hates))

if 'you' not in ask and 'i ' not in ask:
    compliment = False
if compliment or selfc:
    loves = ["That's great!","I like you too, %s" % player,"Wow, that's nice!","Awesome!","I think you're awesome too!","Wow, so humble!"]
    print(random.choice(loves))

if "tutorial" in ask:
    good = True
    exec(open("./tutorial.py").read())
    print("Ok, now what would you like to talk about?")

if "feedback" in ask:
    good = True
    exec(open("./feedback.py").read())
    print("Hi again! What would you like to do?")
if "reviews" in ask:
    good = True
    subprocess.call([opener,"../personal assistant/feedback.txt"])
    print("If you would like to leave a review, just ask, \"Harry, leave some feedback.\".")

#name
if ask == "whats your name"or ask == "who are you":
    if built_in:
        print("My name is Harry. I was given this name by my manufacturer, Serena Zhu. Although she claims the name just popped into her head one day, I suspect she named me after Harry Styles. If you would like to change my name, just type in \"Harry, can I change my name?\"")
    else:
        print("My name is %s. I was given this name by you, %s. Although I do have a built-in name, I like %s better. If you would like to change my name, just type in \"%s, can I change my name?\"" % (name, player, name,name))

if ask == "whats my name" or ask == "who am i":
    print("You have asked me to call you %s. I think this is a lovely name. If you wish to change your name though, just type in \"%s, can I change my name?\"" % (player, name))

if "change your name" in ask:
    good = True    
    print("Certainly, although I quite like %s. What would you like to change it to?" % name)
    name = string.capwords(input())
    built_in = False
    print("Alright, I like %s even better!" % name)
    with open("savefile.dat","wb") as f:
        pickle.dump([name, player, built_in],f, protocol = 2)

if 'change my name' in ask:
    print("Of course, %s. Although I can't change it legally, I can call you something else if you like. What would you like to change your name to?" % player)
    good = True
    player = string.capwords(input())
    print("Ok, from now on, I will call you %s!" % player)
    with open("savefile.dat","wb") as f:
        pickle.dump([name, player, built_in],f, protocol = 2)

harry = ["I'm listening.","I am your personal assistant, %s. What would you like me to do?" % name, "I'm here, %s." % player,"Hello, %s" % player,"What can I do for you, %s?" % player,"Right here, at your service","Wassup, bro?","Hola!","Aloha!"]
if empty or weird or isname or hey:
    print(random.choice(harry))



#options dictionary access and ai
interactives = ["tell me a joke","play a game","check my contacts","what time is it","whats the date"]
webs = ['check the daily news','show me some recipes']

if ask in interactives:
    for i in interactives:
        if i in ask:
            File = options[i]['file']
    stop = 'yes'
    while stop != 'no':
        try:
            exec(open(File).read())            
        except:
            print("Sorry, something went wrong. We'll try to fix the problem next time")
            stop = "no"
    good = True

    if ask != "whats the date" and ask != "what time is it":
        print("What would you like to talk about?")
if a_i:
    exec(open(options[File]['file']).read())


if "most popular people" in ask or "birthday" in ask and "today" in ask or "birthday" in ask and "tomorrow" in ask:
    good = True
    try:
        exec(open(options['who is']['file']).read())
    except:
        print("Sorry, you seem not to be connected to the internet.")

if "collected people" in ask:
    people = []
    for i in os.listdir("../personal assistant/choices/ai/people"):
        people.append(string.capwords(i.replace("-"," ")))
    if "random" in ask:
        ask = "who is %s" % random.choice(people).lower()
        a_i = True
        exec(open(options['who is']['file']).read())
    else:
        good = True
        people.sort()
        for i, el in enumerate(people, 1):
            print("%d. %s" % (i, el))
    
        

if ask in webs:
    for i in webs:
        if i in ask:
            website(options[i]["URL"])
    good = True


#websites
if "open a website in chrome" in ask:
    print("What website would you like to go to, %s?" % player)
    url = input()
    website(url)
if "search something on google" in ask:
    print("What would you like to look up?")
    look = input()
    look = look.replace(" ","+")
    url = 'https://www.google.com/search?q=' + look + '&oq=' + look + '&aqs=chrome.0.0l3.2802j0j4&sourceid=chrome&ie=UTF-8'
    website(url)
if "search up an image" in ask:
    print("Which image?")
    im = input()
    im = im.replace(" ","+")
    url = 'https://www.google.com/search?q=' + im +  '&safe=strict&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj-8K2VjpvqAhWVcc0KHQn1CsUQ_AUoAXoECB4QAw&biw=1038&bih=576'
    website(url)

if ask == "reset":
    good = True
    accessed = module.password("harryrules",2)
    if accessed:
        try:
            os.remove("./savefile.dat")
            print("File deleted.")
        except:
            print("File does not exist.")

if "mycircle" in ask:
    website("""http://filter.meetcircle.com/teen/?filtered=www.spotify.com&cat=Custom&catid=0&reason=blocked
""")

kk = [empty, weird, isname, good, hey, bored, selfc, selfh, compliment, hate,a_i,farewell, dontknow]

#error
if True not in kk and ask not in others:
    example = random.choice(talks2)
    if "." in example:
        a = ""
    else:
        a = "?"
    Example = 'Ex. "%s, %s%s"' % (name, example, a)
    
    print(random.choice(sorries),Example)
