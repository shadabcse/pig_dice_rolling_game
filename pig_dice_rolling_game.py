import random

def roll():
    return random.randint(1, 6)

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0] * players  

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn! Total Score: {player_scores[player_idx]}")
        current_score = 0

        while True:
            action = input("Roll (r) or Hold (h)? ").lower()
            
            if action == "h":
                print(f"You held your score. Adding {current_score} to your total.")
                break  
            
            elif action == "r":
                value = roll()
                print(f"You rolled: {value}")
                
                if value == 1:
                    print("Oops! Rolled a 1. Turn over, no points added.")
                    current_score = 0
                    break 
                else:
                    current_score += value
                    print(f"Current turn score: {current_score}")
            else:
                print("Invalid input! Type 'r' to roll or 'h' to hold.")

        player_scores[player_idx] += current_score
        print(f"Total Score after turn: {player_scores[player_idx]}")

winner = player_scores.index(max(player_scores)) + 1
print(f"\n🎉 Player {winner} wins with {max(player_scores)} points!")
