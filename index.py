import tkinter
from util import *

win = tkinter.Tk()
win.title('sudoku')
win.geometry('400x400')

sudokuFrame = tkinter.Frame(win)
sudokuFrame.pack()
sudokuFrame.place(width=288, height=288, x=50, y=50)

sudoku = [0]*81
solutionArr = calcSudoku(sudoku)

sudokuFrames = []
sudokuLabels = []
solutionLabels = []
selectedFrame = None

for i in range(81):
  sudokuFrames.append(tkinter.Frame(sudokuFrame, highlightbackground='black', highlightthickness=1))
  sudokuFrames[i].pack()
  sudokuFrames[i].place(x=(i%9)*31, y=int(i/9)*31, width=32, height=32)
  solutionLabels.append([])
  for j in range(9):
    num = j+1
    if solutionArr[i].count(num) == 0:
      num = ''
    solutionLabels[i].append(tkinter.Label(sudokuFrames[i], text=num, font=('Arial', 6)))
    solutionLabels[i][j].place(x=(j%3)*10, y=int(j/3)*10, width=10, height=10)

l = tkinter.Label(win, text='展示信息', font=('Arial', 20))
l.pack()

def selectFrame(event):
  print(event.x, event.y)
  print(event.widget)
  print(dir(event))
  l.config(text=str(event.x)+'|'+str(event.y))

# win.bind("<Button-1>", selectFrame)
# l.bind("<Button-1>", selectFrame)
sudokuFrames[0].bind("<Button-1>", selectFrame)

# def drawSudoku(sudoku, solutionArr):
  

# drawSudoku(sudoku, solutionArr)



win.mainloop()
