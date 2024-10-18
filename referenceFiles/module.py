from tkinter import filedialog, messagebox
import tkinter, subprocess, os, sys, getpass, subprocess, webbrowser, sys


def read(file, function):
    "Reads file. \"r\" for file.read() and \"rl\" for file.readlines()"
    f = open(file)
    l = f.readlines() if function != "r" else f.read()
    f.close()
    return l

opener = "open" if sys.platform == "darwin" else "xdg-open"    
class file:
    "Open, delete, or exectue files"
    def __init__(self, delete = False, ):
        self.delete = delete
        self.delete2 = 'delete' if self.delete else 'open'
    def open_or_del(self):
        while True:
            window = tkinter.Tk()
            window.geometry("1x1")
            self.dir1 = filedialog.askopenfilename()
            if not self.delete: subprocess.call([opener, self.dir1]) 
            else:
                delete = messagebox.askyesno(title = 'Confirm Action', message = f'Are you sure you want to delete {self.dir1}?')    
                if delete: os.remove(self.dir1)
            open_or_del_again = messagebox.askyesno(title = f"{str.capitalize(self.delete2)} Again?", message = "Would you like to open another file?")
            window.destroy()
            if not open_or_del_again:
                break
        
    def execute(self):
        exec(open(self.dir1).read())
    def change_dir(self, newdir):
        sys.path.append(newdir)

website = lambda url: webbrowser.open(url)

#hi i added an argument here so you may need to change some things in your
#other programs
def yesorno(question):
    "Returns \"True\" for yes and \"False\" for no."
    answer = input(question + '\n').lower()
    while answer != 'yes' and answer != 'no':
        print("Sorry, you must either type Yes or No below")
        answer = input().lower()
    return True if answer == 'yes' else False


def numbers(start, end):
    "Choose a number from 'start' to 'end'."
    answer = input().lower()
    x = [str(i) for i in range(start,end + 1)]
    while answer not in x:
        print("Sorry, you must pick a number from the list above.")
        answer = input().lower()
    return int(answer)
def enter():
    answer = input()
    while answer != '':
        print("You must press ENTER to continue.")
        answer = input()

def Next(function,text):
    enter()
    function(text)

def Replace(List, List2):
    "Replaces each element in List1 that is also in List2 with an empty string."
    List1 = [i for i in List]
    for i in range(len(List1)):
        for el in List2:
            if el in List1[i]:
                List1[i] = List1[i].replace(el, '')
    return List1

def Replace2(List, keyword):
    "Replaces all elements in keyword that are in List"
    k = [i for i in keyword if i not in List]
    return "".join(k)

def listreplace(List, word, replace):
    "Replaces each 'word' in 'List' with 'replace'"
    if len(List) == 0:
        return []
    return [List[0].replace(word, replace)] + listreplace(List[1:], word, replace)
        
def strreplace(String, args):
    "Replaces all 'args' in 'String'"
    for i in args:
        if i in String:
            String = String.replace(i, '')
    return String

def TrueorFalse(List, string):
    "If string in List, returns True."
    if len(List) == 0:
        return True
    return List[0] in string or TrueorFalse(List[1:])

def password(pwd, tries):
    triess = 1
    accessed = True
    pass_word = getpass.getpass()
    while pass_word != pwd:
        print("Incorrect password.")
        pass_word = getpass.getpass()
        triess = triess + 1
        if triess == tries and pass_word != pwd:
            print("Access Denied.")
            accessed = False
            break
    return accessed
            
