names = os.listdir(directory + "contacts")
people = {}
for i in names:
    lines = [i.strip() for i in module.read(f"{directory}contacts/{i}", 'rl')]
    people[lines[0]] = {}
    characteristics = ["Name", "Phone", "Birthday", "Address"]
    for i, el in enumerate(characteristics):
        people[lines[0]][el] = lines[i]
        people[lines[0]]['Pictures'] = lines[len(characteristics):]
for i, el in enumerate(people, 1):
    print(f"{i}. {el}")
person = string.capwords(input("\nWhat person would you like to check?\n"))
y = [str(i) for i in range(len(people))]
while person not in y and person not in people:
    person = string.capwords(input("Sorry. You must choose an available contact."))
try: person = list(people)[int(person) - 1]
except: pass
for i in people[person]:
    if i != "Pictures":
        print(str(i)  + ":",people[person][i])
if len(people[person]["Pictures"]) != 0:
    pic = module.yesorno(f"\nWould you like to see a pic of {person}?")
    if pic:
        pic_dir = "/home/serena/Nextcloud/Photos/"
        for i in people[person]['Pictures']:
            subprocess.call(['xdg-open', pic_dir + i])

