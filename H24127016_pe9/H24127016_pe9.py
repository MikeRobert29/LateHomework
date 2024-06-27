import random
from sys import exit

class OptionError(Exception) :

    def __init__(self, message) :
        self.message = message

class TooMuchObstaclesError(Exception) :

    def __init__(self, message) :
        self.message = message

def generatePath(maze):
    path = []
    freeSpaceAfterPath = 0
    position = [0, 0]

    row = 0
    while row < len(maze):
        i = 0
        cantReachTheseColumns = []

        while i < len(maze[0]):
            if row == len(maze) - 1:
                break

            if maze[row + 1][i] == " X ":
                cantReachTheseColumns.append(i)

            i += 1

        if " X " in maze[row][position[1]:]:
            stop_index = maze[row][position[1]:].index(" X ") + position[1]
            stops = [j for j in range(position[1], stop_index) if j not in cantReachTheseColumns]
        else:
            stops = [j for j in range(position[1], len(maze[0])) if j not in cantReachTheseColumns]

        if len(stops) == 0:
            path.append([row, position[1]])
            row += 1
            continue

        if row == len(maze) - 1:
            stop = len(maze[0]) - 1
        else:
            stop = random.choice(stops)

        for col in range(position[1], stop + 1):
            path.append([row, col])

        position[1] = stop
        row += 1

    for coordinate in path:
        maze[coordinate[0]][coordinate[1]] = " O "

    for line in maze:
        void = line.count("   ")
        freeSpaceAfterPath += void

    return freeSpaceAfterPath
    

def generateObstacles(maze, totalObstacles) :

    emptyCells, cellsToFill = [], []

    i , j, k = 0, 0, 0

    while i < len(maze) :
        while j < len(maze[i]) :

            if maze[i][j] == "   " :
                emptyCells.append([i, j])

            j += 1

        j  = 0
        i += 1

    while k < totalObstacles :

        randomCoordinate = random.choice(emptyCells)
        cellsToFill.append(randomCoordinate)
        del emptyCells[emptyCells.index(randomCoordinate)]

        k += 1

    for coordinate in cellsToFill :
        maze[coordinate[0]][coordinate[1]] = " X "


def setObstacle(maze) :
    
    coordinate = input("\n\t\tEnter the coordinates of the obstacle you want to place (ex : 6 7) : ")
    coordinate = coordinate.split(" ")
    row, column = int(coordinate[0]), int(coordinate[1])

    if maze[row][column] == " X " :
        print("\t\tThis position already has an obstacle.")
    elif maze[row][column] == " O " :
        print("\t\tThis postion is on the path.")
    else :
        maze[row][column] = " X "

def removeObstacle(maze) :
    
    coordinate = input("\n\t\tEnter the coordinates of the obstacle you want to remove (ex : 3 0) : ")
    coordinate = coordinate.split(" ")
    row, column = int(coordinate[0]), int(coordinate[1])

    if maze[row][column] == "   " or maze[row][column] == " O " :
        print("\t\tThere are no obstacle in that position.")
    else :
        maze[row][column] = "   "

def run(maze) :

    limit = generatePath(maze)
    displayMaze(maze)

    while 1 :

        try :
            minimumNumberOfObstacle = int(input("\n\t\tEnter the minimum number of obstacle (0 - {}) : ".format(limit)))

            if minimumNumberOfObstacle > limit :
                raise TooMuchObstaclesError("\t\tThis is too much obstacles for the maze.")
            else :
                generateObstacles(maze, minimumNumberOfObstacle)
                break

        except ValueError :
            print("\t\tThis is not a number.")
            continue

        except TooMuchObstaclesError as e :
            print(e.message)
            continue

    displayMaze(maze)

    while 1 :

        print("\n\t\tOptions")
        print("\t\t1-Set obstacle")
        print("\t\t2-Remove obstacle")
        print("\t\t3-Exit")

        try :
            choice = int(input("\n\t\tEnter your option : "))

            if choice not in [1, 2, 3] :
                raise OptionError("\t\tThis number is not one of the options number.\n\t\tPlease enter a valid number.")

        except ValueError :
            print("\t\tYou should choose an option by his number.\n\t\tPlease choose a valid option : ")
            continue
        except OptionError as e :
            print(e.message)
            continue

        if choice == 1 :
            setObstacle(maze)

        elif choice == 2 :
            removeObstacle(maze)

        else :
            break

        displayMaze(maze)


def displayMaze(maze) :

    i = 0

    print("\n\n")

    while i < len(maze) :

        print("\t\t" + "+---" * len(maze[0]) + "+")
        print("\t\t" + "|" + "|".join(maze[i]) + "|")
        i += 1

    print("\t\t" + "+---" * len(maze[0]) + "+")

    print("\n\n")

 
def main():
    
    maze      = []
    file_path = input("\n\t\tWhat file do you want to open ? ")

    try :

        file = open(file_path, 'r')

        content = file.readlines()

        file.close()

        print("\n")
        for line in content :

            if "\n" in line :
                line = line.replace("\n", "")

            print("\t\t" + line)
        print("\n")

        i = 1
        while i <= len(content) - 1 :

            content[i] = content[i].split("|")
            del content[i][0]
            del content[i][len(content[i]) - 1]

            maze.append(content[i])

            i += 2

        run(maze)

    except :

        print("\n\t\t\tFile not found\n\n\t\t\t     END\n")
        exit()

main()

print("\n\n\t\t\tEND\n")