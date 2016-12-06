class Call(Expression):
  self.target
  self.arguments

  def checkTypes(self):
    functionDeclaration = self.target.target
    if len(self.arguments) != len(functionDeclaration.parameters)
      print 'error: incorrent number of arguments {} vs {}'.format(len(self.arguments), len(functionDeclaration.parameters))

      return

    for argument in self.arguments:
        argument.checkTypes()

    for i range(0, len(self.arguments) - 1):
      type0 = self.arguments[i].type
      type1 = functionDeclaration.parameters[i].type
      print 'ZZ {} {}'.format(self.arguments[i].__class__.__name__, type0])
      if type0 != type1:
        print 'error: wrong argument type {} vs {}'.format(type0, type1)
        pp(self.arguments[i])
        pp(functionDeclaration.parameters[i])


  def compile(self, pw):
    for argument in self.arguments:
        argument.compile(pw)

    pw.addInstruction(:I_CALL, self.target.target.codeOffset, len(self.arguments))


  def resolveNames(self, scope):
    self.target.resolveNames(scope)

    for argument in self.arguments:
        argument.resolveNames(scope)


  def type(self):
    functionDeclaration = self.target.target
    functionDeclaration.returnType()
