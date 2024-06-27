import copy
import os

def grid_creation(size) :

	grid = [["_ "]*size]*size

	return grid

def display_grid(grid) :

	i = 0

	print("\n")

	while i < len(grid) :

		print("\t" + "".join(grid[i]))
		i += 1

	print("\n")	

def fill_the_grid(grid, row, col, value) :

	line = copy.deepcopy(grid[row - 1])
	line[col - 1] = value + " "

	del grid[row -1]
	grid.insert(row - 1, line)

	return grid


sizeOfTheGrid = int(input("Enter the size of the grid : "))

newGrid = grid_creation(sizeOfTheGrid)
display_grid(newGrid)

while 1 :

	answer = input("\nDo you want to modify a cell? ")

	if answer == "no":
		break
	else :

		cellCoordinates = input("\nEnter the cell coordinates (the rows and column start from 1) : ")

		coordinates = cellCoordinates.split(",")
		row = int(coordinates[0])
		col = int(coordinates[1])

		newValue = input("\nEnter the new value for the cell : ")
		updatedGrid = fill_the_grid(newGrid, row, col, newValue)
		display_grid(updatedGrid)
		print("\n")

os.system("cls")
print("End")