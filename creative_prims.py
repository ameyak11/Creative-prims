
import pygame
import random
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 0

grid = []
for row in range(24):
	grid.append([])
	for column in range(34):
		grid[row].append(0) 

pygame.init()

WINDOW_SIZE = [680, 480]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("RANDOM MAZE")

done = False

clock = pygame.time.Clock()
frontier = []
frontier_flag = 0
i = random.randint(2,21)
j = random.randint(2,31)
grid[i][j]=1
print "grid["+str(i)+"]["+str(j)+"]"
if grid[i+2][j] == 0:
	for t in range(0,len(frontier)):
		if (i+2,j)==frontier[t]:
			frontier_flag =1 
	if frontier_flag == 0:
		if i+2<21:
			grid[i+2][j]=2
			frontier.append((i+2,j))
		frontier_flag=0
	print frontier
if grid[i-2][j] == 0:
	for t in range(0,len(frontier)):
		if (i-2,j)==frontier[t]:
			frontier_flag =1 
	if frontier_flag == 0:
		if i-2>=2:
			grid[i-2][j]=2
			frontier.append((i-2,j))
		frontier_flag=0
	print frontier		
if grid[i][j+2] == 0:
	for t in range(0,len(frontier)):
		if (i,j+2)==frontier[t]:
			frontier_flag =1 
	if frontier_flag == 0:
		if j+2<32:
			grid[i][j+2]=2
			frontier.append((i,j+2))
		frontier_flag=0
	print frontier		
if grid[i][j-2] == 0:
	for t in range(0,len(frontier)):
		if (i,j-2)==frontier[t]:
			frontier_flag =1 
	if frontier_flag == 0:
		if j-2>=2:
			grid[i][j-2]=2
			frontier.append((i,j-2))
		frontier_flag=0
	print frontier		
		
# Draw the grid
for row in range(24):
	for column in range(34):
		color = BLACK
		if grid[row][column] == 1:
			color = WHITE
		if grid[row][column] == 2:
			color = RED
		pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
# Limit to 60 frames per second
clock.tick(10)

pygame.display.flip()
# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			done = True 
		
	#---------actual maze generating while loop-----------

	while len(frontier)!=0:
		f = random.randint(0,len(frontier)-1)
		num = frontier[f]
		print "Selected frontier " + str(num)
		x = num[0]
		y = num[1]
		neighbours = []
		if grid[x-2][y] == 1:
			neighbours.append((x-2,y))
		if grid[x+2][y] == 1:
			neighbours.append((x+2,y))
		if grid[x][y-2] == 1:
			neighbours.append((x,y-2))
		if grid[x][y+2] == 1:
			neighbours.append((x,y+2))
		print neighbours
		n = random.randint(0,len(neighbours)-1)
		num1 = neighbours[n]
		print "Selected neighbour is " + str(num1)
		p = num1[0]
		q = num1[1]
		grid[x][y]=1
		if p==x:
			if q>y:
				grid[x][y+1]=1
			elif q<y:
				grid[x][y-1]=1
		elif q==y:
			if p>x:
				grid[x+1][y]=1
			elif p<x:
				grid[x-1][y]=1
		#-----------frontier of selected frontier----------------------

		if grid[x+2][y] == 0:
			for t in range(0,len(frontier)):
				if (x+2,y)==frontier[t]:
					frontier_flag =1 
			if frontier_flag == 0:
				if x+2<21:
					grid[x+2][y]=2
					frontier.append((x+2,y))
				frontier_flag=0
			print frontier
		if grid[x-2][y] == 0:
			for t in range(0,len(frontier)):
				if (x-2,y)==frontier[t]:
					frontier_flag =1 
			if frontier_flag == 0:
				if x-2>=2:
					grid[x-2][y]=2
					frontier.append((x-2,y))
				frontier_flag=0
			print frontier		
		if grid[x][y+2] == 0:
			for t in range(0,len(frontier)):
				if (x,y+2)==frontier[t]:
					frontier_flag =1 
			if frontier_flag == 0:
				if y+2<32:
					grid[x][y+2]=2
					frontier.append((x,y+2))
				frontier_flag=0
			print frontier		
		if grid[x][y-2] == 0:
			grid[x][y-2]=2
			for t in range(0,len(frontier)):
				if (x,y-2)==frontier[t]:
					frontier_flag =1 
			if frontier_flag == 0:
				if y-2>=2:
					frontier.append((x,y-2))
			frontier_flag=0
			print frontier
		for row in range(24):
			for column in range(34):
				color = BLACK
				if grid[row][column] == 1:
					color = WHITE
				pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
	
		clock.tick(10)
		pygame.display.flip()
		del frontier[f]
pygame.quit()
