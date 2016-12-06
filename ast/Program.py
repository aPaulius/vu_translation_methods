class Program(Node):

  def __init__(self):
    self.functions = []

  def addFunction(self, function):
    function.parent = self
    self.functions.append(function)

  def allocateSlots(self):
    for function in self.functions:
        function.allocateSlots()

  def checkTypes(self):
    for function in self.functions:
        function.checkTypes()

  def compile(self, pw):
    for function in self.functions:
        function.compile(pw)

  def echo(self, indent = 0):
    output(indent, "PROGRAM")
    for function in self.functions:
      function.echo(indent + 1)

  def resolveNames(self, scope):
     for function in self.functions:
         function.resolveNames(scope)
