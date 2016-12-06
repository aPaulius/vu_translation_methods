from parser_config import *

import Expector
import Peeker

class Parser(object):

    tokens   = []
    expector = None
    peeker   = None

    def parse(self, tokens):
        self.tokens   = tokens
        self.expector = Expector.Expector(self.tokens)
        self.peeker   = Peeker.Peeker(self.tokens)
        print '<kodas>'

        while self.peeker.peek('funkcija', self.expector.getPosition()):
            self.parseFunction()

    # parses function
    def parseFunction(self):
        self.expector.expect('funkcija')
        print '  <funkcija>'
        self.expector.expect('funkcijos vardas')
        print '    <funkcijosVardas>'
        self.expector.expect('(')
        self.parseParameters()
        self.expector.expect(')')
        self.expector.expect('{')
        print '    <fragmentas>'
        self.parseStatements()

    # parses parameters
    def parseParameters(self):
        if not self.peeker.peek(')', self.expector.getPosition()):
            print '    <formalusArgumentai>'
            self.parseParameter()

        while True:
            if self.peeker.peek(',', self.expector.getPosition()):
                self.expector.expect(',')
                self.parseParameter()
            else:
                break

    # parses parameter
    def parseParameter(self):
        self.expector.expectOptional('eilute', 'skaicius')
        self.expector.expect('kintamasis')
        print '       <kintamojoVardas>'

    # parses statements
    def parseStatements(self):
        #while self.expector.getPosition() < len(self.tokens):
        while not self.peeker.peek('funkcija', self.expector.getPosition()) and self.expector.getPosition() < len(self.tokens):
            self.parseStatement()

    # parses statement
    def parseStatement(self):
        if self.peeker.peek('kol', self.expector.getPosition()):
            print '      <cikloSakinys>'
            self.parseWhile()
        if self.peeker.peek('jei', self.expector.getPosition()):
            print '      <salygosSakinys>'
            self.parseIf()
        if self.peeker.peek('spausdinti', self.expector.getPosition()):
            print '      <isvedimas>'
            self.parsePrint()
        if self.peeker.peek('grazinti', self.expector.getPosition()):
            print '      <grizimas>'
            self.parseReturn()
        if self.peeker.peek('ivesti', self.expector.getPosition()):
            print '      <ivedimas>'
            self.parseInput()
        if self.peeker.peek('kintamasis', self.expector.getPosition()):
            print '      <priskyrimas>'
            self.parseAssignment()
        if self.peeker.peek('}', self.expector.getPosition()):
            self.expector.expect('}')

    # parses while statement
    def parseWhile(self):
        self.expector.expect('kol')
        print '        kol'
        self.expector.expect('(')
        self.expector.expectOptional('kintamasis', '<skaicius>')
        self.expector.expectComparisonOperator()
        self.expector.expectOptional('kintamasis', '<skaicius>')
        self.expector.expect(')')
        self.expector.expect('{')

    # parses if statement
    def parseIf(self):
        self.expector.expect('jei')
        print '        jei'
        self.expector.expect('(')
        self.expector.expectOptional('kintamasis', '<skaicius>')
        self.expector.expectComparisonOperator()
        self.expector.expectOptional('kintamasis', '<skaicius>')
        self.expector.expect(')')
        self.expector.expect('{')

    # parses print function
    def parsePrint(self):
        self.expector.expect('spausdinti')
        print '        spausdinti'
        self.expector.expect('(')
        self.expector.expectOptional('kintamasis', '<eilute>')
        self.expector.expect(')')
        self.expector.expect(';')

    # parses return function
    def parseReturn(self):
        self.expector.expect('grazinti')
        print '        grazinti'
        self.expector.expectOptional2('kintamasis', '<skaicius>', '<eilute>')
        print '        <parametras>'
        self.expector.expect(';')

    # parses input function
    def parseInput(self):
        self.expector.expect('ivesti')
        print '        ivedimas'
        self.expector.expect('(')
        self.expector.expect('<eilute>')
        print '        <eilute>'
        self.expector.expect(')')
        self.expector.expect(';')

    # parses variable assignment
    def parseAssignment(self):
        self.expector.expect('kintamasis')
        print '        <kintamojoVardas>'
        self.expector.expect('=')
        print '        ='
        self.expector.expectOptional('kintamasis', '<skaicius>')
        self.expector.expectMathOperator()
        self.expector.expectOptional('kintamasis', '<skaicius>')
        self.expector.expect(';')
