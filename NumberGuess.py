'''I have no idea what this
program actually does yet'''

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  maxval = number_of_sides * 2
  print "The maximum value is %d" % maxval
  guess = get_user_guess()
  if guess > maxval:
    print "Number too high"
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d " % first_roll
    sleep(1)
    print "The second roll is %d " % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result... %d " % total_roll
    sleep(1)
    if guess > total_roll:
      print "You win!"
    else:
      print "Aww, too low."

roll_dice(6)
