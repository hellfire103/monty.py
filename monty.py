#!/bin/python3

def dunno(name,variable):
  die = False

  if "no" in variable:
    die = True

  if die:
    print("(" + name + " was launched into the ravine from a great height and died. Just tell them walk it off, they'll be fine.)")
    die = False
    return "dead"

name1 = input("What is your name? ")

dunno(name1,name1)

quest1 = input("What is your quest? ")

dunno(name1,quest1)

colour1 = input("What is your favourite colour? ")

if dunno(name1,colour1) != "dead":
  print("Right. Off you go!")

name2 = input("What is your name? ")

dunno(name2,name2)

quest2 = input("What is your quest? ")

dunno(name2,quest2)

assyria = input("What is the capital of Assyria? ")

if dunno(name2,assyria) != "dead":
  dunno(name2,"no")

name3 = input("What is your name? ")

dunno(name3,name3)

quest3 = input("What is your quest? ")

dunno(name3,quest3)

colour2 = input("What is your favourite colour? ")

dunno(name3,colour2)

name4 = input("What is your name? ")

dunno(name4,name4)

quest4 = input("What is your quest? ")

dunno(name4,quest4)

swallow = input("What is the airspeed velocity of an unladen swallow? ")

dunno(name4,swallow)

if "african or european" in swallow.lower():
  print("I don't know that! Agh!\n\n(The bridgekeeper was launched into the ravine from a great height and died.)\n\nYou win!")
else:
  dunno(name4,"no")
