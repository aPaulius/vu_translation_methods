class EqualExpression(BinaryOperationExpression):

  def compile(self, pw):
    super().__init__(pw)
    pw.addInstruction(:I_EQ)
