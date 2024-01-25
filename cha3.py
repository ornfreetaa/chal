#!/usr/bin/env python2

import random

def find_winner():
    # choose a move
    choice = random.choice(["rock", "paper", "scissors"])

    # print the value of choice
    print("[*] Computer's choice:", choice)

    # find winner
    if choice == "rock": # rock beats paper
        winner = 2
    if choice == "paper": # scissors beats paper
        winner = 3
    if choice == "scissors": # rock beats scissors
        winner = 1

    # get user input
    print("1 for rock, 2 for paper, 3 for scissors")
    inp = int(input("> "))
    if inp == winner:
        print("[*] You win!")
        return True
    else:
        print("[*] You lose! (or tied, idrc)")
        return False

# main function
def main():
    print("Rock, paper, or scissors?")

    # run 10 games
    for _ in range(10):
        if find_winner():
             print("[*] Moving on to the next round...")
        else:
             print("[*] GAME OVER")
             exit()

    # this will execute if you win all 10 games
    print("[*] Printing flag...")
    print(open("/home/ctf/chal3/flag.txt").read())

# run the main function
if __name__ == "__main__":
    main()
