import random
import turtle
import numpy





def randomConnect(grid, x, y):
    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # su giu destra sinistra
    random.shuffle(dirs)
    #print(dirs)
    for d in dirs:
        #print(d)
        yt = y + d[0]
        xt = x + d[1]
        #print("xt : " + str(xt) + " yt : " + str(yt))
        if 0 <= yt < 5 and 0 <= xt < 5:
            grid[yt][xt] = 1
            break
        #else:
            #print("out of bounds")
    return grid

def randomConnectCheck(grid, x, y):
    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # su giu destra sinistra
    random.shuffle(dirs)
    for d in dirs:
        print("new loop")
        yt = y + d[0]
        xt = x + d[1]

        if (yt + d[0] == 2 and xt + d[1] == 2):
            if d[0] == 0:
                checkSum = 0
                #grid[yt + 1][xt] = 5
                #grid[yt - 1][xt] = 6

                for d2 in dirs:
                    checkSum += grid[yt + 1 + d2[0]][xt + d2[1]]
                    print(" 5: " + str(checkSum))
                    #grid[yt + 1 + d2[0]][xt + d2[1]] = 5
                if checkSum >= 3:
                    print(checkSum)
                    continue

                checkSum = 0
                for d2 in dirs:
                    checkSum += grid[yt - 1 + d2[0]][xt + d2[1]]
                    print(" 6: " + str(checkSum))
                    #grid[yt - 1 + d2[0]][xt + d2[1]] = 8
                if checkSum >= 3:
                    print(checkSum)
                    continue


            elif d[1] == 0:
                #grid[yt][xt + 1] = 7
                #grid[yt][xt - 1] = 8

                checkSum = 0
                for d2 in dirs:
                    checkSum += grid[yt + d2[0]][xt + 1 + d2[1]]
                    print( " 7: " + str(checkSum))
                    #grid[yt + d2[0]][xt + 1 + d2[1]] = 7

                if checkSum >= 3:
                    print(checkSum)
                    continue

                checkSum = 0
                for d2 in dirs:
                    checkSum += grid[yt + d2[0]][xt - 1 + d2[1]]
                    print(" 8: " + str(checkSum))
                    #grid[yt + d2[0]][xt - 1 + d2[1]] = 8
                if checkSum >= 3:
                    print(checkSum)
                    continue
        print("second check")
        if 0 <= yt < 5 and 0 <= xt < 5:

            if grid[yt][xt] == 0:
                grid[yt][xt] = 1
                break
            #else:
                #print("already connected")
    return grid




def drawgrid(grid):
    win_width, win_height, bg_color = 30000, 30000, 'white'
    turtle.setup()
    turtle.screensize(win_width, win_height, bg_color)
    turtle.tracer(0, 0)

    pen = turtle.Turtle()
    pen.speed(0)  # Set the drawing speed (0 is the fastest)

    cell_size = 5

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                pen.color("black")
                pen.fillcolor("black")
            else:
                pen.color("white")
                pen.fillcolor("white")

            pen.penup()
            pen.goto(x * cell_size, -y * cell_size)  # Negative y for correct orientation
            pen.pendown()
            pen.begin_fill()

            for _ in range(4):
                pen.forward(cell_size)
                pen.right(90)

            pen.end_fill()


    pen.hideturtle()
    turtle.update()
    turtle.done()

def creategrid(rows, colums):
    rows = rows + rows - 1
    colums = colums + colums - 1
    grid = []
    for y in range(rows):
        row = []
        for x in range(colums):
            row.append(0)
        grid.append(row)
    return grid


def printgrid(grid):
    for row in grid:
        print(' '.join(str(x) for x in row).replace("0", "□").replace("1","■"))



def genChunk():
    grid = creategrid(3, 3)
    i = 0
    y = 0
    x = 0
    firstBatch = []
    secondBatch = []
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            #print("x : " + str(i) + " y : " + str(j))
            if((j/2) % 2 == i/2 % 2):
                grid[i][j] = 1
                firstBatch.append([i, j])
            else:
                grid[i][j] = 1
                secondBatch.append([i, j])
            j += 2

        i += 2

    for cord in firstBatch:
        randomConnect(grid, cord[0], cord[1])
    for cord in secondBatch:
        randomConnectCheck(grid, cord[0], cord[1])

    return grid

def genlab(level):
    grid = []

    map = genChunk()
    #printgrid(map)

    if level == 0:
        return genChunk()

    for j in range(3):
        lineC = None
        for i in range(3):
            chunk = genlab(level-1)

            if j + 1 < 3:
                glue = [0] * len(chunk)
                if map[j * 2 + 1][i * 2] == 1:
                    connectPoint = random.randint(1, 2)
                    for ra in range(connectPoint):
                        glue[random.randint(0, 2) * 2] = 1
                chunk.append(glue)
            if i + 1 < 3:
                if map[j * 2][i * 2 +1] == 1:
                    connectPoint = []
                    for r in range(random.randint(1, 2)):
                        connectPoint.append(random.randint(0, 2) * 2)
                    for l in range(len(chunk)):
                        if l in connectPoint:
                            chunk[l].append(1)
                        else:
                            chunk[l].append(0)
                else:
                    for line in chunk:
                        line.append(0)

            if lineC is None:
                lineC = chunk
            else:
                for l in range(len(lineC)):
                    lineC[l].extend(chunk[l])
        grid.extend(lineC)




    return grid

grid = genlab(2)
printgrid(grid)
wall = [0] * len(grid)
wall[random.randint(0, int(len(wall) / 2)) * 2] = 1
grid.insert(0, wall)

wall = [0] * (len(grid) + 1)
wall[random.randint(0, int(len(wall) / 2)) * 2 + 1] = 1
grid.append(wall)

for i in range(len(grid[0]) + 1):
    grid[i].insert(0,0)
    grid[i].append(0)

printgrid(grid)
drawgrid(grid)
