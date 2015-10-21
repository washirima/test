__author__ = 'Ingrid Marie'

#this is a gess the mumber game.
import random

print('Hello. Whats is your name?')
name = input()

print ('well,' + name + ', I am thinking of a No bten 0 ,20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('take aguess')
    guess = int ( input())

    if guess < secretNumber:
        print('your guess is too low')
