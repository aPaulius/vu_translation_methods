import Scope
import Parameter
import Type

class Function(Node):
  self.parameters
  self.name
  self.body
  self.returnType
  self.codeOffset
  self.globalSlot

  def __init__(self):
    self.parameters  = []
    self.name        = null
    self.body        = null
    self.returnType  = null
    self.globalSlot  = null
    self.numberSlots = null

  def allocateSlots(self):
    global globalSlot
    global localSlot

    self.globalSlot = globalSlot
    globalSlot      += 1
    localSlot       = 0

    for parameter in self.parameters:
        parameter.allocateSlots()
    self.body.allocateSlots()
    self.numberSlots = localSlot


  def checkTypes(self):
    self.body.checkTypes()


  def compile(self, pw):
    pw.addGlobal(self.globalSlot)
    # pw.offset ? is variable or method?
    self.codeOffset = pw.offset
    # what to with I_LOCAL_ALLOC ?
    pw.addInstruction(:I_LOCAL_ALLOC, self.numberSlots)
    self.body.compile(pw)

    if not isInstance(self.body.lastStatement, ReturnStatement)
      # what to with I_RET ?
      pw.addInstruction(:I_RET)


  def echo(self, indent = 0):
    output(indent, "FUNCTION {}".format(self.name))

    output(indent + 1, "parameters:")
    for parameter in self.parameters:
        parameter.echo(indent + 2)

    output(indent + 1, "BODY:")
    for statement in self.body:
        statement.echo(indent + 2)

  def resolveNames(self, scope):
    scope.addVar(self.name, self)
    innerScope = Scope.Scope(scope)

    for parameter in self.parameters:
        parameter.addVariable(parameter.name, parameter)

    self.body.resolveNames(innerScope)

  def type(self):
    Type.Type('FnType')
