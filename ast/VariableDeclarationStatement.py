class VariableDeclarationStatement(Statement):
  self.name
  self.type
  self.localSlot

  def allocateSlots(self):
    global localSlot

    self.localSlot  = localSlot
    localSlot      += 1

  def checkTypes(self):

  def compile(self, pw):

  def isConst(self):
    return False

  def resolveNames(self, scope):
    scope.addVariable(self.name, self)
