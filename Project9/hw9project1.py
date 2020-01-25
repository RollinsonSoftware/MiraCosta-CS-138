#! /usr/bin/python
# Exercise No.   01
# File Name:     hw9project1.py
# Programmer:    John Rollinson
# Date:          10/27/2019
#
# Problem Statement:
# Write a program to simulate multiple games of craps and estimate the
# probability that the player wins. For example, if the player wins 249 out of
# 500 games, then the estimated probability of winning is 249/500 = 0.498
#
# Overall Plan:
# 1. Create a function printIntro() to introduce the users to the game.
# 2. Create a function printRules() to list down the game rules.
# 3. Create a function getInput() to ask the user for the number of games to be simulated. 
# 4. Create a function simNGames() which simulates multiple games of Craps.
# 5. Create a function simOneGame() which implements all the rules of the game and returns
#       whether the player has won the game. This function requires generating random
#       integers in the range 1 to 6, both inclusive, to simulate the roll of two dice.
#       Create a function rollTwoDices() for this.
# 6. Create a function checkIfWon() to be used by simOneGame(). This function implements all
#       all the rules of the game and returns if the game has been won or lost.
# 7. Create a function printSummary() which prints the final statistics of the simulation.
#
# import the necessary python libraries
from random import randrange

def printIntro():
    print("This program simulates n games of")
    print("Craps' which is a dice based game.")

def printRules():
    print("\nThe rules of the game are:")
    print("1. Roll a pair of normal six-faced dice.")
    print("2. If the initial roll is 2, 3, or 12 - the player loses.")
    print("3. If the roll is 7 or 11 - the player wins.")
    print("4. Any other roll leads to roll for point.")
    print("5. The player continues to roll until they get a 7 or re-rolls the previous value.")
    print("6. the player loses by rolling a 7 while re-rolling the same value allows the player to win.\n")

def getInputs():
    n = eval(input("How many games to simulate?: "))

    return n

def simNGames(n):
    wins = 0
    for i in range(n):
        won = simOneGame()

        if won is True:
            wins = wins + 1

    return wins

def simOneGame():
    sumDice = rollTwoDices()

    return checkIfWon(sumDice)

def rollTwoDices():
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    sumDice = dice1 + dice2

    return sumDice

def checkIfWon(sumDice):
    if sumDice == 2 or sumDice == 3 or sumDice == 12:
        return False
    elif sumDice == 7 or sumDice == 11:
        return True
    else:
        while True:
            sumDice = rollTwoDices()
            if sumDice == sumDice:
                return True
            elif sumDice == 7:
                return False

def printSummary(wins, nSim):
    print("\nGames simulated: {0}".format(nSim))
    nSim = float(nSim)
    print("Wins for the player: {0}({1:0.1%})".format(wins, (wins / nSim)))
    
def main():
    printIntro()
    printRules()

    n = getInputs()
    wins = simNGames(n)
    printSummary(wins, n)

main()
