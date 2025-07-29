from re import split
from pyfiglet import Figlet
import time
import sys
import os


print()
print("You find yourself walking through a thick forest, its hard to tell whether or not it's day or night but you can see little specks of what seem\nlike sunlight floating through the forest. You have no recollection of comming to this place or when you started walking but you continue to walk.\nHas that trail always been there or did it just now appear? You dont seem to mind you just continue to walk. ")
print()
input("a. Keep walking. \n \n")
print("How long have you been walking? You're unsure but you've noticed that like the flowers the trees are the same way. The trunks warping into odd shapes in the corner of your\neye. Some of the branches dont even seem connected to the trees themselves they're simply floting in the air above you.")
print()
input("a. Keep walking.\n\n")
print()
print("You feel like you've been walking for an eternity and yet there isnt an ounce of exaustion in you, so, you keep walking. The flowers and trees continue to warp in the\nside of your vision. Suddenly without any warning you come across a fork in the road. You swear that wasnt infront of you a moment ago.")
print()

choice1 = input("a. Look at RIGHT path.\nb. Look at LEFT path.\n\n")
if choice1 == "a":
  print()
  print("To the right the path continues through the forest with no end in sight, it simply disolves into a blank grey void of nothingness.")
  print()
elif choice1 == "b":
  print()
  print("To the left there is a tunnel seemingly made of sticks and vines, all weaved together to create an oddly cylindrical pathway. Like the forest there are flowers growing\non the walls of the tunnel, all completely still when your gaze rests on them but begining to change shape the second you turn away.")
print()
print("You feel like you've been walking for an eternity and yet there isnt an ounce of exaustion in you, so, you keep walking. The flowers and trees continue to warp in the\nside of your vision. Suddenly without any warning you come across a fork in the road. You swear that wasnt infront of you a moment ago.")
print()

choice1 = input("a. Look at RIGHT path.\nb. Look at LEFT path.\n\n")
if choice1 == "a":
  print()
  print("To the right the path continues through the forest with no end in sight, it simply disolves into a blank grey void of nothingness.")
  print()
elif choice1 == "b":
  print()
  print("To the left there is a tunnel seemingly made of sticks and vines, all weaved together to create an oddly cylindrical pathway. Like the forest there are flowers growing\non the walls of the tunnel, all completely still when your gaze rests on them but begining to change shape the second you turn away.")
print()
print("You decide to continue your treck. You decide to go...\n")
print()

choice2 = input("a. RIGHT\nb. LEFT\n\n")
if choice2 == "b":
  print()
  print("You walk towards the tunnel. Strangely enough there is more sunlight in the tunnel than there is in the forest, allowing you to safely enter the cyliender of vines\nwithout any fear of tripping. The way the sunlight (or is it moonlight) shines into the tunnel makes you feel like you are living in a perminant golden hour.\nIts beautiful, and you find yourself standing at the edge of the tunnel only steps away form entering. Do you...")
  print()
  choice2b = input("a. ENTER\nb. TURN BACK\n\n")
  print()
  if choice2b == "a":
    print()
    print("You ENTER the tunnel, and begin walking through it. The place glowes with the light of whatever celestial body is above you.")
    print()
    time.sleep(2)
    def delayed_horizontal_text(text, delay_per_char=0.5):
      for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_per_char)
    message = "...\n"
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    def delayed_horizontal_text(text, delay_per_char=0.15):
      for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_per_char)
    message = "Theres no going back now..."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "But you already knew that."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "Despite how you try and deny it..."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "You cant change the past."
    delayed_horizontal_text(message)
    print()
    time.sleep(3)
    print()
    print("As you walk through the tunnel you begin to think, why are you here? Where are you going? Are you really even going anywhere?\nIs all of this for a reason?")
    print()
    time.sleep(2)
    def delayed_horizontal_text(text, delay_per_char=0.5):
      for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_per_char)
    message = "...\n"
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    print("Of course theres a reason for this! It would be silly to think otherwise!")
    print()
    time.sleep(2)
    print()
    print("The tunnel continues to twist and turn as you walk through. As The light remains unmoving in the sky you get the feeling that the forest is now a thing of the past.\nNo longer are you bound by the neverending trees and shifting flowers, you now exist in a new world. One hanging on the edge of a precipice, that you could fall off of\nat any moment.")
    print()
    input("a. Keep walking\n\n")
    print()
    print("Finaly after no time at all has passed you see what you believe to be the end of the tunnel. It looks like the end simply leeds to a white void but as you get closer\nyou realize that you're walking into a building with pure white walls. When you reach the end of the tunnel you hesitate. Do you...")
    print()
    choice2b1 = input("a. Step out.\nb. GO BACK\n\n")
    print()
    if choice2b1 == "a":
      print()
      print()
      print("You step out of the tunnel, entering into the new space. You find yourself standing in a small mall, the walls and ceiling are all a bright white and made out a material\nyou cant quite place. Carved into the walls and ceiling are beautiful swirling vines that beautifly climb up the walls and across the ceiling. Like the forest\nthe building doesnt seem quite right. There's something uncanny about the place. Its almost to perfect and yet there are mistakes if you look closely.\nThe walls seem to merge into the ceiling in some place almost like their clipping through the soild material. Everything about the place is wrong and yet you dont\nGO BACK.")
      print()
      input("a. STEP FORWARD\n\n")
      print()
      print("You STEP FORWARD deeper in to the building. Behind you you hear the shifting of leaves and vines, looking back you realize the tunnel has closed behind you\nleaving a carved white wall in its place. You continue to walk forward into the building, eventually you step out into what seems like the main plaza, of what yo now\nrecognize as some kind of mall. Around you are five differnt shops:")
      print("Marie's Boutique")
      print("Jan's Jewlers")
      print("")
    elif choice2b1 == "b":
      def nochoicesroute(visitedOnce):


      
        if visitedOnce==True:
          print()
          print("You step out of the tunnel, entering into the new space. You find yourself standing in a small mall, the walls and ceiling are all a bright white and made out a material\nyou cant quite place. Carved into the walls and ceiling are beautiful swirling vines that beautifly climb up the walls and across the ceiling. Like the forest\nthe building doesnt seem quite right. There's something uncanny about the place. Its almost to perfect and yet there are mistakes if you look closely.\nThe walls seem to merge into the ceiling in some place almost like their clipping through the soild material. Everything about the place is wrong and yet you dont\nGO BACK.")
          print()
          input("a. STEP FORWARD\n\n")
          print()
          print("You STEP FORWARD deeper in to the building. Behind you you hear the shifting of leaves and vines, looking back you realize the tunnel has closed behind you\nleaving a carved white wall in its place. You continue to walk forward into the building, eventually you step out into what seems like the main plaza, of what yo now\nrecognize as some kind of mall. Around you are five differnt shops:")
          print()
          print("Marie's Boutique")
          print()
          print("Jan's Jewlers")
          print("")
          return
        elif choice2b1 == "b":
          def delayed_horizontal_text(text, delay_per_char=0.5):
            for char in text:
              sys.stdout.write(char)
              sys.stdout.flush()
              time.sleep(delay_per_char)
          print()
          message = "...\n"
          delayed_horizontal_text(message)
          print()
          def delayed_horizontal_text(text, delay_per_char=0.15):
            for char in text:
              sys.stdout.write(char)
              sys.stdout.flush()
              time.sleep(delay_per_char)
          time.sleep(2)
          print()
          message = "No.\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(2)
          print()
          message = "Why would I let you do that?\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          message = "I already told you...\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          message = "You made your choice...\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          message = "Theres no going back now.\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print("Finaly after no time at all has passed you see what you believe to be the end of the tunnel. It looks like the end simply leeds to a white void but as you get closer\nyou realize that you're walking into a building with pure white walls. When you reach the end of the tunnel you hesitate. Do you...")
          print()
        choice2b1a = input("a. Step out.\nb. GO BACK\n\n")
        if choice2b1a == "b":
          print()
          message = "You know what?\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          message = "You dont get to make the choices any more.\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          print("Behind you you hear the creaking of vines as the tunnel closes blocking you from your only way back to the fores. You're stuck here now.")
          print()
          time.sleep(1)
          print()
          message = "Now...\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          message = "What are you going to choose?\n"
          delayed_horizontal_text(message)
          print()
          time.sleep(1)
          print()
          choice2b1b = input("a. Step out\nb. Ĝ̴̟͓͚̯̖̪̟͖͖̰̗͍̪̬͎̉̉̊̀̐̓̀Ǫ̸̛̲̩̜̣͙͙̝̤̳̜̩̖͎͎̘̟͉̝̜͉̲̥̽̓̎́̽̾̈́͑̌̊́̋͛͐́͒̍̅̏̓̒̋͐̋̒̌̈̌́̐̈́̚ ̴̧̲̪͇̣̲̈́͝͠ͅB̴̡̥̫͈̝̤̥͖̙̜̙̲͓̳̙̼́̎͋͊̎̆͐̏̌̆́̅͜͜ͅA̶̡̡͓̝̤͇͕̘͕̭̞̘̭̤̝̱̺͚̜͚̬̠͍̬̮̣̠͂̐̏͆̿̐͊ͅC̸̡̨̮̩͇̯͈͍̺̤̼͕̫̖͓͍̜͙͔̈́K̷̪͑͆̉͊̊͂̈́͂́̏͝ \n\n")
          print()
          if choice2b1b == "a":
            print()

          elif choice2b1b == "b":
            time.sleep(2)
            print()
            print()
            message = "*sigh*\n"
            delayed_horizontal_text(message)
            print()
            time.sleep(2)
            print()
            message = "Fine.\n"
            delayed_horizontal_text(message)
            print()
            time.sleep(2)
            print()
            message = "We're just going to do this the easier way then.\n"
            delayed_horizontal_text(message)
            print()
            time.sleep(3)
            for y in range(0,3):
                for x in range(0,5):
                      b = "Reseting" + "." * x
                      print(b, end="\r")
                      time.sleep(.5)
                print()
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
          nochoicesroute(True) 
      nochoicesroute(False)


            




            

if choice2 == "a":
  print()
  choice2a = input("a. Keep walking.\nb. Stop\nc. GO BACK\n\n")
  print()
  if choice2a == "a":
    print()
    print("You keep walking. It feels like the forest might never end. Deep down you know you need to get to the grey void. That once you get there this will all be over.\nBut what is this? Is it really anything? Is it even real?")
    print()
    import random
    from random import choice
    marks = list(map(chr, range(768, 879)))
    time.sleep(6)
    string = 'IS IT REAL?'
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    print(string)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    time.sleep(1)
    words = string.split()
    print(' '.join(''.join(c + ''.join(choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words)))
    print()
    def delayed_horizontal_text(text, delay_per_char=0.2):
      for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_per_char)
    message = "Of course its real!"
    delayed_horizontal_text(message)
    print()
    time.sleep(3)
    print()
    time.sleep(2)
    message = "You know that."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "You cant GO BACK on your choice."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "Here how about this."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "You cant GO BACK."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "But you can GO FORWARD"
    delayed_horizontal_text(message)
    print()
    time.sleep(3)
    for y in range(0,3):
      for x in range(0,5):
        b = "Generating" + "." * x
        print(b, end="\r")
        time.sleep(.5)
        print()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    def delayed_horizontal_text(text, delay_per_char=0.2):
      for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_per_char)
    time.sleep(2)
    print()
    print("Suddenly about ten steps infront of you a doorway generates out of thin air.")
    print()
    time.sleep(3)
    print()
    message = "There!"
    print()
    delayed_horizontal_text(message)
    time.sleep(1)
    print()
    message = "Just go through that door! I think you'll like it there."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "Even if you dont..."
    delayed_horizontal_text(message)
    print()
    time.sleep
    print()
    message = "You chose this..."
    delayed_horizontal_text(message)
    print()
    time.sleep(2)
    print()
    message = "You cant GO BACK now..."
    delayed_horizontal_text(message)
    print()
    time.sleep(3)
    print()
    f = Figlet(font='block')
    print(f.renderText("End of Demo..."))

  elif choice2a == "b":
    print()
    print("You stop, standing in the middle of the trail. The forest around you is SILENT. No birds chirping or leaves rustling in the wind, just SILENCE. It feels wrong.\nA forest shouldn't be silent. There should be something, anything! There shouldn't just be a grey void, there should be an end to the path! The forest can't go on forever!")
    print()
    time.sleep(2)
    print()
    print("Right?")
    print()
    time.sleep(2)
    print()
    print("I want to wake up...")
    print()
    time.sleep(2)
    print()
    print("Please...")
    print()
    time.sleep(2)
    print()
    print("I- I made a mistake...") 
    print()
    time.sleep(2)
    print()
    print("I want to GO BACK.")
    print()
    time.sleep(2)
    print()
    f = Figlet(font='block')
    print(f.renderText("End of Demo..."))

