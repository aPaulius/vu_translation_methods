class ReturnStatement(Statement):
  self.value

  def __init__(self):
    self.value = null


  def checkTypes(self):
    print 'check return type {}'.format(instance.__class__.__name__)

    if self.value:
        self.value.checkTypes()


  def compile(self, pw):
    if self.value:
      self.value.compile(pw)
      pw.addInstruction(:I_RET_VALUE)
    else:
      pw.addInstruction(:I_RET)


  def resolveNames(self, scope):
     if self.value:
         self.value.resolveNames(scope)
