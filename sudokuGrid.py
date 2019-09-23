import tkinter

class SudokuGrid:
  def __init__(self, root, index, selectEvent):
    self.root = root
    self.solutionLabels = [None]*9
    self.index = index
    self.selectEvent = selectEvent
    self.draw()

  def draw(self, solutionArr):
    for i in range(9):
      num = i+1
      if solutionArr[i].count(num) == 0:
        num = ''
      if self.solutionLabels[i] == None:
        self.solutionLabels[i] = tkinter.Label(self.root, text=num, font=('Arial', 6))
        self.solutionLabels[i].bind("<Button-1>", self.selectHandle)
      else:
        self.solutionLabels[i].config(text=num)
      self.solutionLabels[i].place(x=(i%3)*10, y=int(i/3)*10, width=10, height=10)

  def selectHandle(self, event):
    self.selectEvent(self.index)
