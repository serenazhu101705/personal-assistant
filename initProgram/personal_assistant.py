import webbrowser, module, os, random, string, time, calendar, pickle, subprocess, sys, requests, getpass
from datetime import datetime, date
#from bs4 import BeautifulSoup


#dictionary and opener for files
options = {'check the daily news':{'URL':'https://www.cnn.com/'},
'weather':{'file':'../personal assistant/choices/ai/weather'},
'open a website in chrome':{'file':'../personal assistant/choices/chrome'},
'tell me a joke':{'URL':'https://www.ajokeaday.com/','file':'../personal assistant/choices/joke'},
'show me some recipes':{'URL':'https://www.foodnetwork.com/recipes'},
'play a game':{'file':'../personal assistant/choices/game','directory':'../programs/'},
'check my contacts':{'file':'../personal assistant/choices/contact','directory2':'../personal assistant/contacts/'},
'what time is it':{'file':'../personal assistant/choices/ai/date'},
'whats the date':{'file':'../personal assistant/choices/ai/date'},
'what day of the week is':{'file':'../personal assistant/choices/ai/date'},
'when is':{'file':'../personal assistant/choices/ai/holidays'},
'a file':{'file':'../personal assistant/choices/ai/file'},
'who is':{'file':'../personal assistant/choices/ai/person'}}

opener = "open" if sys.platform == "darwin" else "xdg-open"


#functions
def scrape(url):
    page = requests.get(url)
    global soup
    soup = BeautifulSoup(page.content, 'html.parser')
    
def holiday(month,last_or_first,day):
    m = []
    r = list(calendar.monthrange(int(datetime.strftime(date.today(),"%Y")),month))[1]
    for i in range(1,r):
        if calendar.weekday(int(datetime.strftime(date.today(),"%Y")),month,i) == day:
            m.append(i)
    if last_or_first == 'last':
        day = max(m)
    if last_or_first == 'first':
        day = min(m)
    return day

def end(action):
    print("\nWould you like to",action + "?")
    again = input().lower()
    while again != 'yes' and again != 'no':
        print("Sorry, I'm not sure I understand. Please try again.")
        again = input().lower()
    return again

def website(url):
    print('Ok, please wait while this loads')
    webbrowser.open(url)

new = False
try:
    with open("savefile.dat","rb") as f:
        name, player, built_in = pickle.load(f)
except:
    new = True
    
#GET READY FOR HARRY!!!
if new:
    exec(open("./tutorial.py").read())
    print("""Oh hello there, I didn't see you! Let me introduce myself.
I am your personal assistant. Now I don't quite have a name yet, so
I was hoping you would do the honors. What would you like to name me?""")

    name = string.capwords(input())
    if name != "" and name != "I Don't Know":
        print("\nI guess my name is now",name)
        built_in = False
    else:
        print("Well, I do have a built-in name. You can call me Harry from now on.")
        name = "Harry"
        built_in = True
              
    print("I would like to know your name as well. What is yours?")
    player = string.capwords(input())
    if player==name:
        print("Hey, we have the same name!")

    bosses = ["serena zhu","serena","serena rui","serena rui zhu","your boss","your master","your manufacturer","the awesomest","the coolest"]

    if player.lower() in bosses:
        print("Would you like me to call you Boss Master Serena?")
        boss = module.yesorno()
        if boss == "yes":
            player = "Boss Master Serena"

    print("\nHey, %s;)" % (player))
    with open("savefile.dat","wb") as f:
        pickle.dump([name, player, built_in],f, protocol = 2)
else:
    print("Welcome back, %s!" % string.capwords(player))
print("\n\nWhat do you want to talk about?")
print("\nFor a list of things you can talk about with me, just type in, \"%s, what can we talk about?\"" % name)
ask = ""
exec(open("../personal assistant/choices/ai/holidays").read())
again = "yes"
while again != "no":
    exec(open("../personal assistant/choices/talk to me").read())
