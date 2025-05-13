import random
import turtle

import numpy

moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # su giu destra sinistra
movesb = [[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0]]
movesbn = [[0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]

randomDir = [0, 1,  2, 3]

def drawcell(cell, lenght, t):
    for wall in cell:
        if wall == 0:
            t.pendown()
        else:
            t.penup()
        t.right(90)
        t.forward(lenght)


def drawgrid(grid, lenght):
    win_width, win_height, bg_color = 2000, 2000, 'white'
    turtle.setup()
    turtle.screensize(win_width, win_height, bg_color)
    turtle.tracer(0, 0)
    t = turtle.Turtle()

    t.speed(0)
    i = 0
    for row in grid:
        t.penup()
        t.setposition(0, i)
        i2 = 0
        for cell in row:
            t.setheading(180)
            t.penup()
            t.setposition(i2, i)
            drawcell(cell, lenght, t)
            i2 += lenght
        i -= lenght
    t.hideturtle()
    turtle.update()
    turtle.done()


def creategrid(rows, colums):
    grid = []
    for y in range(rows):
        row = []
        for x in range(colums):
            row.append([0, 0, 0, 0])
        grid.append(row)
    return grid


def printgrid(grid):
    for row in grid:
        print(row)


def connectDir(x, y, dir, grid, chunk, chunky):
    h = len(grid)
    w = len(grid[0])

    ym = y + moves[dir][0]
    xm = x + moves[dir][1]
    print("xm : " + str(xm) + " ym : " + str(ym) + " chunk : " + str(3 + chunk * 3) + " chunky: " + str(3 + chunky * 3))
    if not (xm < 0 or ym < 0 or xm >= 3 + chunk * 3 or ym >= 3 + chunky * 3):
        temp = numpy.add(grid[ym][xm], movesbn[dir]).tolist()
        if 2 not in temp:
            grid[ym][xm] = numpy.add(grid[ym][xm], movesbn[dir]).tolist()
            grid[y][x] = numpy.add(grid[y][x], movesb[dir]).tolist()
            return grid
        else:
            print("already connected")
    else:
        print("cant connect")
    return False


def genlab(seed, grid):
    h = len(grid)
    w = len(grid[0])
    if seed != -1:
        random.seed(seed)

    x = 0
    y = 0
    i = 0
    chunkCount = 0
    chunkx = 0
    chunky = 0
    while chunkCount < int((h / 3) * (w / 3)):
        print("chunkx : " + str(chunkx) + " chunky : " + str(chunky))
        print("chunk  count : " + str(chunkCount))
        i = 0
        while i < 9:
            x = i % 3 + chunkx * 3
            y = int(i / 3 + chunky * 3)
            i += 2

            print(x, y)
            random.shuffle(randomDir)
            for dir in randomDir:
                res = connectDir(x, y, dir, grid, chunkx, chunky)
                if (res):
                    grid = res
                    break
        chunkCount += 1
        chunkx = int(chunkCount % (w / 3))
        chunky = int(chunkCount / (w / 3))




    x = 0
    y = 0
    i = 0
    chunkCount = 0
    chunkx = 0
    chunky = 0
    while chunkCount < int((h / 3) * (w / 3)):
        print("chunkx : " + str(chunkx) + " chunky : " + str(chunky))
        print("chunk  count : " + str(chunkCount))
        i = 1
        while i < 9:
            x = i % 3 + chunkx * 3
            y = int(i / 3 + chunky * 3)
            i += 2

            print(x, y)
            random.shuffle(randomDir)
            for dir in randomDir:
                res = connectDir(x, y, dir, grid, chunkx, chunky)
                if (res):
                    grid = res
                    break
        chunkCount += 1
        chunkx = int(chunkCount % (w / 3))
        chunky = int(chunkCount / (w / 3))


    print("done!")
    return grid


grid = genlab(-1, creategrid(6, 6))
printgrid(grid)
drawgrid(grid, 10)
