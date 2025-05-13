# FractalMazeGen
A strange maze generator algorithm i made


It's really fast and can be run in parallel but it has some major drawbacks.
the maze size needs to be a square of 3^n x 3^n, which limits a lot the size of your maze.
the other drawback, that I could fix, is that I made it so that loops are permitted, but the algorithm tends to create loops a bit too much, I could probably add a simple check to fix it, but I need to look into it.

the principle behind this algorithm is that if you take a 3x3 grid and randomly connect each point in a random direction starting from the edges the points will always be fully connected without leaving separated areas or points.
then you can simply add together the 3x3 chunks in a bigger 3x3 chunk made of those chunks and apply the algorithm on that bigger grid as well. you can simply repeat the process as many times as you want, it's almost like a "fractal" maze.

the algorithm is optimized and for each chunk, you simply need to check for existing connection on 4 of the 9 points, since the center point and the points at the corners will never touch, you can connect dose simultaneously and then connect the remaining 4 by first checking if the connection they are trying to make already exists.

PS: I don't know if this algorithm already exists since I didn't look up anything while making it so if someone knows of a similar one feel free to tell me.
PSS: English isn't my first language and this is a really long message, so sorry if there are some errors and if the explanation isn't really clear.

in the step-by-step example, the two groups of points are represented one in red and one in blue. 

![WhatsApp_Image_2023-10-21_at_14 11 59_dec6927f](https://github.com/user-attachments/assets/b67a6757-4037-431c-839a-d9a54ea3d865)

![image](https://github.com/user-attachments/assets/72086b88-dc67-406f-9879-52c6cf36d3a8)
