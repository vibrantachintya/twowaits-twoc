
run_Player1 = int(input("Enter the runs scored by player 1 in 60 balls: "))
run_Player2 = int(input("Enter the runs scored by player 2 in 60 balls: "))
run_Player3 = int(input("Enter the runs scored by player 3 in 60 balls: "))
strikerate1 = run_Player1 * 100 / 60
strikerate2 = run_Player2 * 100 / 60
strikerate3 = run_Player3 * 100 / 60
print("Strike rate of player 1 is", strikerate1)
print("Strike rate of player 2 is", strikerate2)
print("Strike rate of player 3 is", strikerate3)
print("Runs scored by player 1 if they played 60 more balls is", run_Player1 * 2)
print("Runs scored by player 2 if they played 60 more balls is", run_Player2 * 2)
print("Runs scored by player 3 if they played 60 more balls is", run_Player3 * 2)
print("Maximum number of sixes player 1 could hit =", run_Player1 // 6)
print("Maximum number of sixes player 2 could hit =", run_Player2 // 6)
print("Maximum number of sixes player 3 could hit =", run_Player3 // 6)

#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH