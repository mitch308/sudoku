import random

def printSudoku(charArr):
  for i in range(9):
    print(charArr[i*9:(i+1)*9])

def findSolution(charArray,pos):
  row = int(pos/9)
  column = pos%9
  subIndex = int(row/3)*3 + int(column/3)
  arr = [1,2,3,4,5,6,7,8,9]
  for i in range(9):
    if i != row:
      num = charArray[i*9 + column]
      if arr.count(num):
        arr.remove(num)
    if i != column:
      num = charArray[i + row*9]
      if arr.count(num):
        arr.remove(num)
    subPos = (int(subIndex/3)*3 + int(i/3))*9 + (subIndex%3)*3 + (i%3)
    num = charArray[subPos]
    if arr.count(num):
      arr.remove(num)
  return arr

def numSolutionInsub(charArray,num,subIndex):
  res = []
  for rn in range(9):
    pos = (int(subIndex/3)*3 + int(rn/3))*9 + (subIndex%3)*3 + (rn%3)
    if charArray[pos] == 0:
      arr = findSolution(charArray,pos)
      if arr.count(num):
        res.append(pos)
  return res

def createSudoku():
  sudoku = [0]*81
  sudokuArr = []
  posArr = None
  i = 0
  while 1:
    subIndex = i % 9
    num = int(i / 9) + 1
    if posArr == None:
      posArr = numSolutionInsub(sudoku,num,subIndex)
    if len(posArr) == 0:
      i = i - 1
      posArr = sudokuArr[-1][1]
      sudokuArr.pop(-1)
      sudoku = sudokuArr[-1][0]
    else:
      if len(posArr) == 1:
        pos = posArr[0]
      else:
        rn = random.randrange(0, len(posArr)-1, 1)
        pos = posArr[rn]
      sudoku[pos] = num
      posArr.remove(pos)
      sudokuArr.append([sudoku[0:],posArr[0:]])
      posArr = None
      i = i+1
    if i >= 81:
      break
  return sudoku

def calcSudoku(sudoku):
  solutionArr = []
  for i in range(len(sudoku)):
    num = sudoku[i]
    if num > 0:
      solutionArr.append([])
    else:
      solutionArr.append(findSolution(sudoku,i))
  return solutionArr

# sudoku = calcSudoku()
# printSudoku(sudoku)
