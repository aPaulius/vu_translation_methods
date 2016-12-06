import Type

class IfStatement(Statement):
  self.condition
  self.body

  def checkTypes(self):
    self.condition.checkTypes()
    self.body.checkTypes()
    if self.condition.type != Type.Type('Bool')
      print 'invalid condition type {}'.format(self.condition.type)


  def compile(self, pw):
    label = pw.newLabel
    self.condition.compile(pw)
    pw.addInstruction(:I_JZ, label)
    self.body.compile(pw)
    pw.placeLabel(label)


  def resolveNames(self, scope):
    self.condition.resolveNames(scope)
    self.body.resolveNames(scope)
