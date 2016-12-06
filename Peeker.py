from parser_config import *

class Peeker(object):
    tokens = []

    def __init__(self, tokens):
        self.tokens = tokens

    # peeks next value
    def peek(self, type, position):
        if len(self.tokens) <= position:
            return False

        token = self.tokens[position]

        if token == tokenValues[type]:
            return True

        return False

    # peeks next value
    def optionalPeek(self, type1, type2, position):
        token = self.tokens[position]

        if token == tokenValues[type1] or token == tokenValues[type2]:
            return True
        else:
            return False
