class ExpressionStatement(Statement):

  def __init__(self, expression):
    self.expression = expression


  def allocateSlots(self):
    self.expression.allocateSlots()


  def checkTypes(self):
    self.expression.checkTypes()


  def compile(self, pw):
    self.expression.compile(pw)
    pw.addInstruction(:I_POP)


  def resolveNames(self, scope):
    self.expression.resolveNames(scope)
