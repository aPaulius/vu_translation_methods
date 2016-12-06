from ast_config import *
import Statement

class AssignStatement(Statement):
    self.target
    self.target_name
    self.value

    def allocateSlots(self):
        self.value.allocateSlots()

    def checkTypes(self):
        self.value.checkTypes()

    if self.target:
        if self.target.type != self.value.type:
            print 'incompatible types in assignment'
        if self.target.isConst():
            print 'attempt to assign constant variable'

    def compile(self, pw):
        self.value.compile(pw)
        pw.addInstruction(tokenValues[30], self.target.localSlot)

    def resolveNames(self, scope):
        self.target = scope.lookup(self.targetName)
        self.value.resolveNames(scope)
