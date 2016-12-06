class VariableExpression(Expression):
    
  self.target

  def __init__(self, name):
    self.name = name


  def checkTypes(self):


  def compile(self, pw):
    pw.addInstruction(:I_GET, self.target.localSlot)


  def resolveNames(self, scope):
    self.target = scope.lookup(self.name)
    print 'resolve {} -> {}'.format(self.name, self.target)


  def type(self):
    if self.target and self.target.type:
      self.target.type
    else:
      raise Exception('err')
