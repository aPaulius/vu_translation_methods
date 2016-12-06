from parser_config import *

class Expector(object):

        tokens   = []
        position = 0

        def __init__(self, tokens):
            self.tokens = tokens

        # checks if given type is equal to current token in array
        def expect(self, type):
            token = self.tokens[self.position]

            if token == tokenValues[type]:
                self.position += 1
                    
                return self.position
            else:
                tokenKey = tokenValues.keys()[tokenValues.values().index(token)]

                raise Exception(
                    'Found {}, but expected {}'
                    .format(tokenKey, type)
                )

        # checks if given types are equal to current token in array
        def expectOptional(self, type1, type2):
            token = self.tokens[self.position]

            if token == tokenValues[type1] or token == tokenValues[type2]:
                self.position += 1

                self.printType(token, type1, type2)

                return self.position
            else:
                tokenKey = tokenValues.keys()[tokenValues.values().index(token)]

                raise Exception(
                    'Found {}, but expected {} or {}'
                    .format(tokenKey, type1, type2)
                )

        # checks if given types are equal to current token in array
        def expectOptional2(self, type1, type2, type3):
            token = self.tokens[self.position]

            if token == tokenValues[type1] or token == tokenValues[type2] or token == tokenValues[type3]:
                self.position += 1

                return self.position
            else:
                tokenKey = tokenValues.keys()[tokenValues.values().index(token)]

                raise Exception(
                    'Found {}, but expected {} or {} or {}'
                    .format(tokenKey, type1, type2, type3)
                )

        # checks if current token is a comparison operator
        def expectComparisonOperator(self):
            token = self.tokens[self.position]

            if token in comparisonOperators:
                self.position += 1

                print '           ', tokenValues.keys()[tokenValues.values().index(token)]

                return self.position
            else:
                tokenKey = tokenValues.keys()[tokenValues.values().index(token)]

                raise Exception(
                    'Found {}, but expected comparison operator (<, >, ==, >=, <=, !=).'
                    .format(tokenKey)
                )

        # checks if current token is a math operator
        def expectMathOperator(self):
            token = self.tokens[self.position]

            if token in mathOperators:
                self.position += 1

                print '           ', tokenValues.keys()[tokenValues.values().index(token)]

                return self.position
            else:
                tokenKey = tokenValues.keys()[tokenValues.values().index(token)]

                raise Exception(
                    'Found {}, but expected math operator (+, -, *, /).'
                    .format(tokenKey)
                )

        # gets current position
        def getPosition(self):
            return self.position

        def printType(self, token, type1, type2):
            if token == tokenValues[type1]:
                print '      ', type1
            else:
                print '      ', type2
