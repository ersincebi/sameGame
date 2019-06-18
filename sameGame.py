import random
import sys

def main():
	createGamePlane(letters[:letNum],letNum)
	print("The letters to be used in game are: ",end=" ")
	print(letters[:letNum])
	game()
	lastScore()

def lastScore():
	count = currLen()
	print("Your final score : ", end=" ")
	if count == 0:
		print(str(currScore() * 5))
	else:
		print(str(currScore()-count))

def currLen():
	count = 0
	for i in range(10):
		for j in range(20):
			if letterList[i][j]!=" ":
				count += 1
	return count

def createGamePlane(letTers,letNum):
	for i in range(10):
		let = []
		for j in range(20):
			rand = random.randint(0,letNum)
			let.append(letters[rand])
		letterList.append(let)

def listLetters(letterList):
	print(end= "  ")
	for k in range(20):
		if k<10:
			print(str(k),end="  ")
		else:
			print(str(k),end=" ")
	print()
	for i in range(10):
		print(str(i),end=" ")
		for j in range(20):
			print(letterList[i][j], end="  ")
		print()
	print(end= "  ")
	for k in range(20):
		if k<10:
			print(str(k),end="  ")
		else:
			print(str(k),end=" ")
	print()

def currScore():
	n = 200 - currLen()
	if n==0:
		return 0
	return (n-2) ** 2

def showHint():
	return 0

def searchHorizontalUpwardLeft(posX,posY,letter,moveCountOnH=0):
	if posY == 0 or posX == 0:
		return 0
	if letterList[posX][posY]==letter:
		letterList[posX][posY] = " "
		return searchHorizontalUpwardLeft(posX,posY-1,letter,moveCountOnH+1)
	if letterList[posX-1][posY-moveCountOnH]==letter:
		return searchHorizontalUpwardLeft(posX-1,posY+moveCountOnH,letter)

def searchHorizontalUpwardRight(posX,posY,letter,moveCountOnH=0):
	if posY == 19 or posX == 0:
		return 0
	if letterList[posX][posY]==letter:
		letterList[posX][posY] = " "
		return searchHorizontalUpwardRight(posX,posY+1,letter,moveCountOnH+1)
	if letterList[posX-1][posY-moveCountOnH]==letter:
		return searchHorizontalUpwardRight(posX-1,posY-moveCountOnH,letter)

def searchHorizontalDownwardLeft(posX,posY,letter,moveCountOnH=0):
	if posY == 0 or posX == 9:
		return 0
	if letterList[posX][posY]==letter:
		letterList[posX][posY] = " "
		return searchHorizontalDownwardLeft(posX,posY-1,letter,moveCountOnH+1)
	if letterList[posX+1][posY-moveCountOnH]==letter:
		return searchHorizontalDownwardLeft(posX+1,posY+moveCountOnH,letter)

def searchHorizontalDownwardRight(posX,posY,letter,moveCountOnH=0):
	if posY == 19 or posX == 9:
		return 0
	if letterList[posX][posY]==letter:
		letterList[posX][posY] = " "
		return searchHorizontalDownwardRight(posX,posY+1,letter,moveCountOnH+1)
	if letterList[posX+1][posY-moveCountOnH]==letter:
		return searchHorizontalDownwardRight(posX+1,posY-moveCountOnH,letter)

def searchVerticalUpward(posX,posY,letter):
	if posX == 0:
		return 0
	if letterList[posX][posY]==letter:
		letterList[posX][posY] = " "
	return searchVerticalUpward(posX-1,posY,letter)

def searchVerticalDownward(posX,posY,letter):
	if posX == 9:
		return 0
	if letterList[posX][posY]==letter:
		letterList[posX][posY] = " "
	return searchVerticalDownward(posX+1,posY,letter)

def checkPlane():
	global emptyCol
	for k in range(10):
		for j in range(20):
			for i in reversed(range(1,10)):
				if letterList[i][j] == " ":
					letterList[i][j] = letterList[i-1][j]
					letterList[i-1][j] = " "
	count = 0
	for j in range(20):
		for i in range(10):
			if letterList[i][j]==" ":
				count += 1
		if count==10:
			emptyCol += 1
			shiftListLeft(j)
		count=0
	for j in range(20-emptyCol,20):
		for i in range(10):
			letterList[i][j] = " "

def shiftListLeft(posY):
	if posY==19:
		return 0
	for i in range(10):
		letterList[i][posY] = letterList[i][posY+1]
	return shiftListLeft(posY+1)

def exit():
	lastScore()
	print("Bye")
	sys.exit()

def game():
	listLetters(letterList)
	print("Current Score : " + str(currScore()))
	print("Enter -1 to quit")
	print("Enter -2 to get hint")
	posX = int(input("Enter the possition for X: "))
	posY = int(input("Enter the possition for Y: "))
	if posX == -1 or posY == -1:
		exit()
	elif posX == -2 or posY == -2:
		showHint()
	elif posX >= 10 or posY >= 20:
		print("İnvalid Operation")
	elif posX >= 0 and posY >= 0:
		searchHorizontalUpwardLeft(posX,posY-1,letterList[posX][posY])
		searchHorizontalUpwardRight(posX,posY+1,letterList[posX][posY])
		searchHorizontalDownwardLeft(posX,posY-1,letterList[posX][posY])
		searchHorizontalDownwardRight(posX,posY+1,letterList[posX][posY])
		searchVerticalUpward(posX,posY,letterList[posX][posY])
		searchVerticalDownward(posX,posY,letterList[posX][posY])
	else:
		exit()
	checkPlane()
	game()



letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","q","s","t","u","v","w","x","y","z"]
letNum = int(input("Enter number of letters to be used: "))
letterList = []
n = 0
emptyCol = 0
if __name__ == "__main__":
	main()