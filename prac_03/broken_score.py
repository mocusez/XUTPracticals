"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print("Your score is:{:.0f}, is {}".format(score,check(score)))
    randomscore = random.randint(0,100)
    print("Your score is:{:.0f}, is {}".format(randomscore,check(randomscore)))


def check(score):
    if 0 > score or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
