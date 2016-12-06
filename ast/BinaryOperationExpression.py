import Type

class BinaryOperationExpression(Node):

  self.type

  def __init__(self, expression0, expression1):
    self.expression0 = expression0
    self.expression1 = expression1


  def checkTypes(self):
    self.expression0.checkTypes()
    self.expression1.checkTypes()
    if self.expression0.type != self.expression1.type:
      print 'incompatible types {} and {}'.format(self.expression0.type, self.expression1.type)
      self.type = Type.Type('Invalid')
    else:
      self.type = self.expression0.type


  def compile(self, pw):
    self.expression0.compile(pw)
    self.expression1.compile(pw)


  def echo(self, indent = 0):
    output(indent, "BIN_EXP {}".format(instance.__class__.__name__))
    self.expression0.echo(indent + 1)
    self.expression1.echo(indent + 1)


  def resolveNames(self, scope):
    self.expression0.resolveNames(scope)
    self.expression1.resolveNames(scope)
