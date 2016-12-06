import Type

class ConstantExpression(Expression):

  def __init__(value):
    self.value = value


  def checkTypes(self):


  def compile(self, pw):
    pw.addInstruction(:I_PUSH_INT, self.value.value)


  def type(self):
    if self.value.type == :T_LIT_INT:
      Type.Type('Int')
    else if self.value.type == :T_LIT_STRING:
      Type.Type('String')
    else:
      raise Exception('internal error')
