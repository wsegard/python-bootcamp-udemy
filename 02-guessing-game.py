from random import randint

a = randint(1,101)
print(a)
guess_history = []
guess = input("What's your first guess: ")
guess_history.append(guess)
while a != guess:
  if guess < 1 or guess > 100:
    print("OUT OF BOUNDS")
  else:
    if len(guess_history) == 1:
      if abs(a - guess) < 11:
        print("WARM")
      else:
        print("COLD")
    else:
      print(guess)
      print(guess_history[-1])
      if abs(a - guess) < abs(a - guess_history[-1]):
        print("WARMER")
      else:
        print("COLDER")
  guess_history.append(guess)
  guess = input("What's your new guess: ")
print("you have guessed correctly. It took you {} guesses" .format(len(guess_history)))
