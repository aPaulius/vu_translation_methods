class Node(object):

    def __init__():
        self.parent = null

    def allocateSlots(self):
        null


    def checkTypes(self):
        raise Exception('Not implemented {}'.format(instance.__class__.__name__))


    def compile(self, pw):
        raise Exception('Not implemented {}'.format(instance.__class__.__name__))


    def isConst(self):
        return True


    def output(self, indent, str):
        print '*' * indent, str


    def echo(self, indent = 0):
        output(indent, "?????")


    def resolveNames(self, scope):
        null