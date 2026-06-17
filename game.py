import random

def rock_paper_scissors():
    print("=== Let's Play Rock - Paper - Scissors ===")
    
    options = ['rock', 'paper', 'scissors']
    player_points = 0
    ai_points = 0

    while True:
        user_pick = input("\nChoose your move (rock/paper/scissors): ").strip().lower()

        if user_pick not in options:
            print("That’s not a valid move. Try again.")
            continue

        ai_pick = random.choice(options)
        print(f"The computer chose: {ai_pick}")

        if user_pick == ai_pick:
            print("It's a tie!")
        elif (user_pick == 'rock' and ai_pick == 'scissors') or \
             (user_pick == 'scissors' and ai_pick == 'paper') or \
             (user_pick == 'paper' and ai_pick == 'rock'):
            print("You win this round!")
            player_points += 1
        else:
            print("Computer wins this round!")
            ai_points += 1

        print(f"Current Score - You: {player_points} | Computer: {ai_points}")

        play_more = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_more != 'yes':
            print("\nGame Over. Thanks for playing!")
            break

rock_paper_scissors()
