import random
#define welcome
def welcome():
    print("Welcome to Rock-Python-Scissors!")
#Ask user to enter their choice
    print("Enter your choice: 'rock', 'python', or'scissors'")
    print("I accept banana's but they can't be played in this game")
#define computer choice using random
def get_computer_choice(states):
    return random.choice(states)
#define user choice using input
def get_user_choice(states):
    user_choice = input().lower()
#using while loop to ensure user inputs a valid choice
    while user_choice not in states:
        print("Invalid input, please enter: 'rock', 'python', or 'scissors'")
        user_choice = input().lower()
    return user_choice
#define the winner
def get_winner(user_choice, computer_choice, states, results):
    if user_choice == computer_choice:
        results["draws"] += 1
        print("It's a draw!")
    elif(
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'python' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'python')
    ):
        results["user_wins"] += 1
        print(f"You win! {user_choice.capitalize()} beats {computer_choice}")
    else:
        results["computer_wins"] += 1
        print(f"You lose! {computer_choice} beats {user_choice}.")
#define outcome of 2 wins
def check_wins(results):
    if results["user_wins"] == 2:
        return "user"
    elif results["computer_wins"] == 2:
        return "computer"
    return None
#define the winner of three rounds
def display_winner(winner,results):
    print(f"{winner.capitalize} Wins the Game!")
    print(f"Final results: {results}")
#define display the final results
def display_final_results(results):
    print("final results:")
    print(f"User Wins! {results['user_wins']}")
    print(f"Computer Wins! {results['computer_wins']}")
    print(f"It's a draw {results['draws']}")
#define goodbye
def goodbye():
    print("Thank you for playing ROCK-PYTHON-SCISSORS\n I'll be back!")
#define main
def main():
    states = ["rock", "python", "scissors"]
    results = {"user_wins": 0,"computer_wins": 0,"draws": 0}

    welcome()

    for i in range(1,4):
        print(f"Round {i}:")
        computer_choice = get_computer_choice(states)
        user_choice = get_user_choice(states)
        get_winner(user_choice, computer_choice, states, results)
        winner = check_wins(results)
        if winner:
            display_winner(winner, results)
            display_final_results(results)
            goodbye()
            break

#If statement to run the main program if the name is main
if __name__=="__main__":
    main()
