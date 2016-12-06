import Scope

class BlockStatement(Statement):

  def __init__(self):
    self.statements = []


  def addStatement(self, stmt):
    stmt.parent = self
    self.statements.append(stmt)

    for statement in self.statements:
        statement.allocateSlots()


  def checkTypes(self):
    for statement in self.statements:
        statement.checkTypes()


  def compile(self, pw):
    for statement in self.statements:
        statement.compile(pw)

  def lastStatement(self):
    self.statements[-1]


  def resolveNames(self, scope):
    innerScope = Scope.Scope(scope)

    for statement in self.statements:
        statement.resolveNames(innerScope)
