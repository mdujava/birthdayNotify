from person import Person
import readline
import re


def go(db):
    global status
    while status == 1:
        inputText = input("command> ")
        resArray = {}
        for i in commands:
            res = re.search("^" + inputText + ".*", i)
            resArray[i] = res

        candidate = []
        for i in resArray:
            if resArray[i] != None:
                candidate.append(i)

        if len(candidate) == 1:
            commands[candidate[0]](db)
        elif len(candidate) > 1:
            print("do you mean:")
            for can in candidate:
                print("\t", can)
        else:
            print("use h/help for help.")

def helpMe(db):
    print("help:")
    for i in commandsHelp:
        print("\t", i, ":",  commandsHelp[i])

def add(db):
    print("add")

    firstName = input("\tfirstName: ")
    secondName = input("\tsecondName: ")
    birthdayDate = input("\tbirthdayDate: ")
    namedayDate = input("\tnamedayDate: ")
    mail = input("\tmail: ")
    telNumber = input("\ttelNumber: ")
    facebook = input("\tfacebook: ")
    group = input("\tgroup: ")

    newPerson = Person(firstName, secondName, birthdayDate,namedayDate, mail, telNumber, facebook, group)

    db.add(newPerson)

def showDb(db):
    for person in db.db:
        print(person)

def quit(db):
    global status
    status = 0

def showTable(db):
    print("\tfirstName\t|secondName\t|birthdayDate\t|namedayDate\t|mail\t\t|telNumber\t|facebook\t|group\t")
    for person in db.db:
        raw = "\t"+str(person.firstName)
        raw += "\t"+str(person.secondName)
        raw += "\t"+str(person.birthdayDate)
        raw += "\t"+str(person.namedayDate)
        raw += "\t"+str(person.mail)
        raw += "\t"+str(person.telNumber)
        raw += "\t"+str(person.facebook)
        raw += "\t"+str(person.group)

status = 1
commands = {"help": helpMe,
            "add": add,
            "quit": quit,
            "exit": quit,
            "list": showDb,
            "listTable": showTable}

commandsHelp = {"help": "help for command help",
                "add": "help for command add",
                "quit": "help for command quit",
                "list": "help for command list"}
