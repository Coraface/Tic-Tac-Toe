from typing import Any

result = input("Hello players. Ready to play?(Y/N)")
if result == 'Y':
	print("Ok, begin!")
else :
	print("Bye!")
	exit(1)
X = 'X'
O = 'O'

#print initial table
print("This is the initial table:\n  0  1  2\n0 _  _  _\n1 _  _  _\n2 _  _  _\n")

#create table
table = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
def printTable():
	print("  0   1   2")
	for i in range(len(table)):
		print(i)
		for j in range(len(table[i])):
			print(' ', table[i][j], end =' ')
		print()

def win():
	for i in range(len(table)):
		# rows
		if table[i][0] == table[i][1] and table[i][1] == table[i][2] and table[i][0] != "_":
			return True
	for j in range(len(table[i])):
		#columns
		if table[0][j] == table[1][j] and table[1][j] == table[2][j] and table[0][j] != "_":
			return True
	#1st diagonal
	if table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][0] != "_":
		return True
	#2nd diagonal
	elif table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2] != "_":
		return True
	else :
		return False

counter = 0
print("Player 1 gets O and Player 2 gets X\n")
while True:
	print("It's Player", counter%2+1,"'s turn")
	row = 3
	col = 3
	while True:
		while row > 2 or col > 2:
			row = int(input("Select the row you want(0-2):"))
			col = int(input("Select the column you want(0-2):"))
		if table[row][col] != "_":
			print("Someone has already selected this position, choose another\n")
			row = 3
			col = 3
		else:
			break

	if counter % 2 == 0:
		table[row][col] = O
	else:
		table[row][col] = X
	printTable()
	win()
	counter+=1
	if counter == 9 or win() == True :
		break

if win() == True and counter % 2 == 0:
	print("Player 2 won!!")
elif win() == True and counter % 2 != 0:
	print("Player 1 won!!")
else:
	print("It's a tie :)")
