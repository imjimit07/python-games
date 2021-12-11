print("Welcome to Games!")
print("Please choose a game you want to play.")

print("1) Sudoku")
print("2) 2048")
print("3) Hangman")

ans = input(print("Please type the number of the game you want to play: "))

if ans == '1' :
    exec(open('Sudoku.py').read())
elif ans == '2' :
    exec(open('2048.py').read())
elif ans == '3':
    exec(open('hangman.py').read())
else:
    print('Invalid command!')